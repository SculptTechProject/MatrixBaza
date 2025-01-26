print("Podaj kazde przeksztalcenie w formacie x;y")
a = list(input("Podaj 1 przeksztalcenie: ").split(";"))
a = [float(i) for i in a]
b = list(input("Podaj 2 przeksztalcenie: ").split(";"))
b = [float(i) for i in b]
c = list(input("Podaj 3 przeksztalcenie: ").split(";"))
c = [float(i) for i in c]
d = list(input("Podaj 4 przeksztalcenie: ").split(";"))
d = [float(i) for i in d]
x = 0
if b[0] > a[0]:

    while b[0] > a[0]:
        b[0] -= 1
        x += 1
    b[0] = x
elif b[0] < a[0]:
    
    while b[0] < a[0]:
        b[0] += 1
        x -= 1
    b[0] = x
elif b[0] == a[0]:
    b[0] = 0
x = 0
if c[0] > a[0]:
    
    while c[0] > a[0]:
        c[0] -= 1
        x += 1
    c[0] = x
elif c[0] < a[0]:
    
    while c[0] < a[0]:
        c[0] += 1
        x -= 1
    c[0] = x
elif c[0] == a[0]:
    c[0] = 0
###
x = 0
if b[1] > a[1]:
    
    while b[1] > a[1]:
        b[1] -= 1
        x += 1
    b[1] = x
elif b[1] < a[1]:
    
    while b[1] < a[1]:
        b[1] += 1
        x -= 1
    b[1] = x
elif b[1] == a[1]:
    b[1] = 0
x = 0
if c[1] > a[1]:
    
    while c[1] > a[1]:
        c[1] -= 1
        x += 1
    c[1] = x
elif c[1] < a[1]:
    
    while c[1] < a[1]:
        c[1] += 1
        x -= 1
    c[1] = x
elif c[1] == a[1]:
    c[1] = 0
print("Przeksztalcenia: ")
print(f"{c[0]} {b[0]} {a[0]}\n {c[1]} {b[1]} {a[1]}\n 0 0 1")