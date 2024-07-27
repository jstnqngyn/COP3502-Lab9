"""
Justin Nguyen
[COP3502C] - Lab 9, functions.py

Objective: Create encode and decode functions.
"""

def encode(password):
    encoded_pass = [str((int(char) + 3) % 10) for char in password]
    return "".join(encoded_pass)

# PARTNER WILL COMPLETE DECODE
def decode(password):
    decoded_pass = ''
    for char in password:
        if char.isdigit():
            new_digit = (int(char) - 3) % 10
            decoded_pass += str(new_digit)
        else:
            decoded_pass += char
    return decoded_pass