a = [1000,7,4,15,6,-4,-1000]
k = len(a)-1
i= 0
while True:
    i=0
    t=0
    while i < k:
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
            print(a)
        elif a[i] < a[i+1]:
            t+=1
            if t == k:
                exit(0)
        i+=1

