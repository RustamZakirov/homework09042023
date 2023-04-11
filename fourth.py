# # Задайте список из N элементов, заполненных числами 
# # из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# # 3 -> [2, 3, -3, -2, -1, 0, 1]

# Имя массива.append

def input_array(arr, a):
    arr_length = a * 2 + 1
    a = -a
    for i in range(arr_length):
        arr.insert(i, a)
        a +=1
a = int (input ("Введите число:  "))
arr = []
input_array(arr, a)
print(f"Начальный массив: {arr}")
arr1 = arr[len(arr) - 2: len(arr)] + arr[0: len(arr) - 2]
print(f"Массив со сдвигом: {arr1}")

