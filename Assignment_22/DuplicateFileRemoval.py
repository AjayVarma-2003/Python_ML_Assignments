import os
import sys
import hashlib
import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def CalculateCheckSum(File):
    fobj = open(File, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DirectoryTravel(DirectoryName):
    Duplicate = {}
    Count = 0

    flag = os.path.isabs(DirectoryName)
    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if(flag == False):
        print("There is no such directory available in current directory.")

    flag = os.path.isdir(DirectoryName)
    if(flag == False):
        print("There is no such directory available.")

    for FolderName, SubFolders, FileNames in os.walk(DirectoryName):
        for File in FileNames:
            Count += 1
            fname = os.path.join(FolderName, File)

            ret = CalculateCheckSum(fname)

            if ret in Duplicate:
                Duplicate[ret].append(fname)
            else:
                Duplicate[ret] = [fname]

    return Duplicate, Count

def SendMail(File, Cnt, count):
    start_time = time.ctime()
    start_time = str(start_time)

    sender_email = "ajayvarma20062003@gmail.com"
    sender_pass = "joqd oivd csrn lxxd"
    reciever_email = sys.argv[3]
    subject = "Record of Duplicate files removal."
    body = start_time + "\n" + "Total number of files scanned are : " + str(count) + "\n" + "Total number of duplicate files deleted : " + str(Cnt) + "\n"
    File_path = File

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = reciever_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    fobj = open(File_path, "rb")

    attached_file = MIMEApplication(fobj.read(), _subtype = "txt")
    attached_file.add_header('Content-Disposition', 'attachment', filename = 'Log.txt')
    msg.attach(attached_file)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_pass)
            server.send_message(msg)
        print("Email send successfully")

    except Exception as eboj:
        print(f"Error sending in sending email : {eboj}")


def DeleteDuplicate(path):

    Mydict, count1 = DirectoryTravel(path)

    Count = 0
    Cnt = 0

    Check = lambda X: (len(X) > 1)

    Result = list(filter(Check, Mydict.values()))

    fobj = open("Log.txt", "w")

    fobj.write("Deleted files are : " + "\n")

    for value in Result:
        for subvalue in value:
            Count += 1
            if(Count > 1):
                Cnt += 1
                fobj.write(str(subvalue) + "\n")
                os.remove(subvalue)
        Count = 0

    fobj.write("Number of duplicate files which are delted are : " + str(Cnt) + "\n")
    fobj.close()

    SendMail("Log.txt", Cnt, count1)

def main():
    border = "-" * 54

    print(border)
    print(border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This is help section of script.")
            print("This is automation script for removing duplicate files from directory and sendign details in logbook to mail.")
            print("Type --u to get the how to use script.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("This is use section of script.")
            print("Type following command to run script properly.")
            print("python Scriptname.py Directoryname TimeforScheduling ReceiverMailId")

    elif(len(sys.argv) == 4):
        schedule.every(int(sys.argv[2])).minutes.do(DeleteDuplicate, sys.argv[1])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments.")
        print("--h : type with command to open Help section of script.")
        print("--u : type with command to open Use section of script.")

if __name__ == "__main__":
    main()