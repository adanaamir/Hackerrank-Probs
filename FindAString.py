def count_substring(string, sub_string):
    start = 0
    count = 0
    while True:
        start = string.find(sub_string, start)   #using the find function to find a certain string in a string
        if start == -1:   #since we're starting start from 0, if it equals -1 it means none is left
            break
        count+=1   # else incrementing count and start
        start+=1
        
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)