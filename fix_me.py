"""
Модуль для вычисления среднего значения списка чисел.
"""


def calculate_average(nums):
    """
        Вычисляет среднее значение списка чисел.

        :param nums: Список чисел.
        :return: Среднее значение списка.
    """
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
