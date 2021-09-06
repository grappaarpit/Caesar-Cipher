import art


def caesar (text,shift,alphabet,direction):

  
  if direction == "encode":
    word = encrypt(text=text,shift=shift,alphabet=alphabet)

  else:
    word =decrypt(text=text,shift=shift,alphabet=alphabet)

  return(word)

def play_again():
  choice_f = input("Wanna play again ")

  if choice_f == 'y':
    return(True)
  
  if choice_f == 'n':
    print("Goodbye")
    return(False)
  else:
    print("Are you stupid or what, try again")
    play_again()
  


def encrypt(text,shift,alphabet):
  word = ""
  shift_f = (shift%26)
  for letter in text:
    for i,num in enumerate(alphabet):
      if num ==letter:
        if i>=21:
          letter = alphabet[i-(26-shift_f)]
        else:
          letter = alphabet[i+shift_f]
        word = word + letter
        break
  
  return(word)

def decrypt(text,shift,alphabet):
  word = ""
  shift_f = (shift%26)
  for letter in text:
    for i,num in enumerate(alphabet):
      if num ==letter:
        if i<=4:
          letter = alphabet[-(shift_f-i)]
        else:
          letter = alphabet[i-shift_f]
        word = word + letter
        break

  return(word)
  
  
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

choice = True

while(choice):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  word = caesar (text,shift,alphabet,direction)
  print(f"the code is {word} ")
  choice = play_again()
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 