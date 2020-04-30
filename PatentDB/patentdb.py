import mysql.connector
from mysql.connector import Error

print("\n\nWelcome to PatentDB!")
s = "MMMMMMMMMMMMMMMMMMMMMMMMMMMNdyo+:-.`        `.-:+oydNMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMNho:.                          .:ohNMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMdo-                                    -odMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMh+`                                          `+hMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMNo.                                                .oNMMMMMMMMMMMMM\nMMMMMMMMMMMN+                                                      +NMMMMMMMMMMM\nMMMMMMMMMN+                `...`                                     +NMMMMMMMMM\nMMMMMMMMs`               `-::::::-                                    `sMMMMMMMM\nMMMMMMN:                 -::::::::.                                     :NMMMMMM\nMMMMMd`                  -::::::::.                                      `dMMMMM\nMMMMy                     .::::::+.                                        yMMMM\nMMMy                        ```  `/+.:////:.      .---`                     yMMM\nMMd                                /++++++++/`.-::-----                      dMM\nMN.                               :+++++++++++:-` `...`                      .NM\nM+                                :++++++++++/                                +M\nN                                 `/++++++++/`                                 N\no                                   /+/++/:.                                   o\n-                               `..:+`                                         -\n                              ./++++/`                                          \n                              /++++++-                                          \n                              .+++++/`                                          \n                                .-.`                                            \n-     -+++/:.                                        .++++/:`    .++++/:`      -\no     :s`  .++            o:                     s:  -s.  `-++`  .s.  `/o`     o\nN     :s`  `++            o:                     s:  -s.     /o  .s.  `/+      N\nM+    :s++++:`  ./++/// -+so+. -/++:`  ::-/++: -+so+.-s.     -s` .s+++o+.     +M\nMN.   :s`      -s.  `o+   o:  /o--/o+  /o-  -s.  s:  -s.     ++  .s.   .o-   .NM\nMMd   :s`      -s-  .o+   o:  /s+-.`   /o   .s.  s:  -s. `.-+/`  .s.  `-s-   dMM\nMMMy  -/        ./++///   /-   -/++:   :/   .+`  /-  .+///:-`    .+////:.   yMMM\nMMMMy                                                                      yMMMM\nMMMMMd`                                                                  `dMMMMM\nMMMMMMN:                                                                :NMMMMMM\nMMMMMMMMy`                                                            `yMMMMMMMM\nMMMMMMMMMN+                                                          +NMMMMMMMMM\nMMMMMMMMMMMN+                                                      +NMMMMMMMMMMM\nMMMMMMMMMMMMMNo.                                                .oNMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMh+`                                          `+hMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMdo-                                    -odMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMNho:.                          .:ohNMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMNdyo+:-.`        `.-:+oydNMMMMMMMMMMMMMMMMMMMMMMMMMMM"
print(s)

def applicant_menu(user):
    choice = 0
    while(choice!=5):
        print("1. File a patent \n2. Check Application Status \n3. Search Patents by title \n4. Search Patents by subject \n5. Logout")
        choice = int(input())
        if(choice==1):
            q1 = "SELECT * FROM Patent_Applications ORDER BY Application_ID DESC"
            cursor.execute(q1)
            result = cursor.fetchall()
            last_id = result[0][0]
            prev_examiner_id = result[0][2]
            prev_attorney_id = result[0][3]
            prev_office_id = result[0][4]
            app_id = last_id+1
            title = input("Title of your Patent:")
            inventor = input("Inventor of solution:")
            category = input("Company/Individual:")
            examiner_id = (prev_examiner_id%1000 + 1)%320 + 500000
            attorney_id = (prev_attorney_id%1000 +1)%200 + 345000
            office_id = (prev_office_id+1)%5 +1 
            status = 'Pending'
            q2 = "INSERT INTO Patent_Applications VALUES(%s, %s, %s, %s, %s)"
            q3 = "INSERT INTO Applicants Values(%s, %s, %s, %s, %s)"
            cursor.execute(q2, (int(app_id), status, int(examiner_id), int(attorney_id), int(office_id)))
            connection.commit()
            cursor.execute(q3, (int(app_id), int(user), title, inventor, category))
            connection.commit()
            print("\nApplication submitted!")
        
        if(choice==2):
            q1 = "SELECT Application_ID FROM Applicants where Applicant_ID = %s"
            cursor.execute(q1, (int(user), ))
            result = cursor.fetchall()
            for application in result:
                q2 = "SELECT Status from Patent_Applications where Application_ID = %s"
                app_id = application[0]
                cursor.execute(q2, (int(app_id),))
                res = cursor.fetchall()
                print(application[0], ":", res[0][0])

        if(choice==3):
            q1 = "SELECT * FROM Patents where Title LIKE %s and Validation_States = 'Approved'"
            keyword = input("Enter Title:")
            keyword = "%"+keyword+"%"
            cursor.execute(q1, (keyword,))
            results = cursor.fetchall()
            for patent in results:
                print("Patent Title:", patent[2])
                print("Patent Subject:", patent[3])
                print("Patent Inventor:", patent[4]+"\n")

        if(choice==4):
            q1 = "SELECT Title, Subject, Inventor FROM Patents where Subject LIKE %s and Validation_States = 'Approved'"
            keyword = input("Enter Title:")
            keyword = "%"+keyword+"%"
            cursor.execute(q1, (keyword,))
            results = cursor.fetchall()
            for patent in results:
                print("Patent Title:", patent[2])
                print("Patent Subject:", patent[3])
                print("Patent Inventor:", patent[4]+"\n")


