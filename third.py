# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

first_string = input("Введите первую строку:  ")
second_string = input("Введите первую строку:  ")
for i in range(len(first_string)):
    count = 0
    for j in range(len(second_string)):
        if first_string[i] == second_string[j]:
            count +=1
    print(f"{first_string[i]} - {count},\t", end="")