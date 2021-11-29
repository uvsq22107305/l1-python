a = [3, 5, 10]
print (a)

b = [12,17]


a.extend (b)

print (a)

a[2] = -7

print(a)



b = [i*2 for i in a]

print(b)

for i in range (len(b)):

    b[i]= b[i] +i

print (b)
