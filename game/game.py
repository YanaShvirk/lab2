import random

def rock_paper_scissors():
    choices = ["камень", "ножницы", "бумага"]
    user_choice = input("Выберите (камень, ножницы, бумага): ").strip().lower()
    
    if user_choice not in choices:
        print("Некорректный выбор.")
        return
    
    computer_choice = random.choice(choices)
    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        print("Вы победили!")
    else:
        print("Вы проиграли!")

rock_paper_scissors()
