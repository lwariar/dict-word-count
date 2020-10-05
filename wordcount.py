# put your code here.
import sys

def get_word_count():
    text = open(sys.argv[1])
    word_counts = {}
    for line in text:
        # remove the trailing spaces and new line chars
        line = line.rstrip()

        words = line.split(" ")
        for word in words:
            # remove the commas, question marks and periods at the end of the words
            word = word.rstrip(',')
            word = word.rstrip('.')
            word = word.rstrip('?')
            word_counts[word] = word_counts.get(word, 0) + 1
    for key in word_counts:
        print(f"{key} {word_counts[key]}")
    return word_counts

get_word_count()