run = True
counter = 0
change_account = True
import os.path
from decimal import Decimal

#function to find number of lines
def line_num(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

while run == True:
    while change_account == True:
        #user is given option to login or change accounts
        loop5 = True
        while loop5 == True:
            login = input("LOGIN or CREATE ACCOUNT: ")
            login = login.lower()
            if login == "login" or login == "create account":
                loop5 = False
            else:
                print("Please enter a valid answer.")
        print("(Username and password are case sensitive.)")
        #while loop waiting until real account details are input
        while change_account == True:
            #login loop, not accepting until actual account details are input
            if login == "login":
                print("\nLOGIN")
                username = input("Username: ")
                password = input("Password: ")
                if os.path.exists(r'''G:\\QUIZPROGRAM\\accounts\\'''+str(username)+"ACCOUNTDETAILS"+'''.txt''') == True:
                    userRead = open(r'''G:\\QUIZPROGRAM\\accounts\\'''+username+"ACCOUNTDETAILS"+".txt",'r')
                    userCheck = userRead.read()
                    if userCheck == username+password:
                        print("Login accepted")
                        change_account = False
                        Continue = True
                    else:
                        print("Username or password incorrect, try again")
                elif os.path.exists(r'''G:\\QUIZPROGRAM\\'''+str(username)+"ACCOUNTDETAILS"+'''.txt''') == False:
                    print("Account does not exist.")
            #account creation loop, only proceeding when original account info is input
            if login == "create account":
                username = input("Username: ")
                password = input("Password: ")
                if os.path.exists(r'''G:\\QUIZPROGRAM\\accounts\\'''+str(username)+"ACCOUNTDETAILS"+'''.txt''') == False:
                    userCreate = open(r'''G:\\QUIZPROGRAM\\accounts\\'''+str(username)+"ACCOUNTDETAILS"+".txt",'w')
                    userCreate.write(str(username)+str(password))
                    userCreate.close()
                    login = "login"
                elif os.path.exists(r'''G:\\QUIZPROGRAM\\accounts\\'''+str(username)+"ACCOUNTDETAILS"+'''.txt''') == True:
                    print("Username already taken, try another.")

    #while loop used to redo the quiz segment if the user chooses to
    while Continue == True:
        loop3 = True
        while loop3 == True:
            print("Subjects available:\nMaths")
            subject = input("Subject: ")
            subject = subject.lower()
            if subject == "maths" or subject == "geography" or subject == "spanish":
                loop3 = False
            else:
                print("We do not currently have that subject.")
        loop4 = True
        while loop4 == True:
            difficulty = input("Difficulty (easy/medium/hard): ")
            difficulty = difficulty.lower()
            if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
                loop4 = False
            else:
                print("Please enter a valid difficulty.")
        qnum = 1
        mark = 0
        #if a highscore file for the input difficulty doesn't exist, one is made.
        if os.path.exists(r'''G:\\QUIZPROGRAM\\scores\\'''+difficulty.upper()+subject.upper()+"HighScore.txt") == False:
            createHSFile = open(r'''G:\\QUIZPROGRAM\\scores\\'''+difficulty.upper()+subject.upper()+"HighScore.txt",'w')
            createHSFile.write("0")
            createHSFile.close()
        #while loop that prints all the questions, and checks the answers against a mark scheme
        while qnum <= 4:
            subjectQ = open(r'''G:\\QUIZPROGRAM\\questions\\'''+subject+'''\\'''+difficulty+'''\\q'''+str(qnum)+".txt",'r')
            subjectQAns = open(r'''G:\\QUIZPROGRAM\\answers\\'''+subject+'''\\'''+difficulty+'''\\q'''+str(qnum)+"_answer.txt",'r')
            question = subjectQ.read()
            answer = subjectQAns.read()
            ans = input(question)
            if subject == "physics":
                ans = ans.lower()
            if ans == answer:
                mark = mark + 1
            qnum = qnum + 1
        #grading system
        if mark == 0:
            grade = "U"
        if mark == 1:
            grade = "D"
        if mark == 2:
            grade = "C"
        if mark == 3:
            grade = "B"
        if mark == 4:
            grade = "A"
        #calculates the percentage and mark out of
        finalMark = (str(mark)+"/4")
        percentage = (str(mark*25)+"%")
        #prints final mark, percentage and grade
        print(finalMark)
        print(percentage)
        print(grade)
        #creates a user file if it doesnt't already exist, and writes the mark and difficulty into it
        if os.path.exists(r'''G:\\QUIZPROGRAM\\scores\\'''+str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt") == False:
            subjectScore = open(r'''G:\\QUIZPROGRAM\\scores\\'''+str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt",'w')
            subjectScore.write(str(mark))
            subjectScore.close()
        #copies the users already saved marks, then re-writes the file along with the new mark
        elif os.path.exists(r'''G:\\QUIZPROGRAM\\scores\\'''+str(username.upper())+str(difficulty.upper())+subject.upper()+'''Score.txt''') == True:
            subjectScore = open(r'''G:\\QUIZPROGRAM\\scores\\'''+str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt",'r')
            userSubjectScore = subjectScore.read()
            subjectScore.close()
            writeLatestScore = open(r'''G:\\QUIZPROGRAM\\scores\\'''+str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt",'w')
            allScores = str(userSubjectScore)+"\n"+str(mark)
            subjectScore = open(r'''G:\\QUIZPROGRAM\\scores\\'''+str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt",'w')
            subjectScore.write(allScores)
            subjectScore.close()
        #opens and reads the chosen difficulties maths highscore
        subjectScore = open(r'''G:\\QUIZPROGRAM\\scores\\'''+difficulty.upper()+subject.upper()+"HighScore.txt",'r')
        subjectHighScore = subjectScore.read()
        subjectScore.close()
        #compares the mark achieved and the highscore mark
        if mark > int(str(subjectHighScore[:1])):
            #writes the mark to the file if it's the highest
            subjectWrite = open(r'''G:\\QUIZPROGRAM\\scores\\'''+difficulty.upper()+subject.upper()+"HighScore.txt",'w')
            subjectWrite.write(str(mark)+"\n"+username.upper())
            subjectWrite.close()
        loop1 = True
        while loop1 == True:
            Next = input("Would you like a report on a user's progress in this difficulty, or who scored the highest mark (report/highscore)?: ")
            Next = Next.lower()
            #generates report on progress
            if Next == "report":
                try:
                    username = input("Which user's scores would you like to see? ")
                    numLines = line_num(r'''G:\\QUIZPROGRAM\\scores\\'''+str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt")
                    #opens users score list
                    if os.path.exists(r'''G:\\QUIZPROGRAM\\scores\\'''+str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt") == True:
                        loop1 = False
                    strLines = open(r'''G:\\QUIZPROGRAM\\scores\\'''+str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt",'r')
                    #puts each line into a list
                    lines = list(strLines)
                    p = str(lines)
                    strLines.close()
                    #while loop that shortens each variable in the list to just one character
                    while counter < numLines:
                        lines[counter] = lines[counter][:1]
                        counter = counter + 1
                    total = 0
                    #for loop, adding all the lines together for a total
                    for line in lines:
                        num = 0
                        num += int(line)
                        total += int(num)
                    #finds average
                    average = total/numLines
                    print("Average score: "+str(average))
                except FileNotFoundError:
                    print("That user does not exist.")
            elif Next == "highscore":
                loop1 = False
                try:
                    running = open(r'''G:\\QUIZPROGRAM\\scores\\'''+difficulty.upper()+subject.upper()+"HighScore.txt",'r')
                    out_of = running.readlines()
                    variable_names = str(out_of)
                    out_of[0] = out_of[0][:1]
                    print(out_of[1]+": "+out_of[0])
                except FileNotFoundError:
                    print("That user does not exist.")
        loop2 = True
        while loop2 == True:
            again = input("\nWould you like to change accounts, do another quiz, or logout? ")
            again = again.lower()
            if again == "logout":
                loop2 = False
                run = False
                change_account = False
                Continue = False
            elif again == "change accounts":
                loop2 = False
                change_account = True
                Continue = False
            elif again == "do another" or again == "do another quiz":
                loop2 = False
                Continue = True
            else:
                print("Please enter valid answer.")
