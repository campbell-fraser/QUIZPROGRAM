#imports os.path to check whether a file exists or not
import os.path
Continue = False

login = input("LOGIN or CREATE ACCOUNT: ")
print("(Username and password are case sensitive)")
#while loop waiting until real account details are input
while Continue == False:
    #login loop, not accepting until actual account details are input
    if login == "login":
        print("\nLOGIN")
        username = input("Username: ")
        password = input("Password: ")
        if os.path.exists(r'''C:\\\Users\\\fraze\\Documents\\QUIZPROGRAM\\'''+str(username)+"ACCOUNTDETAILS"+'''.txt''') == True:
            userRead = open(username+"ACCOUNTDETAILS"+".txt",'r')
            userCheck = userRead.read()
            if userCheck == username+password:
                print("Login accepted")
                Continue = True
            else:
                print("Username or password incorrect, try again")
        if os.path.exists(r'''C:\\\Users\\\fraze\\Documents\\QUIZPROGRAM\\'''+str(username)+"ACCOUNTDETAILS"+'''.txt''') == False:
            print("Account does not exist.")
    #account creation loop, only proceeding when original account info is input
    elif login == "create account":
        username = input("Username: ")
        password = input("Password: ")
        if os.path.exists(r'''C:\\\Users\\\fraze\\Documents\\QUIZPROGRAM\\'''+str(username)+"ACCOUNTDETAILS"+'''.txt''') == False:
            userCreate = open(str(username)+"ACCOUNTDETAILS"+".txt","w")
            userCreate.write(str(username)+str(password))
            userCreate.close()
            login = "login"
        elif os.path.exists(r'''C:\\\Users\\\fraze\\Documents\\QUIZPROGRAM\\'''+str(username)+"ACCOUNTDETAILS"+'''.txt''') == True:
            print("Username already taken, try another.")
