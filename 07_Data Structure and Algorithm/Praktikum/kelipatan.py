def group_numbers(numbers, target):
    result = [[], []]
    for num in numbers:
        if num % target == 0:
            result[0].append(num)
        else:
            result[1].append(num)
    return result

print(group_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(group_numbers([23, 15, 19, 20, 75, 30, 45], 5))