import json
from os import listdir

class Paper():
	def __init__(self, title):
		self.title = title
		self.tags = None
		self.authors = None
		self.abstract = None
		self.venue = None
		self.year = None

	def add_tags(self, tags):
		self.tags = tags

def dump_paper_data_to_file(paper_obj):
	obj = json.dumps(paper_obj.__dict__, indent=4)
	# Writing to sample.json
	with open("../data/from_semanticscholar/{}.json".format(convert_string_to_filename(paper_obj.title)), "w") as outfile:
		outfile.write(obj)

def convert_string_to_filename(s):
	if s == None:
		return s

	# Not allowing space
	valid_chars = "%s%s" % (string.ascii_letters, string.digits)
	return ''.join(c for c in s if c in valid_chars)

def load_paper_data_from_file():
	papers = []

	for f in listdir("../data/from_semanticscholar"):
		if ".json" not in f:
			continue

		with open("{}/{}".format("../data/from_semanticscholar",f), 'r') as openfile:
			# Reading from json file
			json_object = json.load(openfile)
			papers.append(json)
			
	return papers