
import turtle
import math

# Функція рекурсивного малювання дерева Піфагора
def pifagor_tree(t, length, level):
    if level == 0:
        return

    # Малюємо стовбур дерева
    t.forward(length)

    # Зберігаємо поточну позицію та напрямок
    position = t.position()
    direction = t.heading()

    # Малюємо ліву гілку
    t.left(45)
    pifagor_tree(t, length * math.sqrt(2) / 2, level - 1)

    # Повертаємося до початкової позиції
    t.penup()
    t.goto(position)
    t.setheading(direction)
    t.pendown()

    # Малюємо праву гілку
    t.right(45)
    pifagor_tree(t, length * math.sqrt(2) / 2, level - 1)

    # Повертаємося назад
    t.penup()
    t.goto(position)
    t.setheading(direction)
    t.pendown()


# Отримання рівня рекурсії від користувача
level = int(input("Введіть рівень рекурсії (1-12): "))

if level < 1 or level > 12:
    print("Помилка! Введіть число від 1 до 12.")
else:
    # Налаштування графічного вікна
    screen = turtle.Screen()
    screen.setup(width=1000, height=800)
    screen.bgcolor("white")
    screen.title("Фрактал — Дерево Піфагора")

    # Створення об'єкта черепашки
    t = turtle.Turtle()
    t.speed(0)
    t.color("darkgreen")
    t.pensize(2)

    # Початкова позиція
    t.penup()
    t.goto(0, -300)
    t.setheading(90)
    t.pendown()

    # Запуск рекурсії
    pifagor_tree(t, 150, level)

    # Приховуємо черепашку
    t.hideturtle()

    # Завершення програми
    screen.exitonclick()
