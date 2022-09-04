sentence= input('Enter the sentence: ')  #take input from user

def reverse(sent):
    words_in_sentence= sent.split()
    words_in_sentence.reverse()

    return ' '.join(words_in_sentence)


reversed= reverse(sentence)  #reverse of given sentence

print('Reversed Sentence is: ', reversed)  #result
