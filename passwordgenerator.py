import secrets
import string
import time

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
white_space = string.whitespace

alphabet = letters+digits+special_chars+white_space

#fixed password length
pwd_length = int(input("Enter the length of your desired password: "))

#password generate
pwd = ''
for i in range(pwd_length):
    pwd+=''.join(secrets.choice(alphabet))
print(pwd)
time.sleep(10)
print("This is your password")