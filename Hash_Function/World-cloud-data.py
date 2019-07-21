'''
You want to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the body of text.

To do this, you'll need data. Write code that takes a long string and builds its word cloud data in a dictionary ↴ , where the keys are words and the values are the number of times the words occurred.

Think about capitalized words. For example, look at these sentences:

'After beating the eggs, Dana read the next step:'
'Add milk and eggs, then add flour and sugar.'

What do we want to do with "After", "Dana", and "add"? In this example, your final dictionary should include one "Add" or "add" with a value of 22. Make reasonable (not necessarily perfect) decisions about cases like "After" and "Dana".

Assume the input will only contain words and standard punctuation.
'''

import string


class WordCloudData(object):
    def __init__(self, input_string):

        # Count the frequency of each word

        self.words_to_counts = {}
        self.input_string = input_string

    def remove_punctuation(self, s):
        parsed_string = "".join(
            c for c in s if c not in ('!', '.', ':', '-'))
        return parsed_string

    def count_words(self):
        temp_string = self.remove_punctuation(self.input_string)
        split_string = temp_string.split(' ')
        for word in split_string:
            if word in self.words_to_counts:
                self.words_to_counts[word] += 1
            else:
                self.words_to_counts[word] = 1

        return self.words_to_counts


if __name__ == "__main__":
    test_1 = 'I like cake'
    test_2 = 'Chocolate cake for dinner and pound cake for dessert'
    test_3 = 'Strawberry short cake? Yum!'
    test_4 = 'Mmm... mmm... decisions... decisions'

    data1 = WordCloudData(test_1)
    data2 = WordCloudData(test_2)
    data3 = WordCloudData(test_3)
    data4 = WordCloudData(test_4)

    print(data1.count_words())
    print(data2.count_words())
    print(data3.count_words())
    print(data4.count_words())
