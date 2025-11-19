#Introduction in python
'''
This is all about the Intro of python 
'''
'''
import random as rand
def Name():
    a=input("Enter your name:")
    return a
def opengift():
    gender =print(input("Enter your gender for male M and for Female F"))
    gender.upper()
    if gender == 'F':
        print("there is a doll for you")
    else:
        print("there is a RC car for you")
        
def Exit():
    exit()
choice=print(input(f"Welcom {Name()}! there is some gift for you to see your gift press 1 and 2 for Exit:"))
if choice == '1':
    opengift()
elif choice == '2':
    Exit()
else:
    print("Entered wrong choise")
    Name()
    
'''

user_data = {}
logged_user = []
logged = False
registration =False
current_user =None
def register():
    global registration , logged
    if not logged:
        Uname = input("Enter your name:-")
        E_mail = input("Enter your Email Id:-")
        Phone_no = input("Enter your phone_no:-")
        Password = input("Create a strong password: ")
        
        registration = True

        user_data[Uname] = {
            "password": Password,
            "email": E_mail,
            "phone": Phone_no
        }
        logged_user.append(Uname)
        current_user = Uname
        


        
        print("Succesfull Registered",logged_user)
        Ask = input("Wnat to go back to main menu? (yes/no)")
        if Ask.lower() != 'yes':
            terminate()
        else:
            main()
    else:
        if registration:
            print("Succesfull Registered")
        else:
            register()
            
def login():
    global registration, current_user

    if registration:
        userName = input("Enter your UserName: ")
        Password = input("Enter your Password: ")
    

    if userName in user_data and user_data[userName]["password"] == Password:
        current_user = userName
        print("Login successful.")
        while True:
            choice = input("Do you want to add another user? (yes/no): ")
            if choice.lower() != 'yes':
                break
                
            Uname = input("Enter new UserName: ")
            E_mail = input("Enter Email: ")
            Phone_no = input("Enter Phone number: ")
            Password = input("Create a strong password: ")

            user_data[Uname] = {
                "password": Password,
                "email": E_mail,
                "phone": Phone_no
            }
            logged_user.append(Uname)
            print("User added.")

        print("All Stored Users:")
        for user, info in user_data.items():
            print(f"{user}: {info}")
            Ask = input("Want to go back to main menu? (yes/no): ")
            if Ask.lower() != 'yes':
                terminate()
            else:
                main()
        else:
            print("Invalid username or password.")
            login()
    else:
        again = input("You must register first. To register, press 9: ")
        if again == '9':
            register()
        else:
            print("Wrong input.")
            main()
def Display_profile():
    global current_user
    if current_user and current_user in user_data:
        profile = user_data[current_user]
        print(f"Welcome {current_user}!")
        print(f"Email: {profile['email']}")
        print(f"Phone: {profile['phone']}")
    else:
        print("No user logged in.")
    
def show_profile():
    global registration, logged
    if registration and logged:
        display_profile()
    else:
        print("Please register first.")
        register()
def update_profile():
    pass
def logout():
    pass
def terminate():
    print(f"GOODBYE {Uname}")
    exit()

def main():
    print("Welcome in LNCT")
    response = input('''
        Choose option:
        1. Registration
        2. Login
        3. Profile
        4. Update profile
        5. Logout
        6. Main Menu
        7. Exit

            select option 1/2/3/4/5/6/7: ''')

    if response == '1':
        register()
    elif response == '2':
        login()
    elif response == '3':
        show_profile()
    elif response == '4':
        update_profile()
    elif response == '5':
        logout()
    elif response == '6':
        main()
    elif response == '7':
        terminate()
    else:
        print("Invalid Choice, Please select correct option")
        main()
main()
