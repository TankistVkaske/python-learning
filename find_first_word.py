
def first_word(text):
    for group in text.split(' '):
        if len(group) > 1 and (map(str.isalpha, group) or '\'' in group):
            word = group
            return word




if __name__ == '__main__':
    print(first_word("kek, ivan"))
