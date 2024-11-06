def main(s):
    print("True" if s.isalnum() else "False")
    print("True" if s.isalpha() else "False")
    print("True" if s.isdigit() else "False")
    print("True" if s.islower() else "False")
    print("True" if s.isupper() else "False")

if __name__ == '__main__':
    s = input()
    main(s)
