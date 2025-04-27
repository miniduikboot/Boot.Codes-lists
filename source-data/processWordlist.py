#!/usr/bin/env python
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("length", type=int)
parser.add_argument("prevalence", type=float)
parser.add_argument("--safe", action="store_true")
args = parser.parse_args()

badwords = set()
badfiles = ["bad-words.txt", "miniban.txt"]

if args.safe:
    for badfile in badfiles:
        with open(badfile, "r") as f:
            for bad in f.readlines():
                badwords.add(bad.split(' ')[0].strip())

print(
    """-- Word list for Boot.Codes: http://github.com/miniduikboot/Boot.Codes-lists
-- Based off research from UGent: http://crr.ugent.be/archives/2045
-- Licensed under the CC-BY-NC-SA 4.0 https://creativecommons.org/licenses/by-nc-sa/4.0/"""
)

with open("WordprevalencesSupplementaryfilefirstsubmission.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=" ", quotechar='"')
    for row in reader:
        word = row[0]
        prev = float(row[3].replace(",", "."))
        if (
            len(word) == args.length
            and prev >= args.prevalence
            and word not in badwords
        ):
            print(word.upper())
