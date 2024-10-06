#unlike lists, tuples cannot be modified
def main():
    n = int(input())
    integer_list = list(map(int, input().split()))  #integers enetred

    #using slicing here, we will be first converting the iterator coming from map to list(to slice) then slice till n
    t = tuple(integer_list[:n])    #converting the iterable to tuple
    print(hash(t))
        

if __name__ == "__main__":
    main()