def patentee_menu(user):
    choice = 0
    while(choice!=5):
        print("1. View Patent Status \n2. View Expired Patents \n3. File a new Patent \n4. Renew a Patent \n5. Logout")
        choice = int(input())

        if(choice==1):
            q1 = "SELECT Patent_ID, Title, Validation_States FROM Patents where Patentee_ID = %s"
            cursor.execute(q1, (int(user),))
            patents = cursor.fetchall()
            for patent in patents:
                print(patent[0], ":", patent[1], ":", patent[2])

        elif(choice==2):
            q1 = "SELECT Patent_ID, Title FROM Patents where Patentee_ID = %s AND Validation_States = 'Expired'"
            cursor.execute(q1, (int(user),))
            patents = cursor.fetchall()
            for patent in patents:
                print(patent[0], ":", patent[1])

        elif(choice==3):
            q1 = "SELECT * FROM Patent_Applications ORDER BY Application_ID DESC"
            cursor.execute(q1)
            result = cursor.fetchall()
            last_id = result[0][0]
            prev_examiner_id = result[0][2]
            prev_attorney_id = result[0][3]
            prev_office_id = result[0][4]
            app_id = last_id+1
            title = input("Title of your Patent:")
            inventor = input("Inventor of solution:")
            category = input("Company/Individual:")
            examiner_id = (prev_examiner_id%1000 + 1)%320 + 500000
            attorney_id = (prev_attorney_id%1000 +1)%200 + 345000
            office_id = (prev_office_id+1)%5 +1 
            status = 'Pending'
            q2 = "INSERT INTO Patent_Applications VALUES(%s, %s, %s, %s, %s)"
            q3 = "INSERT INTO Applicants Values(%s, %s, %s, %s, %s)"
            cursor.execute(q2, (int(app_id), status, int(examiner_id), int(attorney_id), int(office_id)))
            connection.commit()
            cursor.execute(q3, (int(app_id), int(user), title, inventor, category))
            connection.commit()
            print("\nApplication submitted!")

        elif(choice==4):
            q1 = "SELECT MAX(Renewal_Application_ID) FROM Renewal_Applications"
            q2 = "SELECT Patent_Attorney_ID, Patent_Examiner_ID, Office_ID FROM Patents where Patent_ID = %s AND Patentee_ID = %s AND Validation_States='Expired'"
            cursor.execute(q1)
            result = cursor.fetchall()
            last_id = result[0][0]
            app_id = last_id+1
            patent_id = input("Enter Expired Patent ID:")
            cursor.execute(q2, (int(patent_id), int(user)))
            res = cursor.fetchall()
            attorney = res[0][0]
            examiner = res[0][1]
            office = res[0][2]
            q3 = "INSERT INTO Renewal_Applications VALUES(%s, %s, %s, %s, %s, %s)"
            cursor.execute(q3, (int(app_id), int(patent_id), int(office), int(examiner), 'False', 'False'))
            connection.commit()
            print("\nRenewal Application Submitted!\n")



def examiner_menu(user):
    choice = 0
    while(choice!=5):
        print("1. View Pending Patent Applications \n2. View Pending Renewal Applications\n3. Approve or Reject Patent Application \n4. Approve or Reject Renewal Application \n5. Logout")
        choice = int(input())

        if(choice==1):
            q1 = "SELECT Application_ID FROM Patent_Applications where Status = 'Pending' and Patent_Examiner_ID = %s"
            cursor.execute(q1, (int(user),))
            res = cursor.fetchall()
            for pending in res:
                print(pending[0])

        elif(choice==2):
            q1 = "SELECT Renewal_Application_ID FROM Renewal_Applications where Renewal_Status = 'False' and Examiner_ID = %s"
            cursor.execute(q1, (int(user),))
            res = cursor.fetchall()
            for pending in res:
                print(pending[0])

        elif(choice==3):
            app_id = input("\nEnter the Application ID:")
            q1 = "UPDATE Patent_Applications SET Status = %s WHERE Application_ID = %s"
            decision = input("Approved or Rejected:")
            cursor.execute(q1, (decision, int(app_id)))
            connection.commit()
            print("Application", decision)
            
        elif(choice==4):
            app_id = input("\nEnter the Renewal Application ID:")
            q1 = "UPDATE Renewal_Applications SET Renewal_Status = %s WHERE Renewal_Application_ID = %s"
            decision = input("Approved or Rejected:")
            dec = "None"
            if(decision=="Approved"):
                dec = "True"
            else:
                dec = "False"
            cursor.execute(q1, (dec, int(app_id)))
            connection.commit()
            print("Renewal Application", decision)



