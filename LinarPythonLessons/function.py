
#Ask or create a function to determine student details: first name, last name, school name, exam number and seat number
yellow = '\033[93m'#ANSI color codes, to implement color in out put
green = '\033[92m'
red = '\033[91m'
bold = '\033[1m' #to make output bold
reset = '\033[0m'# to reset back to normal
print (f" {yellow} WELCOME TO LINAR EXAM ASSESSMENT PORTAL{reset}")
print (f"{bold}The Linar Exam Assessment Portal is designed to grade student exam score for each subject as well as\ncalculates student cummulative and aggregate scores, and provides immediate pass or fail status.\nAlso students who meet the passmark can generate a detailed statement of result {reset}")
print()
qst1 = input(f"Do you wish to proceed? (yes or no) ")
import sys
if qst1 == "no":
  print(f'Exiting....\n{green}Goodbye!{reset}')
  sys.exit() # exit function to terminate a process from running
else:
  while True:
    code = input(f"Enter the verification code \"@1234%\" to be granted access: ")
    try:
      if code == "@1234%":
        print (f"Access granted \u2714")
        break # Exit the loop when condition is true
      else:
        print ("Acess denied \u274c")
    except ValueError:
      print()
    print(f"{bold}Invalid verification code, Please enter the verification code as provided{reset}")

def student_details():
  Student_firstname = input("Enter first_name: ")
  Student_lastname = input ("Enter last_name: ")
  Gender = input("Gender: ")
  School_name = input ("School Name: ")
  Exam_Number = input("Examination Number: ")
  Seat_Number = input("Seat Number: ")
  print()
  print(f'VERIFYING STUDENT DETAILS' )
  import time
  for i in range(3):
    print("Please wait...") # iterates please wait 3 times as in range
    time.sleep(3) # 3 in bracket indicates how many seconds loop counts before it iterates
  print(f'Verification complete and successful!\nStudent First Name:{Student_firstname.upper()} \nStudent Last Name:{Student_lastname.upper()} \nExam Number:{Exam_Number}\nSeat No: {Seat_Number} \nGender: {Gender.upper()} \nSchool: {School_name.upper()}')
  print ("Proceed to enter your score on each subject")
  grading(Student_firstname,Student_lastname,School_name, Exam_Number,Seat_Number)
  print()
