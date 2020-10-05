# put your code here.
import sys

def get_word_count():
    # read the filename from the command line
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
            word = word.lower()
            word_counts[word] = word_counts.get(word, 0) + 1

    sorted_word_counts = reversed(sorted(word_counts.items(), key=lambda x: x[1]))
    for i in sorted_word_counts:
    	print(i[0], i[1])        
    
    return word_counts
    
get_word_count()