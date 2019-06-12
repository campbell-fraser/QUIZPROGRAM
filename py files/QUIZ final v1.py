run = True
change_account = True
#imports os.path to check whether a file exists or not
import os.path
from decimal import Decimal

#function that removes the annoying ".0" that was being printed after the average was found
def format_float(f):
    d = Decimal(str(f));
    return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()
counter = 0

#function to find number of lines
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
while run == True:
    while change_account == True:
        login = input("LOGIN or CREATE ACCOUNT: ")
        print("(Username and password are case sensitive)")
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
                    else:
                        print("Username or password incorrect, try again")
                elif os.path.exists(r'''G:\\QUIZPROGRAM\\'''+str(username)+"ACCOUNTDETAILS"+'''.txt''') == False:
                    print("Account does not exist.")
            #account creation loop, only proceeding when original account info is input
            elif login == "create account":
                username = input("Username: ")
                password = input("Password: ")
                if os.path.exists(r'''G:\\QUIZPROGRAM\\accounts\\'''+str(username)+"ACCOUNTDETAILS"+'''.txt''') == False:
                    userCreate = open(r'''G:\\QUIZPROGRAM\\accounts\\'''+str(username)+"ACCOUNTDETAILS"+".txt",'w')
                    userCreate.write(str(username)+str(password))
                    userCreate.close()
                    login = "login"
                elif os.path.exists(r'''G:\\QUIZPROGRAM\\accounts'''+str(username)+"ACCOUNTDETAILS"+'''.txt''') == True:
                    print("Username already taken, try another.")
    
    subject = input("Subject: ")
    difficulty = input("Difficulty: ")
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
    Next = input("Would you like a report on your progress, or who scored the highest mark (report/highscore)?: ")
    #generates report on progress
    if Next == "report":    
        numLines = file_len(r'''G:\\QUIZPROGRAM\\scores\\'''+str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt")
        #opens users score list
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
            printnum = 0
            try: 
                printnum += float(line)
                total += printnum
            except ValueError:
                print("Invalid Literal for Int() With Base 10:", ValueError)
        #finds average
        average = total/numLines
        #formats average, removing the ".0"
        average = format_float(average)
        print("Average score: "+str(average))
    if Next == "highscore":
        running = open(r'''G:\\QUIZPROGRAM\\scores\\'''+difficulty.upper()+subject.upper()+"HighScore.txt",'r')
        out_of = running.readlines()
        variable_names = str(out_of)
        out_of[0] = out_of[0][:1]
        print(out_of[1]+": "+out_of[0])
    again = input("Would you like to change accounts, or logout? ")
    if again == "logout":
        run = False
        change_account = False
    elif again == "change accounts":
        change_account = True