# Determine 5 subject grading
def grading(Student_firstname, Student_lastname, School_name, Exam_Number, Seat_Number):
  English = int(input(f"Enter English Score: "))
  Maths = int(input("Enter Maths Score: "))
  Physics = int(input("Enter Physics Score: "))
  Chemistry = int(input("Enter Chemistry Score: "))
  ICT = int(input("Enter ICT Score: "))
  print()
  if English <= 100 and English >=70:
    print (f'English:{English}')
    Eremark = "Excellent(A)"
  elif English <70 and English >= 60:
    print (f'English:{English}')
    Eremark = "Very Good(B)"
  elif English <60 and English >=50:
    print (f'English:{English}') 
    Eremark = "Average(C)"
  elif English <50 and English >=40:
    print (f'English:{English}') 
    Eremark = "Poor(D)"
  elif English <40 and English >=0:
    print (f'English:{English}')
    Eremark = "Fail(F)" 
  else:
    print (f'English: invalid score entered. Score range (0-100)')
  if Maths <= 100 and Maths >=70:
     print (f'Maths:{Maths}')
     math_remark = "Excellent(A)"
  elif Maths <70 and Maths >= 60:
    print (f'Maths:{Maths}') 
    math_remark = "Very Good(B)"
  elif Maths <60 and Maths >=50:
    print (f'Maths:{Maths} ')
    math_remark = "Average(C)" 
  elif Maths <50 and Maths >=40:
    print (f'Maths:{Maths}') 
    math_remark = "Poor(D)"
  elif Maths <40 and Maths >=0:
    print (f'Maths:{Maths} ')
    math_remark= "Fail(F)" 
  else:
    print (f'Maths:invalid score entered. Score range (0-100)')
  if Physics <= 100 and Physics >=70:
     print (f'Physics:{Physics}')
     Premark = "Excellent(A)"
  elif Physics <70 and Physics >= 60:
    print (f'Physics:{Maths} ') 
    Premark = "Very good(B)"
  elif Physics <60 and Physics >=50:
    print (f'Physics:{Maths}') 
    Premark = "Average(C)"
  elif Physics <50 and Physics >=40:
    print (f'Physics:{Physics}') 
    Premark = "Poor(D)"
  elif Physics <40 and Physics >=0:
    print (f'Physics:{Physics}')
    Premark = "Fail(F)"
  else:
    print (f'Physics: invalid score entered. Score range (0-100)') 
  if Chemistry <= 100 and Chemistry >=70:
    print (f'Chemistry:{Chemistry}')
    Cremark = "Excellent(A)"
  elif Chemistry <70 and Chemistry >= 60:
    print (f'Chemistry:{Chemistry}')
    Cremark = "Very Good(B)"
  elif Chemistry <60 and Chemistry >=50:
    print (f'Chemistry:{Chemistry}') 
    Cremark = "Average(C)"
  elif Chemistry <50 and Chemistry >=40:
    print (f'Chemistry:{Chemistry}') 
    Cremark = "Poor(D)"
  elif Chemistry <40 and Chemistry >=0:
    print (f'Chemistry:{Chemistry}')
    Cremark = "Fail(F)"
  else:
    print (f'Chemistry: invalid score entered. Score range (0-100)')
  if ICT <= 100 and ICT >=70:
    print (f'ICT:{ICT} ')
    Iremark = "Excellent(A)"
  elif ICT <70 and ICT >= 60:
    print (f'ICT:{ICT}')
    Iremark = "Very Good(B)"
  elif ICT <60 and ICT >=50:
    print (f'ICT:{ICT}')
    Iremark = "Average(C)" 
  elif ICT <50 and ICT >=40:
    print (f'ICT:{ICT}') 
    Iremark = "poor(D)"
  elif ICT <40 and ICT >=0:
    print (f'ICT:{ICT}') 
    Iremark = "Fail(F)"
  else:
    print (f' ICT: invalid score entered. Score range (0-100) ')
  cumm_score = English + Maths + Physics + Chemistry + ICT 
    #determine the,cummulative score, average score and status of student as either pass or fail
  print()
  def scorecal():
    passmark = 50
    print (f"{bold}NB: To pass this exam,the avearge score of your total score must be {passmark} and above{reset}")
    totalscore = cumm_score
    print (f'Your total  score is: {totalscore} / 500')
    Averagescore = totalscore / 5
    if Averagescore == 50:
      print (f'Your Average score is: {Averagescore} \nCongratulations!!! you have met the passmark')
    elif Averagescore >50:
      print (f'Your Average score is: {Averagescore}\nCongratulations!!! you have exceeded the passmark')
    else:
      print(f'Your Average score is: {Averagescore}\nUnfortunately you did not met the passmark, stay focused and try again')
    
    def statement_of_result():
      if Averagescore == 50 or Averagescore >50:
          ask = input("Do you want to print your statement of result? \nEnter yes or No: ")
          print(ask)
          import sys
          if ask == "yes":
            import time
            for i in range (1):
              print ("loading...")
            time.sleep(2)  
            print()
            print (f'{bold}......STATEMENT OF RESULT........{reset} \nTO Whom it may concern')
            print (f'This is to inform you that {Student_firstname} {Student_lastname} a student of {School_name} whith the examination number: {Exam_Number}\nand seat number:{Seat_Number} successfully passed his/her exam at {School_name}')
            print("\nBelow is the result summary:")
            print()
            print(F'English = {English} -{Eremark}')
            print(F'Mathematics = {Maths} -{math_remark}')
            print(F'Physics = {Physics} -{Premark}')
            print(F'Chemistry = {Chemistry} -{Cremark}')
            print(F'Information and Computer Technology = {ICT} -{Iremark}')
            print()
            print("THANK YOU!")
            print()
            print(f"SIGNED by {School_name}")
            print()
            print(f'Designed by PEACE')
          else:
            print(f'Thank you for using Linar Exam Assesment Portal \nExiting....\n{green}Goodbye!{reset}')
            sys.exit
      else:
          print("Only Student with PassMark and Above can print their Statement of Result")
          print("Thank you for using LINAR EXAM ASSESMENT PORTAL")
    statement_of_result()
  scorecal()
student_details() # note identation and chronological arrangement of def function
# Student details call itself and indirectly calls grading() as part of its process.

  
   
   




  



  

  

  