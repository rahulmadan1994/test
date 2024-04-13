“commands” - people use to communicate with a computer!
We convey our commands to the computer by writing them in a text file using a programming language. These files are called programs.
Running a program means telling a computer to read the text file, translate it to the set of operations that it understands, and perform those actions.

script.py

my_name = "Rahul"
print("Hello and welcome " + my_name + "!")


Output:
Hello and welcome Rahul!

temp  =6
print("Hello and welcome " + temp + "!")

Output :

ERROR!
Traceback (most recent call last):
  File "<string>", line 6, in <module>
TypeError: can only concatenate str (not "int") to str

temp  =6
temp = str(temp)
my_name = "Rahul"
print("Hello and welcome " + temp + "!")

or 

temp  =2
print("Hello and welcome " + str(temp) + " !")

or

#old method
temp  =6
print("Hello and welcome %d !" %(temp))

or 

#new method
temp  =6
print("Hello and welcome {} !" .format(temp))

Output
Hello and welcome 6 !

temp  =[1,2,3]
print("Hello and welcome {} !" .format(temp))

temp  =(1,2,3)
print("Hello and welcome {} !" .format(temp))

temp={'rahul':[1,2,3],'kritika':10,'doggy':(1,2,3),'dash':"rahul",'dhinchak pooja':2}
print("welcome all {} !" .format(temp))

Output
Hello and welcome [1, 2, 3] !
Hello and welcome (1, 2, 3) !
welcome all {'rahul': [1, 2, 3], 'kritika': 10, 'doggy': (1, 2, 3), 'dash': 'rahul', 'dhinchak pooja': 2} !

temp1  =[1,2,3]
temp2=(1,2,3)
print("Hello and welcome {} ! {}" .format(temp1,temp2))

Output
Hello and welcome [1, 2, 3] ! (1, 2, 3)