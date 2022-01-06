import yaml
from extract import *
from summarize import summarize
import argparse


def main():
    argument_parser = argparse.ArgumentParser(description="make buzz corner")
    argument_parser.add_argument("url", type=str, help="url for website")
    argument_parser.add_argument("-o", "--output",
                                 action="store",
                                 help="output file. Will append if file not empty")
    arguments = argument_parser.parse_args()
    # url = "https://mlcommons.org/en/news/neurips21/"
    url = arguments.url
    title, content = extract_title_content(url)

    summary = summarize(content)

    try:
        with open(arguments.output, "r") as f:
            entries = yaml.safe_load(f)
    except IOError:
        entries = {"links": []}
    entry = {
        "title": title,
        "url": url,
        "description": summary
    }
    entries["links"].append(entry)
    with open(arguments.output, "w") as f:
        yaml.safe_dump(entries, stream=f)


if __name__ == "__main__":
    main()
