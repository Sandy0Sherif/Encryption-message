with open("Alphabets.txt") as file1:
    letters=file1.read()
with open("original-msg.txt") as file2:
    message=file2.read()
file3=open("Cypher.txt","w")

def encrypt( plaintext, key):
    ciphertext= ''
    for letter in plaintext:
        if letter.lower()in letters:
                index = letters.find(letter.lower())
                if index == -1:
                    ciphertext += letter
                else:
                    if letter.islower():
                       new_index = index + key
                       if new_index >= 26:
                          new_index -= 26
                       ciphertext += letters[new_index].lower()
                    elif letter.isupper():
                        new_index = index + key
                        if new_index >= 26:
                            new_index -= 26
                        ciphertext += letters[new_index].upper()
        else:
            ciphertext += letter

    return ciphertext




print(f"The text you need to have encryption is {message}")

ciphertext=encrypt(message,3)
print("Substitution Technique ")
print(f'chipertext: {ciphertext}')

result=file3.write(ciphertext)



def encrypt2(plaintext):
    ciphertext2=''
    ciphertext3=''
    plaintext2=plaintext.replace(' ','')
    for index in range(0, len(plaintext2)):
       if index%2==0:
         new_index =index
         ciphertext2 += plaintext2[new_index ]

    for index1 in range(0, len(plaintext2)):
        if index1 % 2 != 0:
            ciphertext2 += plaintext2[index1]
    ciphertext3=ciphertext2.replace('\n','')
    return ciphertext3




ciphertext2=encrypt2(ciphertext)
print("Transposition Technique ")
print(f'ciphertext2: {ciphertext2}')
result2=file3.write(ciphertext2)

