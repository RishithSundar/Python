l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd= []
for n in l:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print(even)
print(odd)
