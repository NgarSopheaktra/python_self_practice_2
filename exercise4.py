def sum_n (a):
    sum = 0
    for i in a:
        for j in i:
            sum += j
    return sum
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print (sum_n(a))