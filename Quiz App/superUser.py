import mysql.connector
mydb = mysql.connector.connect(host="localhost",user = "root", password = "12345Tyuio", database = "mydb")
mycursor = mydb.cursor()
class SupUser:
    def __init__(self,loginId):
        self.__loginId = loginId

    def addQuestion(self,question,opt1,opt2,opt3,opt4,ans,quizId,difLevel):

        sql = "INSERT INTO questions(Question,Option1,Option2,Option3,Option4,Answer,QuizID,difficulty) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (question,opt1,opt2,opt3,opt4,ans,quizId,difLevel)
        mycursor.execute(sql,val)
        mydb.commit()
    
    def add_user(self,un,passw):
        sql = "INSERT INTO students(UserName,password) VALUES (%s,%s);"
        val = (un,passw)
        mycursor.execute(sql,val)
        mydb.commit()
    
    
    def display_users(self):
        print("-----USER DETAILS------")
        mycursor.execute("SELECT * FROM students;")
        for row in mycursor:
            print("USERNAME :",row[0],"PASSWORD :",row[1])
    
    def display_qna(self):
        mycursor.execute("SELECT * FROM questions;")
        for row in mycursor:
            print("Q",row[0],".",row[1])
            print("a."+row[2]+"\nb."+row[3]+"\nc."+row[4]+"\nd."+row[5]+"\nAnswer  "+row[6])
            print("Difficulty :"+row[8])

    
