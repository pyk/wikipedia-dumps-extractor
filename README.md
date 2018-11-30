# Wikipedia Dumps Extractor
This repository contains a python script that I use to extract
title and content from
[Wikipedia dumps data](https://id.m.wikipedia.org/wiki/Wikipedia:Unduh_basis_data).

To run it, clone the repository:

    git clone https://github.com/pyk/wikipedia-dumps-extractor.git

Install the dependencies:

    pipenv install

Run the script:

    pipenv run python extract.py wiki-latest-pages-articles.xml

This script use incremental parsing, so it doesn't consume too much
memory.

Enjoy.
