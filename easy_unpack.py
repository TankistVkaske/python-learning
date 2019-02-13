
def easy_unpack(elements):
    if len(elements) < 3:
        return "Number of elements is less than 3!"
    else:
        return elements[0], elements[2], elements[-1]


if __name__ == "__main__":
    arg1 = ('k', 'e', 'k')
    arg2 = ()
    arg3 = ('k', 'e')
    arg4 = (1, 2, 3, 4, 5)
    print(easy_unpack(arg1))
    print(easy_unpack(arg2))
    print(easy_unpack(arg3))
    print(easy_unpack(arg4))
    print(type(easy_unpack(arg4)))
