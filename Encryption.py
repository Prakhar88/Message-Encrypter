import Abtash
import Alphanum
import Ceasar
import ROT_n
import Vigenere
while True:
    print("Welcome to text encrypter and decrypter")
    try:
     choice=int(input("1.Encrypt\n2.Decrypt\n3.exit\nenter choice:"))
    except ValueError:
        print("Enter numbers!!!")
        continue
    if choice==1:
        while True:
            text=input('enter the message below:\n')
            print("Enter the type of encryption you want?")
            print(f"1. Abtash (Flips around the alphabets)\n2. Alphanumeric (turns alphabets into number)\n3.Ceasar(not the salad) (shifts the alphabet ahead by 3)\n4. Rotation_n (Rotates the message by n characters)\n5.Vigenere (encrypt using a key)")
            while True:
                try:
                    choice_1=int(input('enter choice:'))
                    break
                except ValueError:
                    print("Enter numbers!!!")
            if choice_1==1:
                print(Abtash.enc(text))
                break
            elif choice_1==2:
                print(Alphanum.enc(text))
                break
            elif choice_1==3:
                print(Ceasar.enc(text))
                break
            elif choice_1==4:
                while True:
                    try:
                        n = int(input("Enter the number of rotation: "))
                        print(ROT_n.enc(text,n))
                        break
                    except ValueError:
                        print("Enter a valid number!")

            elif choice_1==5:
                completion=False
                while True:
                    key=input('enter key to hide:')
                    if not Vigenere.keyvalid(key):
                        print("enter key with only alphabets")
                    elif len(Vigenere.txt_only(text))<len(key):
                        print("please pick a larger key(remember special characters and numbers don't count)")
                    else:
                        print(Vigenere.enc(text,key))
                        completion=True
                        break
                if completion==True:
                    break
            else:
                print('Please enter correct choice')         
    elif choice==2:
        while True:
            text=input('enter the message below:\n')
            print("Enter the type of decryption you want?")
            print(f"1. Abtash (Flips around the alphabets)\n2. Alphanumeric (turns alphabets into number)\n3.Ceasar(not the salad) (shifts the alphabet ahead by 3)\n4. Rotation_n (Rotates the message by n characters)\n5.Vigenere (encrypt using a key)")
            choice_1=int(input('enter choice:'))
            if choice_1==1:
                print(Abtash.dec(text))
                break
            elif choice_1==2:
                print(Alphanum.dec(text))
                break
            elif choice_1==3:
                print(Ceasar.dec(text))
                break
            elif choice_1==4:
                while True:
                    try:
                        n = int(input("Enter the number of rotation: "))
                        print(ROT_n.dec(text,n))
                        break
                    except ValueError:
                        print("Enter a valid number!")

            elif choice_1==5:
                completion=False
                while True:
                    key=input('enter key to uncover:')
                    if not Vigenere.keyvalid(key):
                        print("enter key with only alphabets")
                    elif len(Vigenere.txt_only(text))<len(key):
                        print("please pick a larger key(remember special characters and numbers don't count)")
                    else:
                        print(Vigenere.dec(text,key))
                        completion=True
                        break
                if completion==True:
                    break
            else:
                print('Please enter correct choice')
    elif choice==3:
        break
    else:
        print("Please enter correct choice")
        