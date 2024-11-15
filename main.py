n = str(input("Ввведите сроку: "))
r = len(n)
glass = "уеёыаоэяию"
sogl = "йцкнгшщзхфвпрлджчсмтб"
s = 0
g = 0
for i in n.lower():
    if i in glass:
        g+=1
    elif i in sogl:
        s+=1
print(s)
print(g)
print(r)