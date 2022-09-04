sentence= input('Enter the sentence: ')

def reverse(sent):
    words_in_sentence= sent.split()
    words_in_sentence.reverse()

    return ' '.join(words_in_sentence)


reversed= reverse(sentence)
print('Reversed Sentence is: ', reversed)
