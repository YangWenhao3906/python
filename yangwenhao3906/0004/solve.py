from collections import Counter

def word_frequency_count(file_name):
    with open("text.txt","r") as file:
        content = file.read()

    words = content.split()

    word_counts = Counter(words).most_common()

    for word, count in word_counts:
        print(f"{word}: {count}")

word_frequency_count("text.txt")