"""
This program is developed for counting the number of words in a file.
DATE : 14-07-2020
DEVELOPER : SURIYA KRISHNAN
"""

import collections
import re


def counts(input_file, output_file):
    # Initialization a list
    words_list = []

    # Reading the input file(data.txt)
    with open(file=input_file, mode='r') as file:
        for line in file:
            for words in line.lower().strip().split():
                words_list.append(''.join(re.split("[^a-zA-Z-*]", words)))

    # Counting the appearances using collections
    appearances = collections.Counter(words_list)

    # Writing the output in a file(result.txt)
    with open(file=output_file, mode='w') as write:
        for key, value in appearances.items():
            if key not in '-':
                write.write((key + ' (' + str(value) + ')\n'))


if __name__ == '__main__':
    input_file_path = "data.txt"
    output_file_path = "result.txt"
    counts(input_file_path, output_file_path)
