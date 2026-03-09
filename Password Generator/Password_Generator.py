import random
import string



def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation

    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password



print("Welcome to the Random Password Generator!\n")


try:
    length = int(input("Enter the desired password length: "))

    if length < 4:
        print(" Password should be at least 4 characters long for better security.")
    else:
        generated_password = generate_password(length)
        print("\nYour generated password is:")
        print(generated_password)
        

except ValueError:
    print(" Please enter a valid number.")
