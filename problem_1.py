#### #1. Write a program to print Twinkle twinkle little star poem in python.

# print('''Twinkle, twinkle, little star

# How I wonder what you are

# Up above the world so high

# Like a diamond in the sky

# Twinkle, twinkle little star

# How I wonder what you are

# When the blazing sun is gone

# When he nothing shines upon

# Then you show your little light

# Twinkle, twinkle, all the night

# Twinkle, twinkle, little star

# How I wonder what you are''')



###########2. Use REPL and print the table of 5 using it.

# 5*1 to 5*10

###########3. Install an external module and use it to perform an operation of you interest.


# import pyttsx3  # Importing pyttsx3 library

# # Initialize the pyttsx3 engine
# engine = pyttsx3.init()

# # Set properties (optional)
# engine.setProperty('rate', 150)    # Speed of speech
# engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

# # Text that you want to convert to speech
# text = "Hello, welcome to pyttsx3 text to speech program."

# # Pass the text to be spoken
# engine.say(text)

# # Process and run the speech engine
# engine.runAndWait()


###########4. Write a python program to print the contents of a directory using the os model .


import os

#Specify the directory you want to list.
directory_path='/'

#List all files and directories in the specified path.
contents =os.listdir(directory_path)

#Print each file and directory name.
for items in contents:
    print(items)

###########5. Label the program written in problem 4 with comments.