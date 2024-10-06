def main():
    N= int(input())   #number of commands
    lst = []

    for _ in range(N):
        command = input().split()  #taking 3 inputs, i-e commnd name, and values

        if command[0] == "insert":
            pos,val = int(command[1]), int(command[2])   #at 0th term is command name "insert" at 1 nd 2 is values and pos
            lst.insert(pos,val)
        elif command[0] == "append":
            val = int(command[1])
            lst.append(val)
        elif command[0] == "remove":
            val = int(command[1])
            lst.remove(val)
        elif command[0] == "sort":
            lst.sort()
        elif command[0] == "pop":
            lst.pop()
        elif command[0] == "reverse":
            lst.reverse()
        elif command[0] == "print":
            print(lst)
        
if __name__ == "__main__":
    main() #test