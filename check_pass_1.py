import string

upper = set(string.ascii_uppercase)
lower = set(string.ascii_lowercase)
digits = set(string.digits)


def checkio(data):
    'Return True if password strong and False if not'
    letters = set(data)
    return bool(len(data) >= 10 and upper & letters and lower & letters and digits & letters)

if __name__ == '__main__':
    assert checkio('A1213pokl')==False, 'First'
    assert checkio('bAse730onE4+()===') is True, 'Second'
    print('All ok')