def findmaxnum(n):
    max = 0
    for i in str(n):
        
        if int(i) > int(max):
            max = i
    return max


a = findmaxnum(3982374)
print (a)