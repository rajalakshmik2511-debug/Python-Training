print("welcome to our ATM!!")

pas=int(input("enter the password:"))
while True:
    if(pas==2005):
        print("you entered correct password")
        print("now choose withdraw or deposit")
        break
    else:
        print("you enter the wrong password!!")
        pas=int(input("enter the valid password:"))
        break
