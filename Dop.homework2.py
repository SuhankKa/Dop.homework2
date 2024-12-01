# "Слишком древний шифр"

a = int(input('Введи число от 3 до 20: '))
password = []

for i in range (1, 20):
    big = True
    for j in range (1, 20):
        if a > 20:
            big = False
            break
        k = j + 1
        if i == k:
            continue
      
        if a % (i+k) == 0 and i < k < 20:
            password.append(i)
            password.append(k)
           
if big:
    print(*password)
    
else:
    print("Ошибка! Введи число от 3 до 20!")

