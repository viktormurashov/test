def bubble(a): 
    if len(a) <= 1 :
        return a 
    for _ in range(len(a) - 1):
        for i in range(len(a) - 1):
            if a[i] > a[i+1]: 
                a[i+1], a[i] = a[i], a[i+1]   
    return a 
ann = [1,9,8,2,6,2,3,6,5,4,8,10]
print(bubble(ann))






