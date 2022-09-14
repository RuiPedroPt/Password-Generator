import string
import random

def generate_password():
	characters = list(string.ascii_letters + string.digits + "!?@#$%^&*")  # All the Charchters to choose
	length = 8	# Set the length of the Password you Want
	password = []

	for i in range(length):
		password.append(random.choice(characters))
	random.shuffle(characters)
	print("".join(password))

generate_password()