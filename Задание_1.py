numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
idx = numbers.index(None)
new_sum = sum(x for x in numbers if x is not None)
average = new_sum / len(numbers)
average = float(f"{average:.2f}")
numbers[idx] = average
print("Измененный список:", numbers)

