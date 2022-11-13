def two_length_run(lst):
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return True
    return False

#main
raw_input = input("Please input a list of numbers separated by space: ").strip().split()
lst = []
for a in raw_input:
    lst.append(float(a))
print(two_length_run(lst))
