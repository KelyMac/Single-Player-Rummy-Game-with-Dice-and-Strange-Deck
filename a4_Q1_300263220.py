def number_divisible(lst,n):
    count = 0
    for i in range(len(lst)):
        if lst[i]%n == 0:
            count += 1
    return count

#main
raw_input = input("Please input a list of integers separated by spaces: ").strip().split()
lst = []
for i in range(len(raw_input)):
    lst.append(int(raw_input[i]))
n = int(input("Please input an integer: "))
print("The number of elements divisible by {} is {}".format(n,number_divisible(lst,n),))
