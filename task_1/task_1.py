def caching_fibonacci():
    # Створення порожнього словника для зберігання результатів обчислень
    cache = {}

    # Внутрішня функція fibonacci для обчислення чисел Фібоначчі та кешування результатів
    def fibonacci(n: int) -> int:
        # Перевірка базових випадків
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Перевірка, чи вже є результат у кеші
        if n in cache:
            return cache[n]
        
        # Обчислення числа Фібоначчі за допомогою рекурсії
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        # Повернення обчисленого значення та збереження його в кеші
        return cache[n]

    # Повернення внутрішньої функції fibonacci
    return fibonacci

# Приклад використання:
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610