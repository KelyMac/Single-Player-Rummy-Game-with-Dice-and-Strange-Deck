def longest_run(lst):
    if len(lst) == 0:
        return 0
    longest = 1
    for i in range(len(lst)-1):
        length = 1
        flag = True
        j = i + 1
        
        while (flag and j<=len(lst)-1):
            if lst[i] == lst[j]:
                length += 1
                j += 1
            else:
                flag = False
        if length > longest:
            longest = length 
    return longest
        
#main
raw_input = input("Please input a list of numbers separated by space: ").strip().split()
lst = []
for a in raw_input:
    lst.append(float(a))
print(longest_run(lst))

