import turtle

def draw_star(t, side_length):
    angle = 144  # 每个三角形的内角大小
    for _ in range(5):
        t.forward(side_length)
        t.right(angle)

def main():
    window = turtle.Screen()
    window.bgcolor("white")

    my_turtle = turtle.Turtle()
    my_turtle.speed(2)  # 可以调整turtle的绘制速度

    side_length = 100
    draw_star(my_turtle, side_length)

    window.mainloop()

if __name__ == "__main__":
    main()