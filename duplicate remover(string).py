string= input('Enter the string: ')


def remove_dup(your_str):
    result = ''
    for char in your_str:
        if char not in result:
            result += char
    return result


removed= remove_dup(string)
print('New String: ', removed)
