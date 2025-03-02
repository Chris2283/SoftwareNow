
################ QUESTION 2 - HIT137 Group Assessment 2 ###################################
 
from PIL import Image
import time

# Load the image - File path 'C:\\Users\\chris\\Downloads\\chapter1.jpg' will need to be changed depending on where the chapter1.jpg is stored for each user
image = Image.open('C:\\Users\\chris\\Downloads\\chapter1.jpg')
pixels = image.load()

# Get the time
current_time = int(time.time())

# Create a number using the  time
generated_number = (current_time % 100) + 50

# Check if the number is even
if generated_number % 2 == 0:
    generated_number += 10

# To cycle through across the image, changing the RGB values at each pixel.
for i in range(image.width):
    for j in range(image.height):
        # Get the original pixel values
        r, g, b = pixels[i, j]

        # Add the created number to the original values
        new_r = r + generated_number
        new_g = g + generated_number
        new_b = b + generated_number

        # Set the new pixel values for the new Chaper1out image
        pixels[i, j] = (new_r, new_g, new_b)

# Save the modified image - File path 'C:\\Users\\chris\\Downloads\\chapter1out.jpg' will need to be changed depending on where the output image is to be saved by users.
image.save('C:\\Users\\chris\\Downloads\\chapter1out.png')

# Calculate the sum of all red pixel values
red_sum = sum([pixels[i, j][0] for i in range(image.width) for j in range(image.height)])

# Output the sum
print("Sum of all red pixel values:", red_sum)





################ QUESTION 2 - HIT137 Group Assessment 2 ###################################


total = 0
for i in range(5):
    for j in range(3):
        if i + j ==5:
            total += i + j
        else:
            total -= i - j
            
counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2
        
# There was an error in the else statement of the nested for loop in the original code. 
# The operation should perform the subtraction of i + j instead of i - j. 
# Also the else line of the while loop, the number should be incremented by 1 rather than 2.       


# The fixed code is as follows

total = 0

for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i + j

counter = 0

while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 1

print(total)

# using the "Key = 13" the decript file base on the provided encription file is 

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                elif shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

encrypted_code = "tybony_inevnoyr = 100\nzl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}\n\nqrs cebprff_ahzoref():\n  tybony tybony_inevnoyr\n  ybpny_inevnoyr = 5\n  ahzoref = [1, 2, 3, 4, 5]\n\n  juvyr ybpny_inevnoyr > 0:\n    vs ybpny_inevnoyr % 2 == 0:\n      ahzoref.erzbir(ybpny_inevnoyr)\n    ybpny_inevnoyr -= 1\n\n  erghea ahzoref\n\nzl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}\nerfhyg = cebprff_ahzoref(ahzoref=zl_frg)\n\nqrs zbqvsl_qvpg():\n  ybpny_inevnoyr = 10\n  zl_qvpg['xrl4'] = ybpny_inevnoyr\n\nzbqvsl_qvpg(5)\n\nqrs hcqngr_tybony():\n  tybony tybony_inevnoyr\n  tybony_inevnoyr += 10\n\nsbe v va enatr(5):\n  cevag(v)\n  v += 1\n\nvs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:\n  cevag(\"Pbaqvgvba zrg!\")\n\nvs 5 abg va zl_qvpg:\n  cevag(\"5 abg sbhaq va gur qvpgvbanel!\")\n\ncevag(tybony_inevnoyr)\ncevag(zl_qvpg)\ncevag(zl_frg)"

key = 13
original_code = decrypt(encrypted_code, key)
print(original_code)

# the resulting print is 

# global_variable = 100
#my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

#def process_numbers():
#  global global_variable
#  local_variable = 5
#  numbers = [1, 2, 3, 4, 5]

#  while local_variable > 0:
#    if local_variable % 2 == 0:
#     numbers.remove(local_variable)
#    local_variable -= 1

#  return numbers

#my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
#result = process_numbers(numbers=my_set)

#def modify_dict():
#  local_variable = 10
#  my_dict['key4'] = local_variable

#modify_dict(5)

#def update_global():
#  global global_variable
#  global_variable += 10

#for i in range(5):
#  print(i)
#  i += 1

#if my_set is not None and my_dict['key4'] == 10:
#  print("Condition met!")

#if 5 not in my_dict:
#  print("5 not found in the dictionary!")

#print(global_variable)
#print(my_dict)
#print(my_set)

# HOWEVER THE PRINTED CODE ABOVE HAS ERRORS.

# Below is the code with errors repaired

global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Given that the input parameter "numbers" is already defined in the "process_numbers" function, 
# there is no necessity to specify "numbers=my_set" when utilising the function.

 Instead, transform the integers in the input set into an array.

def process_numbers(numbers):
  global global_variable
  local_variable = 5
  numbers = list(numbers)

  while local_variable > 0:
    if local_variable % 2 == 0:
      numbers.remove(local_variable)
    local_variable -= 1

  return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers(numbers=my_set)

def modify_dict():
  local_variable = 10
  my_dict['key4'] = local_variable

# In the modify_dict function call, the unnecessary argument 5 was removed since 
# the local variable is already defined inside the function.

modify_dict()

def update_global():
  global global_variable
  global_variable += 10

# Because the loop variable i is automatically incremented in each iteration, 
# the i += 1 statement inside the for loop has been removed.

for i in range(5):
  print(i)

if my_set is not None and 'key4' in my_dict and my_dict['key4'] == 10:
  print("Condition met!")

# In the if statement that checks for the presence of 5 in my_dict, 
# my_dict was changed to my_dict.values() to see if 5 is among the dictionary values.

if 5 not in my_dict.values():
  print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)

