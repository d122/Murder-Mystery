#!/usr/bin/env python

file1 = open("1.TXT").read()
file2 = open("2.TXT").read()
corpus = file1 + file2

all_chars = corpus.lower()\
                  .replace(" ", "")\
                  .replace("*", "")\
                  .replace(")", "")\
                  .replace("(", "")\
                  .replace(" ", "")

print all_chars

print "#######################################################################"

def count_words(word):
    word_count = 0
    for line in all_lines:
        word_count += line.count(word)

    return word_count

all_lines = all_chars.split("\n")

max_line_length = max([len(line)for line in all_lines])

output_file = open("output.csv","w")

#word_size = 2
#for word_size in xrange(max_line_length):
for word_size in xrange(1,11):
    print "############ WORD SIZE : %d ##########################################" % word_size
    all_words = []
    for line in all_lines:
        if len(line) >= word_size:
            for new_word in [line[x:x+word_size] for x in xrange(0,len(line)-word_size + 1)]:
                if not new_word in all_words:
                    all_words.append(new_word)
#    print all_words

    counted_words = {}
    for word in all_words:
        counted_words[word] = count_words(word)
        print "%s, %s\n" % (word, count_words(word))
        output_file.write("%s, %s\n" % (word, count_words(word)))

#    print counted_words


