import random


def repeat_with_remaining_attempts():

    total_attempts = 6
    balance = 100  # Initialize balance outside the loop

    for i in range(total_attempts):
        remaining_attempts = total_attempts - (i + 1)

        print(f"Ваш текущий баланс: {balance} единиц")
        bet = int(input("Введите вашу ставку: "))

        # Check if the bet is greater than the balance

        if bet > balance:
            print("Недостаточно средств на балансе!")
            continue  # Skip this iteration if the bet is invalid

        number = random.randint(1, 100)  # Change the range to 1-100
        guess_number = int(input('Угадайте число от 1 до 100: '))

        if guess_number >= 100:
            print("Введите коректное число")
            continue

        if guess_number == number:
            total_winnings = bet * 2
            balance += total_winnings - bet
            print(f"Вы выиграли: {total_winnings} единиц. Ваш новый баланс: {balance} единиц.")
        else:
            balance -= bet  # Deduct the bet from the balance if the guess is incorrect
            print(f"Неправильно. Вы потеряли {bet} единиц. Осталось попыток: {remaining_attempts}.")

        # Check if balance is depleted

        if balance <= 0:
            print("Вы проиграли все свои деньги!")
            break

    print("Игра окончена. Ваш финальный баланс: ", balance)
# Call the function to start the game

repeat_with_remaining_attempts()
