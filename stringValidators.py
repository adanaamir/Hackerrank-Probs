if __name__ == '__main__':
    s = input()

    for i in s:
        if i == s.isalnum():
            print("True")
        else:
            print("False")
        if i == s.isalpha():
            print("True")
        else:
            print("False")
        if i == s.isdigit():
            print("True")
        else:
            print("False")
        if i == s.islower():
            print("True")
        else:
            print("False")
        if i == s.isupper():
            print("True")
        else:
            print("False")