import xml.etree.ElementTree as ET
import mwparserfromhell
import sys

def main():
    # Check the argument
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "wiki-latest-pages-articles.xml")
        sys.exit(1)
    idwikifile = open(sys.argv[1])
    output = open("output.txt", "w")
    tree = ET.iterparse(idwikifile, events=["start", "end"])
    for event, elem in tree:
        if elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}title" and event == "start":
            if elem.text is not None:
                output.write(elem.text + "\n")
        elif elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}text" and event == "start":
            if elem.text is not None:
                wikicode = mwparserfromhell.parse(elem.text)
                # Remove empty line
                clean_texts = []
                raw_texts = wikicode.strip_code().strip().split("\n")
                for text in raw_texts:
                    if text.strip() == "":
                        continue
                    clean_texts.append(text)
                clean_text = "\n".join(clean_texts)
                output.write(clean_text + "\n")
        elem.clear()

    print("File generated: output.txt")
    output.close()

if __name__ == "__main__":
    main()