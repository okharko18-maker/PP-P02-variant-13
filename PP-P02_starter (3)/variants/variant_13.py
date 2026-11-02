def solve(balance_str: str, ops_str: str) -> str:
    """
    Застосовує операції до балансу. Зупиняється, якщо баланс стає від'ємним.
    Повертає фінальний стан рахунку, кількість операцій та факт зупинки.
    """
  # Перевірка початкового балансу
    if not balance_str.isdigit():
        return "Помилка: некоректний початковий баланс"

    balance = int(balance_str)

    operations = ops_str.split()
    count = 0
    stopped = "Ні"

    for op in operations:
        # Перевірка операції
        if op.startswith(("+", "-")):
            if len(op) == 1 or not op[1:].isdigit():
                return "Помилка: некоректна операція"
        else:
            if not op.isdigit():
                return "Помилка: некоректна операція"

        balance += int(op)
        count += 1

        if balance < 0:
            stopped = "Так"
            break

    return (
        f"Фінальний баланс: {balance}\n"
        f"Виконано операцій: {count}\n"
        f"Зупинка: {stopped}"
    )

if __name__ == "__main__":
    balance_input = input("Введіть початковий баланс: ")
    ops_input = input("Введіть операції: ")
    print(solve(balance_input, ops_input))
