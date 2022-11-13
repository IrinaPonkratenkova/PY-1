from random import randint

def get_unique_list_numbers(start, stop, size) -> list[int]:
    unique_numbers = []
    while len(unique_numbers) < size:
        number = randint(start, stop)
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers



list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
