
#from turtle import Turtle, Screen
#timmy = Turtle()
#print(timmy)
#timmy.shape("turtle")
#timmy.color("coral")
#timmy.forward(150)
#Class attributes
#my_screen = Screen()
#print(my_screen.canvheight)
#Object methods
#my_screen.exitonclick()
#**************************************************************
from  prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon name", "Type"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmender","fire"])
print(table)