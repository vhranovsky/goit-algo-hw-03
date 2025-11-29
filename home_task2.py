import turtle


def koch_curve(t: turtle.Turtle, deep: int, size: int):
    if deep == 0:
        # Базовий випадок: малюємо пряму лінію
        t.forward(size)
    else:
        # Зменшуємо розмір відрізка в 3 рази для наступного рівня
        size /= 3

        # Рекурсивний крок:
        koch_curve(t, deep - 1, size)   # 1. Йдемо вперед
        t.left(60)                       # 2. Повертаємо вліво
        koch_curve(t, deep - 1, size)   # 3. Малюємо "виступ"
        t.right(120)                     # 4. Повертаємо вправо
        koch_curve(t, deep - 1, size)   # 5. Малюємо спуск з "виступу"
        t.left(60)                       # 6. Вирівнюємось
        koch_curve(t, deep - 1, size)   # 7. Йдемо вперед до кінця


def draw_snowflake(t, deep, size):
    for _ in range(3):
        koch_curve(t, deep, size)
        t.right(120)  # Поворот для формування трикутника


def main():
    # Отримуємо рівень рекурсії від користувача
    try:
        level = int(input("Введіть рівень рекурсії (рекомендовано 0-5): "))
    except ValueError:
        print("Не вірний ввід рівня рекурсії!!!")
        return

    figure_size: int = 300

    # Налаштування екрану
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    t.goto(- int(figure_size*0.5), int(figure_size*0.5))
    t.pendown()
    t.color("blue")

    print(f"Малюємо сніжинку рівня {level}...")
    draw_snowflake(t, level, figure_size)
    print("Клікніть на вікно з малюнком, щоб закрити його.")
    window.exitonclick()


if __name__ == "__main__":
    main()
