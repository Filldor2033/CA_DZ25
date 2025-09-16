def calculate_average(numbers):
    """
    Вычисляет среднее арифметическое значение списка чисел.
    
    Аргументы:
        numbers: список чисел (целых или дробных)
    
    Возвращает:
        Среднее значение или None, если список пуст или содержит нечисловые элементы
    """
    # Проверка, что передан список
    if not isinstance(numbers, list):
        print("Ошибка: ожидается список чисел")
        return None
    
    # Проверка на пустой список
    if len(numbers) == 0:
        return None
    
    # Проверка, что все элементы являются числами
    for num in numbers:
        if not isinstance(num, (int, float)):
            print(f"Ошибка: элемент {num} не является числом")
            return None
    
    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError as e:
        print(f"Ошибка при вычислении: {e}")
        return None


def calculate_average_simple(numbers):
    """
    Упрощенная версия функции для вычисления среднего значения.
    Возвращает 0 для пустого списка вместо None.
    """
    if not numbers or not isinstance(numbers, list):
        return 0.0
    
    try:
        return sum(numbers) / len(numbers)
    except (TypeError, ZeroDivisionError):
        return 0.0


def demonstrate_function():
    """Демонстрация работы функции с различными сценариями"""
    test_cases = [
        [10, 20, 30, 40],      # Нормальный случай
        [],                    # Пустой список
        [5],                   # Один элемент
        [1.5, 2.5, 3.5],      # Дробные числа
        [10, '20', 30],       # Смешанные типы
        [0, 0, 0],            # Нули
        "not a list"          # Не список
    ]
    
    print("Демонстрация работы функции calculate_average:")
    print("=" * 50)
    
    for i, test_data in enumerate(test_cases, 1):
        print(f"Тест {i}: {test_data}")
        result = calculate_average(test_data)
        
        if result is not None:
            print(f"✓ Среднее значение: {result:.2f}")
        else:
            print("✗ Невозможно вычислить среднее")
        print("-" * 30)


# Пример использования из оригинального кода
if __name__ == "__main__":
    # Оригинальный пример
    numbers_list = [10, 20, 30, 40]
    result = calculate_average(numbers_list)
    
    print("Оригинальный пример:")
    if result is not None:
        print(f"Среднее значение: {result}")
    else:
        print("Список пуст")
    
    print("\n")
    
    # Демонстрация различных сценариев
    demonstrate_function()
    
    print("\nУпрощенная версия:")
    simple_result = calculate_average_simple([10, 20, 30, 40])
    print(f"Среднее (упрощенная версия): {simple_result}")