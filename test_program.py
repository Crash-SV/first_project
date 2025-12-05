def find_max_even_number(a):
    current_max = 1
    for b in a:
        if b % 2 == 0:
            current_max = max(b, current_max)
    return current_max


max_even = find_max_even_number([1, 2, 3, 4, 5])
# Попробуйте передать в find_max_even_number() другие списки:
# max_even = find_max_even_number([10, 8, 6, 4, 2])
# [10, 8, 6, 4, 2]
# [2, 12, 85, 0, 6]
print(f"Максимальное чётное число: {max_even}")

"""
Ищет максимальное чётное значение в списке положительных
целых значений, переданном в параметр функции.
"""
