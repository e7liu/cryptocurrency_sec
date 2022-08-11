from common import load_paper_data_from_file
from common import convert_string_to_filename
from common import MD_TEMPLATE
import os

def dump_paper_as_md(paper):
	filename = "../_posts/{}-01-01-{}.md".format(paper.year,convert_string_to_filename(paper.title))

	if os.path.exists(filename):
		print("Paper: {}\nExists\n".format(filename))
		return

	if paper.tags == None:
		paper.tags = []
	if paper.year != None:
		paper.tags.append(str(paper.year))
	if paper.venue != None:
		paper.tags.append(paper.venue)

	with open(filename, "w") as f:
		f.write(MD_TEMPLATE.format(
			paper.title,
			paper.tags,
			paper.year,
			paper.venue if paper.venue != None else "Venue not available",
			", ".join(paper.authors) if paper.authors != None else "Authors not available",
			paper.abstract if paper.abstract != None else "Abstract not available",
			))

def main():
	papers = load_paper_data_from_file()
	for paper in papers:
		dump_paper_as_md(paper)
		# break

if __name__ == "__main__":
	main()