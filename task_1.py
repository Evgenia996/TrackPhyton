numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sum_of_numbers = sum(num for num in numbers if isinstance(num,(int, float)))
total_count = len(numbers)
average = sum_of_numbers / total_count
for i in range(total_count):
    if numbers [i]  is None:
       numbers[i] = average
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:",(numbers))