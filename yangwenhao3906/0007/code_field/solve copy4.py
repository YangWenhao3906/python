# 任一个英文的纯文本文件，统计其中的单词出现的个数。

from collections import Counter

def word_frequency_count(file_name):
    with open(file_name,"r") as file:
        content = file.read()

    # TODO split()没有去除所有标点
    # 比如测试用例中, 同时存在"together","together,","together."
    words = content.split()

    word_counts = Counter(words).most_common()

    with open("word_frequency_"+file_name,"w") as dst_file:
        for word, count in word_counts:
            print(f"{word}: {count}")
            dst_file.write(f"{word}: {count}\n")

word_frequency_count("text.txt")