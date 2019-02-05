import re


def checkio(password):
    validate = re.fullmatch("[a-zA-Z0-9]+", password)
    is_valid = False
    if validate:
        if 10 <= len(password) < 64 and re.search("[0-9]", password) and \
                re.search("[a-z]", password) and re.search("[A-Z]", password):
            print("Nice Password!")
            is_valid = True
        else:
            print("Password doesnt match requirements!")
    else:
        print("Wrong characters or empty!")
    return is_valid


#Some hints
#Just check all conditions


if __name__ == '__main__':
    assert checkio('123') is False, "#Empty password"
    assert checkio('AAAbbbb123') is True, "#Empty password"
    assert checkio('') is False, "#Empty password"
    assert checkio('Aa1') is False
    assert checkio(('Aaaaaaaa1')) is False

    """assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")"""