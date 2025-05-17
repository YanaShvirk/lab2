from datetime import datetime

def calculate_age():
    birth_date = input("Введите дату рождения (дд/мм/гггг): ")
    try:
        birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        print(f"Ваш возраст: {age} лет")
    except ValueError:
        print("Некорректный формат даты. Попробуйте еще раз.")

calculate_age()
