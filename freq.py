#!/usr/bin/env python

file1 = open("1.TXT").read()
file2 = open("2.TXT").read()
corpus = file1 + file2

all_chars = corpus.replace(" ", "").replace("*", "").replace("\n", "")

alph = {}
for x in all_chars:
  if x in alph:
    alph[x] = alph[x] + 1
  else:
    alph[x] = 1

for x in alph:
  print "%s, %d" % (x, alph[x])

