import turtle

# memindahkan turtle tanpa menggambar ke lokasi awal
turtle.penup()
turtle.goto(-160,110)
# turtle.bgcolor("lightgreen")

# mengubah warna menjadi kuning
turtle.pendown()
turtle.color('yellow')
turtle.begin_fill()

# membuat huruf U
turtle.forward(40)
turtle.right(90)
turtle.forward(140)
turtle.left(45)
turtle.forward(40)
turtle.left(45)
turtle.forward(20)
turtle.left(45)
turtle.forward(40)
turtle.left(45)
turtle.forward(140)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(170)
turtle.right(45)
turtle.forward(40)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(40)
turtle.right(45)
turtle.forward(170)
turtle.end_fill()

# memindahkan turtle tanpa menggambar
turtle.penup()
turtle.right(90)
turtle.forward(180)

# mulai menggambar
turtle.pendown()
turtle.color('black')
turtle.begin_fill()

# todo: lengkapi kode untuk membuat huruf I seperti pada contoh di atas
turtle.forward(40)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

turtle.end_fill()
turtle.hideturtle() # menyembunyikan ikon turtlenya
turtle.exitonclick()
