from superUser import SupUser
from student import User
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user = "root", password = "12345Tyuio", database = "mydb")
mycursor = mydb.cursor()


while(True):
    print("\n\n1.Super User\n2.Student\n")
    choice = input("Enter 1 if you are a Super user\nEnter 2 if you are a Student: \n Anything else to exit\n")
    if choice == "1":
        loginId = input("Enter SuperUser Login ID :")
        passd = input("Enter SuperUser Password :")
        sql = "SELECT * FROM admin WHERE UserName = %s and password = %s"
        val = (loginId,passd)
        mycursor.execute(sql,val)
        res = mycursor.fetchall()
        if res:
            ch1 = "1"
            while(ch1 == "1"):
                print("***********************\n1.Add Question\n2.Add User\n3.Users Information\n4.Exam MCQS\n***************")
                ch2 = input("Enter Here :")
                obj = SupUser(loginId)
                quizId = res[0][0]
                if ch2 == "1":
                    ques = input("Enter question here :")
                    opt1 = input("Enter option1 here : ")
                    opt2 = input("Enter option2 here : ")
                    opt3 = input("Enter option3 here : ")
                    opt4 = input("Enter option4 here : ")
                    ans = input("Enter the correct Answer here : ")
                    difLevel = input("Enter the difficulty level : ")
                    obj.addQuestion(ques,opt1,opt2,opt3,opt4,ans,quizId,difLevel)
                elif ch2 == "2":
                    name = input("Enter username :")
                    password = input("Enter password :")
                    obj.add_user(name,password)
                elif ch2 == "3":
                    obj.display_users()
                elif ch2 == "4":
                    obj.display_qna()

                i = input("\nType 1 if you want to continue or Anything else to exit\n")
        else:
            print("ERROR : INVALID USERNAME OR PASSWORD\n")

    elif choice == "2":
        loginId = input("Enter User Login ID :")
        password = input("Enter User Password :")
        sql = "SELECT * FROM students WHERE UserName = %s and password = %s"
        val = (loginId,password)
        mycursor.execute(sql,val)
        res = mycursor.fetchall()
        while(True):
            if res:
                ch1 = "1"
                while(ch1 == "1"):
                    print("\n*******************\n1.Take the Quiz\n2.Get Information\n****************")
                    ch2 = input("Enter :")
                    if ch2 == "1":
                        obj = User(loginId)
                        obj.takeQuiz()
                    elif ch2 == "2":
                        obj = User(loginId)
                        obj.user_info(loginId)
                    i = input("Type 1 to continue and anything else to exit ")
                    
            else:
                print("ERROR : INVALID USERNAME OR PASSWORD\n")



