import re


def checkio(text):
    if not text:
        return None
    if len(text) > 10000:
        return None
    unique_characters = set(text) - set(' ')
    unique_characters = {c.lower() for c in unique_characters if c.isalpha()}
    print(unique_characters)
    all_chars_matching = dict()
    most_wanted = dict()
    for unique_char in unique_characters:
        matches = 0
        for char in text:
            if unique_char == char.lower():
                matches += 1
        all_chars_matching.update({unique_char: matches})

    max_matches = max(all_chars_matching.values())
    print("Max", max_matches)
    for item, key in all_chars_matching.items():
        if key == max_matches:
            most_wanted.update({item: key})
    print(all_chars_matching)
    return min(most_wanted.keys())


if __name__ == '__main__':
    print(checkio("AAaooo!!!!"))
    print(checkio("12OOnnNee"))
