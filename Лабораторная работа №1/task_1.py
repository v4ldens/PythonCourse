numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

summa = 0
for i in range(len(numbers)):
    if numbers[i] != None:
        summa += numbers[i]

average = summa / len(numbers)

for i in range(len(numbers)):
    if numbers[i] == None:
        numbers[i] = average
        break

print("Измененный список:", numbers)
