#print an array of numbers that donot sum to 3

def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    #list comprehension: [expression ,loop ,if-condition(if any)]
    cuboid_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

    print(cuboid_list)

if __name__ == '__main__':
    main()
