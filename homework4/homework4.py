import random

def find_multiples():
    try:
        x = int(input("Введите число X: "))
        numbers = [random.randint(0, 200) for _ in range(10)]
        multiples = list(filter(lambda num: num % x == 0, numbers))

        print("Сгенерированные числа:", numbers)
        print(f"Числа, кратные {x}:", multiples)
    except ValueError:
        print("Введите корректное число.")

find_multiples()
