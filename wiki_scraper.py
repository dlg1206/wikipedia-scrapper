"""
file: wiki_scraper.py
Description: generates random english or dutch words to data file

@author Derek Garcia
"""
import random
import re
import sys

import requests

# Rand wikipedia urls
RAND_WIKIPEDIA = "wikipedia.org/wiki/Special:Random"

APPROX_WORD_PER_LINE = 15   # sometimes non-alphanumeric characters are counted as "words"

def get_random_wiki_page(lang):
    return requests.get(f"https://{lang}.{RAND_WIKIPEDIA}")

def scrape(mode, lang, max_lines, out_file):
    """
    Scrapes wikipedia for random words

    :param mode: data generation mode
    :param lang: langauge to generate words for
    :param max_lines: max lines of output file
    :param out_file: file to write out to
    """
    # open out file
    with open(out_file, 'w', encoding="utf-8") as file:
        num_line = 1

        # keep writing until return
        while 1:

            # get lang to query
            match lang.lower():
                # randomly assign lang if 'mix' lang
                case "rand":
                    rand = random.randint(0, 1)
                    if rand:
                        query_lang = "en"
                    else:
                        query_lang = "nl"
                # alternate articles, roughly 50/50
                case "en:nl":
                    # every other line
                    if num_line % 2:
                        query_lang = "en"
                    else:
                        query_lang = "nl"
                case _:
                    query_lang = lang

            # query random wikipedia page of respective target lang
            response = get_random_wiki_page(query_lang)

            print(f"{round(100 * (num_line / max_lines), 1)}% | {response.url}")    # status msg to cli

            # get all p-tag content
            r = re.compile("<p>([\\S\\s]*?)<\\/p>")
            data = r.findall(response.text)

            for d in data:
                # clean raw p-tag content
                text = d.replace("\n", "")
                text = re.sub("   *", "", text)                         # rm excessive whitespace
                text = re.sub("[a-zA-Z0-9]*&#[a-zA-Z0-9]*;", "", text)  # rm raw unicode
                text = re.sub("{\\.*}", "", text)                       # rm some math js stuff
                text = re.sub("<[^<>]+>", "", text).strip()             # rm remaining html tags + content

                # build dat file with clean-ish data
                frag = ""
                for word in text.split(" "):

                    # If current fragment is correct length, write to file
                    if len(frag.split(" ")) == APPROX_WORD_PER_LINE:
                        frag = frag.strip() + "\n"

                        # append training header if in train mode
                        if mode.lower() == "train":
                            frag = f"{query_lang}|{frag}"

                        # update vars
                        file.write(frag)
                        frag = ""
                        num_line = num_line + 1

                        # if meet line count, break
                        if num_line > max_lines:
                            print("100.0% | Complete")
                            return

                    # add the word to the current fragment
                    else:
                        frag += word + " "


if __name__ == '__main__':
    try:
        scrape(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4])
    except:
        print("Failed to generate data")
        print("Expected usage: wiki_scraper.py <mode> <lang> <max_lines> <out_file>")
        print("\tmode: train or test (gen w/ or w/o lang prefix)")
        print("\tlang: en, nl, en:nl, or rand")
        print("\tmax_lines: max lines of generated data file")
        print("\tout_file: path to output file")
