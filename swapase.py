def swap_case(s):
    result = ""  #creating an empty string to store the newly converted statment
    while True:
        for i in s:
            if i == i.lower():
                result+=i.upper()
            else:
                result+=i.lower()
        return result  #equals breaking the loop

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)