def attorney_menu(user):
    choice = 0
    while(choice!=3):
        print("1. View Patentees \n2. View Applicants \n3. Logout ")
        choice = int(input())

        if(choice==1):
            q1 = "SELECT Patentee_ID, Inventor FROM Patents where Patent_Attorney_ID = %s"
            cursor.execute(q1, (int(user), ))
            results = cursor.fetchall()
            for patentee in results:
                print(patentee[0], ":", patentee[1])

        elif(choice==2):
            q1 = "SELECT Applicant_ID, Inventor, Applicant_Status from Applicants where Application_ID IN (SELECT Application_ID FROM Patent_Applications where Patent_Attorney_ID = %s)"
            cursor.execute(q1, (int(user), ))
            results = cursor.fetchall()
            for patentee in results:
                print(patentee[0], ":", patentee[1], ":", patentee[2])

def researcher_menu():
    choice = 0
    while(choice!=4):
        print("1. Search Patents by Title \n2. Search Patents by Subject \n3. View Trending Research Topics \n4. Exit PatentDB ")
        choice = int(input())

        if(choice==1):
            q1 = "SELECT * FROM Patents where Title LIKE %s and Validation_States = 'Approved'"
            keyword = input("Enter Title:")
            keyword = "%"+keyword+"%"
            cursor.execute(q1, (keyword,))
            results = cursor.fetchall()
            for patent in results:
                print("Patent Title:", patent[2])
                print("Patent Subject:", patent[3])
                print("Patent Inventor:", patent[4]+"\n")
        
        if(choice==2):
            q1 = "SELECT * FROM Patents where Subject LIKE %s and Validation_States = 'Approved'"
            keyword = input("Enter Title:")
            keyword = "%"+keyword+"%"
            cursor.execute(q1, (keyword,))
            results = cursor.fetchall()
            for patent in results:
                print("Patent Title:", patent[2])
                print("Patent Subject:", patent[3])
                print("Patent Inventor:", patent[4]+"\n")


def login():
    print("1. Login \n2. Register \n3. I am a researcher")
    n = int(input())
    role = 'None'
    if n==1:
        print("Enter your UserID: ")
        user_id = int(input())
        print("Enter your Password: ")
        password = input()
        #Check in db and do identification

        q = "SELECT * FROM Login_Credentials where Username = %s AND Password = %s"
        creds = (user_id, password)
        cursor.execute(q,creds)
        result = cursor.fetchall()
        role = result[0][2]

        if(role=="Applicant"):
            applicant_menu(user_id)
        elif(role=="Patentee"):
            patentee_menu(user_id)
        elif(role=="Patent_Examiner"):
            examiner_menu(user_id)
        elif(role=="Patent_Attorney"):
            attorney_menu(user_id)
        else:
            print("Incorrect password")

    if n==2:
        #Get ID and add to table

        role = input("Who are you? \nApplicant/Patentee/Attorney/Examiner:")
        name = input("Full Name:")
        password = input("Set Password:")

        if(role=="Applicant"):
            q = "SELECT MAX(Applicant_ID) FROM Applicants"
            cursor.execute(q)
            res = cursor.fetchall()
            user_id = res[0][0]+1
            q2 = "INSERT INTO Login_Credentials VALUES(%s, %s, %s)"
            cursor.execute(q2, (int(user_id), password, role))
            connection.commit()
            print("REGISTERED TO PatentDB!")
            applicant_menu(user_id)
        elif(role=="Patentee"):
            q = "SELECT MAX(Patentee_ID) FROM Patentees"
            cursor.execute(q)
            res = cursor.fetchall()
            user_id = res[0][0]+1
            q2 = "INSERT INTO Login_Credentials VALUES(%s, %s, %s)"
            cursor.execute(q2, (int(user_id), password, role))
            connection.commit()
            print("REGISTERED TO PatentDB!")
            patentee_menu(user_id)
        elif(role=="Examiner"):
            q = "SELECT MAX(Patent_Examiner_ID) FROM Patent_Examiners"
            cursor.execute(q)
            res = cursor.fetchall()
            user_id = res[0][0]+1
            q2 = "INSERT INTO Login_Credentials VALUES(%s, %s, %s)"
            cursor.execute(q2, (int(user_id), password, role))
            connection.commit()
            print("REGISTERED TO PatentDB!")
            examiner_menu(user_id)
        elif(role=="Attorney"):
            q = "SELECT MAX(Patent_Attorney_ID) FROM Patent_Attorneys;"
            cursor.execute(q)
            res = cursor.fetchall()
            user_id = res[0][0]+1
            q2 = "INSERT INTO Login_Credentials VALUES(%s, %s, %s)"
            cursor.execute(q2, (int(user_id), password, role))
            connection.commit()
            print("REGISTERED TO PatentDB!")
            attorney_menu(user_id)

    if n==3:
        researcher_menu()


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='PatentDB',
                                         user='root',
                                         password='admin')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to PatentDB")
        login()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("Connection to PatentDB is closed")

