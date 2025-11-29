

def hanoi(n: int, bar_a: str, bar_b: str, bar_c: str, bars: dict):
    if n == 1:
        # Базовий випадок: якщо блок один, просто переміщуємо його на фінальний бар
        print(f"    Переміщуєм блок 1: {bar_a} -> {bar_c}")
        bars[bar_c].append(bars[bar_a].pop(-1))

        if len(bars["bar_A"]) == 0 and len(bars["bar_B"]) == 0:
            print("-"*60)
            print(f"!!!Кінцевий стан: А:{bars["bar_A"]} В:{bars["bar_B"]} С:{bars["bar_C"]}")
        else:
            print(f"      Проміжний стан: А:{bars["bar_A"]} В:{bars["bar_B"]} С:{bars["bar_C"]}")
        return

    # Крок 1: Перемістити n-1 блоків з початкового на середній
    hanoi(n - 1, bar_a, bar_c, bar_b, bars)

    # Крок 2: Перемістити найбільший блок (n) з початкового на фінальний
    print(f"    Переміщуємо блок {n}: {bar_a} -> {bar_c}")
    bars[bar_c].append(bars[bar_a].pop(-1))
    print(f"      Проміжний стан: А:{bars["bar_A"]} В:{bars["bar_B"]} С:{bars["bar_C"]}")

    # Крок 3: Перемістити n-1 блоків з середнього на фінальний
    hanoi(n - 1, bar_b, bar_a, bar_c, bars)


def main():
    print("\n!--- Ханойські башти ---!")
    try:
        n = int(input("Введіть кількість блоків: "))
        if n < 1:
            print("Кількість блоків має бути більше 0.")
            return
    except ValueError:
        print("Не вірний ввід! Введіть ціле число.")
        return

    bars: dict = {"bar_A": [n-i for i in range(0, n)], "bar_B": [], "bar_C": []}
    print(f"!!!Початковий стан: А:{bars["bar_A"]} В:{bars["bar_B"]} С:{bars["bar_C"]}")
    print("-"*60)
    hanoi(n, 'bar_A', 'bar_B', 'bar_C', bars)
    print(f"    Загальна кількість кроків: {2**n - 1}")
    print("-"*60)


if __name__ == "__main__":
    main()
