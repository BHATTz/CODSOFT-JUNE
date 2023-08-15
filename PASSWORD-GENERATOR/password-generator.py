import random
import string

# Prompt the user to specify the desired length of the password
password_length = int(input("Enter the desired password length: "))

# Define character sets for different complexity levels
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

# Combine character sets based on user preferences
valid_characters = lowercase_letters + uppercase_letters + digits + special_characters

# Generate the password using random characters
generated_password = ''.join(random.choice(valid_characters) for _ in range(password_length))

# Display the generated password
print("Generated Password:", generated_password)
