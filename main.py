n = str(input("Ввведите сроку: "))
r = len(n)
glass = "уеёыаоэяию" # Все гласные
sogl = "йцкнгшщзхфвпрлджчсмтб" # Все согласные
s = 0
g = 0
for i in n.lower(): #Приводим к нижнему регистру
    if i in glass: # Если есть гласная
        g+=1
    elif i in sogl: # Если есть согласная
        s+=1
print(s) #Выводим согласные
print(g) #Выводим гласные  
print(r) # Выволдим длинну строки
