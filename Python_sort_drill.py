def mysort(alist):
    for pass_remaining in range(len(alist)-1,0,-1):
        for i in range(pass_remaining):
            if alist[i]>alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

alist = [67, 45, 2, 13, 1, 998]
mysort(alist)
print(alist)

alist = [89, 23, 33, 45, 10, 12, 45, 45, 45]
mysort(alist)
print(alist)

