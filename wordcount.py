# put your code here.
def get_word_count(file_name):
    text = open(file_name)
    word_counts = {}
    for line in text:
        line.rstrip()
        line.strip()
        words = line.split(" ")
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
    for key in word_counts:
        print(f"{key}, {word_counts[key]}")
    return word_counts

get_word_count("test.txt")
