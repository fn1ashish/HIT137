#------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# Question 3 /  1. Fixing the next code will reveal the key.  

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            shifted = ord(char) - key  # Reverse the encryption by subtracting the key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26  # Wrap around to the beginning of the lowercase alphabet
                elif shifted < ord('a'):
                    shifted += 26  # Wrap around to the end of the lowercase alphabet
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26  # Wrap around to the beginning of the uppercase alphabet
                elif shifted < ord('A'):
                    shifted += 26  # Wrap around to the end of the uppercase alphabet
            decrypted_text += chr(shifted)  # Append the decrypted character to the result
        else:
            decrypted_text += char  # Append non-alphabetic characters as they are
    return decrypted_text

# Original code
original_code = "Hello, World!"

# Brute-force to find the key value
for possible_key in range(26):  # Try all possible key values
    decrypted_text = decrypt(original_code, possible_key)  # Decrypt using the current key
    print(f"Key: {possible_key}, Decrypted Text: {decrypted_text}")  # Print the results



#------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# Question 3 / 2. Write the decryption function to decrypt the ‘encrypted code’ to the original code.  

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Example usage
encrypted_code = "Gbol, Jbeyq!"
key = 13
decrypted_code = decrypt(encrypted_code, key)
print(decrypted_code)

#------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# Question 3 / 3. Correct the errors and provide the comments.

tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xr12': 'inyhr2', 'xrl3': 'inyhr3'}

# Define a function to generate a list of even numbers
def cebprff_ahzoref():
    global tybony_inevnoyr  # Use the global variable tybony_inevnoyr
    ybpny_inevnouyr = 5
    ahzoref = []

    # Use a while loop to generate even numbers and add them to ahzoref list
    while ybpny_inevnouyr > 0:
        if ybpny_inevnouyr % 2 == 0:
            ahzoref.append(ybpny_inevnouyr)
        ybpny_inevnouyr -= 1

    return ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref()

# Define a function to update the dictionary zl_qvpg
def zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl4'] = ybpny_inevnoyr

# Call the function zbqvsl_qvpg with an argument of 5
zbqvsl_qvpg(5)

# Define a function to update the variable tybony_inevnoyr
def hcqngr_tybony():
    global tybony_inevnoyr  # Use the global variable tybony_inevnoyr
    tybony_inevnoyr += 10

# Use a for loop to print numbers from 1 to 5
for v in range(1, 6):
    print(v)

# Check conditions and print messages accordingly
if zl_frg == set() and zl_qvpg['xrl4'] == 10:
    print('Congratulations!')

if 5 not in zl_frg:
    print('5 not found in the set!')

# Print the values of tybony_inevnoyr, zl_qvpg, and zl_frg
print(tybony_inevnoyr)
print(zl_qvpg)
print(zl_frg)