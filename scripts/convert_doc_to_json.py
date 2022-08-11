
tags = {}

line = None

import requests
import urllib.parse
import time 
import difflib
import json
import string
from os import listdir
from unidecode import unidecode
from common import dump_paper_data_to_file
from common import load_paper_data_from_file
from common import Paper

total_querys = 0

def to_ascii(s):
	if s == None:
		return s
	return unidecode(s, errors="replace")

def query_paper_by_id(paperID):
	global total_querys
	authors, abstract, venue, year = None, None, None, None

	query = "https://api.semanticscholar.org/graph/v1/paper/{}?fields=title,abstract,authors,venue,year".format(paperID)
	response = requests.get(query)
	total_querys += 1
	# Handle
	if response.status_code != 200:
		raise Exception("Error: Wrong Response Code ({}), Raw: {}\n".format(response.status_code, response.text))

	data = response.json()
	if 'title' not in data:
		raise Exception("Error: Response Format Exception, Raw: {}\n".format(response.text))

	if "venue" in data:
		venue = to_ascii(data['venue'])

	if "abstract" in data:
		abstract = to_ascii(data['abstract'])

	if "authors" in data:
		authors = [to_ascii(author['name']) for author in data['authors']]

	if "year" in data:
		year = data['year']

	time.sleep(2)
	return authors, abstract, venue, year


def query_papers_matching_title(title, tags = None, venue = None):
	global total_querys
	print("Paper: {}".format(title))
	paper_obj = Paper(title)
	paper_obj.add_tags(tags)
	paper_obj.venue = venue

	title_formatted = urllib.parse.quote(title.strip())
	query = "http://api.semanticscholar.org/graph/v1/paper/search?query={}".format(title_formatted)

	response = requests.get(query)
	total_querys += 1

	# Handle
	if response.status_code != 200:
		print("Error: Wrong Response Code ({}), Raw: {}\n".format(response.status_code, response.text))
		return 
	data = response.json()
	if 'total' not in data:
		print("Error: Response Format Exception, Raw: {}\n".format(response.text))
		return

	if int(data['total']) == 0:
		print("Error: No paper found, Raw: {}\n".format(response.text))
		return
	
	for paper_data in data['data']:
		paperID = paper_data['paperId']
		paperTitle = to_ascii(paper_data['title'])
		if difflib.SequenceMatcher(None,paperTitle,title).ratio() > 0.7:
			try:
				authors, abstract, venue, year = query_paper_by_id(paperID)
			except Exception as e:
				print(e)
				return

			paper_obj.authors = authors
			paper_obj.abstract = abstract
			paper_obj.year = year
			# Venue from scholar is not accurate
			if paper_obj.venue == None or paper_obj.venue == "SSRN":
				paper_obj.venue = venue

			break
	else:
		print("Error: No matching paper found, Raw: {}\n".format(response.text))
		return

	# Dump
	dump_paper_data_to_file(paper_obj)
	print("Success!\n")
	time.sleep(2)	

def clean_paper_title(line):
	# Paper title
	line = unidecode(line)
	line = line.strip()

	# Formatted with conference info
	bracket_start = line.rindex("(")
	title = line[:bracket_start].strip()
	venue = line[bracket_start:].strip('()').strip().split("'")[0].strip()
	return title, venue

def main():
	existing_papers = load_paper_data_from_file()
	existing_papers = set(paper.title for paper in existing_papers)

	with open("../data/raw/doc.md") as f:
		for line in f:
			line = unidecode(line.strip()).strip()

			# Empty
			if len(line) == 0:
				continue

			# Tags
			if line.startswith("#"):
				lvl = line.count('#')
				# print(lvl)
				if int(lvl) >= 3:
					# Clear tags
					if int(lvl) in tags:
						del tags[int(lvl)]
					if int(lvl) + 1 in tags:
						del tags[int(lvl) + 1] 

					tags[int(lvl)] = line.strip("#")
					# print(tags)
				continue

			# Unknown
			if not ("(" in line and line.endswith(")") and "'" in line):
				continue

			# Paper
			title, venue = clean_paper_title(line)
			#print(title, venue)
			if title in existing_papers:
				print("Paper: {}".format(title))
				print('Data Exist!\n')
				continue

			query_papers_matching_title(title, list(tags.values()), venue)

			# Don't overload the server
			if total_querys % 80 == 0:
				time.sleep(600)


if __name__ == "__main__":
	main()