n=int(input("Enter the number of elements:"))
l=[]
for i in range(n):
    l.append(int(input("Enter the element:")))
print("The list is:",l)
print(l.index(max(l)))
print(l.index(min(l)))
