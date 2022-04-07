import re
import Admin
import User

class Bms:


    def main(self):

        while True:

            print("*****************Welcome To Book My Show Application****************************")
            print("1:Login")
            print("2:Register new account")
            print("3:Exit")
            flag = 0
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter user name: ")
                password = input("enter the password: ")
                for line in open("userinput1.txt", "r").readlines():
                    login_info = line.split()
                    if name == login_info[0] and password == login_info[1]:
                        print("correct credentials!")
                        val=str(input("Do You Want to Continue or Quit?: "))
                        if val== "continue":
                            User.user()
                        elif val== "quit":
                            quit()
                        else:
                            print("Enter the correct username and password")
                            print("Seems like you are a new ! Do Register")
                            continue


                if name == "admin" and password == "admin":
                    Admin.admin()


            if choice == 2:
                print("*****************Create new Account******************")
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                age = input("enter the age: ")
                password = input("Create a password: ")
                flag =0
                while True:
                    if(len(password)<8):
                        flag=-1
                        break
                    elif not re.search("[a-z]",password):
                        flag = -1
                        break
                    elif not re.search("[A-Z]",password):
                        flag = -1
                        break
                    elif not re.search("[0-9]", password):
                        flag = -1
                        break
                    elif not re.search("[_@$]", password):
                        flag = -1
                        break
                    else:
                        flag = 0
                        print("Kudos!You have entered a valid password")
                        print("***Account created***")  # User Registration
                        break

                if flag == -1:
                    print("Please create a Valid Password with-\n1.Miniumum 8 characters\n"
                          "2.Atleast one upper case and lower case\n3.Atleast one number\n"
                          "4.Atleast one special character from [_or@or$]")
                    continue

                else:
                    file = open("userinput1.txt", "a")
                    file.write(name)
                    file.write(" ")
                    file.write(password)
                    file.write(" ")

            if choice==3:
                exit()

obj1=Bms()
obj1.main()