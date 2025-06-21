import os
import schedule
import time

data = ""

def CreateLog(Filename, timestamp):
    fobj = open("Backup_log.txt", "w")
    fobj.write(Filename + timestamp + "\n")

def CreateBackup(Filename, Data):
    print("Enter the name of directory to save the backup of files : ")
    Directory = input()

    if not os.path.exists(Directory):
        os.mkdir(Directory)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","_")
    timestamp = timestamp.replace(":", "_")

    Filename = os.path.join(Directory, "Backup(%s)%s" %(Filename, timestamp))

    fobj = open(Filename, "w")
    fobj.write(Data)
    
    print("Backup taken successfully.")

    CreateLog(Filename, timestamp)

def TravelFiles(DiretoryName1):
    global data

    flag = os.path.isabs(DiretoryName1)
    if(flag == False):
        DiretoryName1 = os.path.abspath(DiretoryName1)

    flag = os.path.exists(DiretoryName1)
    if(flag == False):
        print("This named directory does not exists.")
        exit()

    flag = os.path.isdir(DiretoryName1)
    if(flag == False):
        print("This named directory is not available.")
        exit()

    for FolderName, SubFolderNames, FileNames in os.walk(DiretoryName1):
        for Files in FileNames:
            Files1 = os.path.join(FolderName, Files)

            if(Files1.endswith((".py", ".txt", ".c", ".cpp", ".java", ".js", "xlsx", ".docx"))):
                fobj = open(Files1, "r")
                data = fobj.read()
                fobj.close()

            CreateBackup(Files, data)

def main():
    print("Enter the name of directory of which you want to backup all files : ")
    Directory = input()

    schedule.every(1).hour.do(TravelFiles, Directory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()