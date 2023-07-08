# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

import os
import nltk
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def count_most_important_word(folder_path):

    # 下载停用词列表（只需要执行一次）
    nltk.download('stopwords')

    nltk.download('punkt')

    # 加载英文停用词列表
    stop_words = set(stopwords.words('english'))


    with open("count_2_"+folder_path, "w") as count_file:

        # 打开文件夹,逐个文件读取
        for file_name in os.listdir(folder_path):

            file_path = os.path.join(folder_path, file_name)

            with open(file_path) as file:
                text = file.read()

                # # 分词1
                # tokens = text.split()

                # 分词2
                tokens = word_tokenize(text)
                tokens = [token for token in tokens if token not in string.punctuation]

                # 去除停用词
                filtered_tokens = [word for word in tokens if not word.lower() in stop_words]

                # 统计
                token_count = Counter(filtered_tokens).most_common()
                token_count = token_count[0]

                # 将最常用的写入
                count_file.write(str(file_name) + ": " + str(token_count) + "\n")
                
count_most_important_word("diary")