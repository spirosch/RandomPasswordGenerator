# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to a Simple Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letters = random.sample(letters, nr_letters)
random_letter_string = str(random_letters)
final_letters = random_letter_string.replace(' ', '')\
    .replace('[]', '')\
    .replace(',', '')\
    .replace("'", '')\
    .strip('[]')

random_numbers = random.sample(numbers, nr_numbers)
random_number_string = str(random_numbers)
final_number = random_number_string.replace(' ', '')\
    .replace('[]', '')\
    .replace(',', '')\
    .replace("'", '')\
    .strip('[]')

random_symbol = random.sample(symbols, nr_symbols)
random_symbol_string = str(random_symbol)
final_symbol = random_symbol_string.replace(' ', '')\
    .replace('[]', '')\
    .replace(',', '')\
    .replace("'", '')\
    .strip('[]')

combined_password = final_letters, final_number, final_symbol
final_password_string = str(combined_password)
final_password = final_password_string.replace(' ', '')\
    .replace('[]', '')\
    .replace(',', '')\
    .replace("'", '')\
    .strip('[]')\
    .strip('()')
combined_list_password = list(combined_password)

shuffled_password = ''.join(random.sample(final_password, len(final_password)))

print(f"Your password is: {shuffled_password}")