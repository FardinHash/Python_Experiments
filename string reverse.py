string = input('Enter the string: ')

def reverse(string):
    reverse= ''
    for character in string:
        reverse= character+reverse

    return reverse


reversed_string= reverse(string)
print('Reversed String is: ', reversed_string)
