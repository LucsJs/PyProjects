# Bubble Sort

l = [7, 4, 3, 12, 8]
print(l)

x = len(l) - 1
y = 0
while (x > y):
    while (y < x):
        if (l[y] > l[y + 1]):
            aux = l[y]
            l[y] = l[y + 1]
            l[y + 1] = aux
        
        y += 1
    
    y = 0
    x -= 1

print(l)
