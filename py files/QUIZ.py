import os.path
from decimal import Decimal

subject = input("Subject: ")
difficulty = input("Difficulty: ")
qnum = 1
mark = 0
#if a highscore file for the input difficulty doesn't exist, one is made.
if os.path.exists(r'''E:\\QUIZPROGRAM\\'''+difficulty.upper()+subject.upper()+'''HighScore.txt''') == False:
    createHSFile = open(difficulty.upper()+subject.upper()+"HighScore.txt","w")
    createHSFile.write("0")
    createHSFile.close()
#while loop that prints all the questions, and checks the answers against a mark scheme
while qnum <= 4:
    subjectQ = open("q"+str(qnum)+subject.upper()+"_"+difficulty.lower()+".txt",'r')
    subjectQAns = open("q"+str(qnum)+subject.upper()+"_"+difficulty.lower()+"_answer.txt",'r')
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
if os.path.exists(r'''E:\\QUIZPROGRAM\\'''+str(username.upper())+str(difficulty.upper())+subject.upper()+'''Score.txt''') == False:
    subjectScore = open(str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt","w")
    subjectScore.write(str(mark))
    subjectScore.close()
#copies the users already saved marks, then re-writes the file along with the new mark
elif os.path.exists(r'''E:\\QUIZPROGRAM\\'''+str(username.upper())+str(difficulty.upper())+subject.upper()+'''Score.txt''') == True:
    subjectScore = open(str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt","r")
    userSubjectScore = subjectScore.read()
    subjectScore.close()
    writeLatestScore = open(str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt","w")
    allScores = str(userSubjectScore)+"\n"+str(mark)
    subjectScore = open(str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt","w")
    subjectScore.write(allScores)
    subjectScore.close()
#opens and reads the chosen difficulties maths highscore
subjectScore = open(difficulty.upper()+subject.upper()+"HighScore.txt","r")
subjectHighScore = subjectScore.read()
subjectScore.close()
#compares the mark achieved and the highscore mark
if mark > int(str(subjectHighScore[:1])):
    #writes the mark to the file if it's the highest
    subjectWrite = open(difficulty.upper()+subject.upper()+"HighScore.txt","w")
    subjectWrite.write(str(mark)+"\n"+username.upper())
    subjectWrite.close()
Next = input("Would you like a report on your progress, or who scored the highest mark (report/highscore)?: ")
#generates report on progress
if Next == "report":    
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
    numLines = file_len(str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt")
    #opens users score list
    strLines = open(str(username.upper())+str(difficulty.upper())+subject.upper()+"Score.txt","r")
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
    running = open(difficulty.upper()+subject.upper()+"HighScore.txt","r")
    out_of = running.readlines()
    variable_names = str(out_of)
    out_of[0] = out_of[0][:1]
    print(out_of[1]+": "+out_of[0])
