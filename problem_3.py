#########1. Write a python program to display a user entered name followed by good Afternoon using input() function.
user=input("Enter your name please : ")
# print("Good Afternoon"+user)
print(f"Good Afternoon {user} ")

#########2. Write a program to fill in a letter template given below with name and date.

letter='''
Dear <|Name|>,
You are selected!
<|Date|>
'''


print(letter.replace("<|Name|>","Gajab").replace("<|Date|>","24-10-2024"))
#########3. Write a program to detect double space in a string.
j="hello ,  how are you , i am fine!"
print(j.find("  "))
#########4. Replace the double space from problem 3 with single spaces.

print(j.replace("  "," "))
#########5. Write a program to format the following letter using escape sequence characters.
Letter="Dear Gaku,\n this is python course is nice .\n \t\"Thanks\"!"
print(Letter)

