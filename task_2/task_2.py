import re
from typing import Callable

def generator_numbers(text: str):
    # Регулярний вираз для пошуку дійсних чисел у тексті
    pattern = r'\b\d+\.\d+\b'
    
    # Пошук у тексті за допомогою регулярного виразу
    for match in re.finditer(pattern, text):
        # Повертаємо знайдене число
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    # Викликаємо генератор для отримання дійсних чисел
    numbers = func(text)
    # Підсумовуємо числа
    total = sum(numbers)
    return total

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
