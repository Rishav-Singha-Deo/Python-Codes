'''
Write a program that uses a dictionary that contains ten user names
and passwords. The program should ask the user to enter their
username and password. If the username is not in the dictionary,
the program should indicate that the person is not a valid user
of the system. If the username is in the dictionary, but the user
does not enter the right password, the program should say that the
password is invalid. If the password is correct, then the program
should tell the user that they are now logged in to the system.
'''
d={"Himani Saini":"W1k9<B)p","Shalabh Bhatnagar":"QfHw9=w5",
   "Gulzar Azad":"VCk^k33c","Javed Shaikh":"+7uB{MKi",
   "Anupam Basu":"6N1Rx*73","Veerachary":"\w-4sS'q",
   "Supratim Biswas":"VCk3L}/[","Anthony Tung":"up]IT7>8",
   "Vinod Sharma":"h6C`&7aL","Sumantra Roy":"{;>MK1rZ"}
u=input("Username : ")
if u in d:
    c=3
    while c>0:
        p=input("Password : ")
        if p==d[u]:
            print("Logged into system")
            break
        else:
            c-=1
            print("Wrong Password.",c,"attempt(s) left.")
else:
    print("Invalid Username.")