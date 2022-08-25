def even():
    start = int(input("Enter start limit of integers: "))
    n = int(input("Enter limit of integers to print: "))
    tmp_lis = []
    for i in range(0, n):
        if i == 0:
            if start%2 != 0:
                start+=1
        tmp_lis.append(start)
        start += 2
    return(tmp_lis)
            
print(even())