from common import load_paper_data_from_file
from common import convert_string_to_filename
from common import MD_TEMPLATE
import os

def dump_paper_as_md(paper):
	filename = "../_posts/{}-01-01-{}.md".format(paper.year,convert_string_to_filename(paper.title))

	if os.path.exists(filename):
		print("Paper: {}\nExists\n".format(filename))
		return

	with open(filename, "w") as f:
		f.write(MD_TEMPLATE.format(
			paper.title,
			paper.tags,
			paper.abstract if paper.abstract != None else "Abstract not available",
			paper.year,
			paper.venue if paper.venue != None else "Venue not available",
			))

def main():
	papers = load_paper_data_from_file()
	for paper in papers:
		dump_paper_as_md(paper)
		break

if __name__ == "__main__":
	main()