import psutil
import os
import time
import smtplib
import getpass
from email.message import EmailMessage

def CreateLog(Data, directory):

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    FileName = f"Marvellous_{timestamp}.log"
    full_path = os.path.join(directory, FileName)

    with open(full_path, "w") as fobj:
        border = "-"*80
        fobj.write(border + "\n")
        fobj.write("\n\t\tMarvellous Infosystems Process Log\n")
        fobj.write(f"\t\tLog file is created at : {time.ctime()}\n")
        fobj.write(border + "\n\n")

        for value in Data:
            fobj.write(f"{value}\n\n")

        fobj.write(border + "\n")
    
    return full_path

def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid', 'name', 'username'])
            listprocess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

def SendMail(file_path, recipient_email):
    sender_email = "ajayvarma@gmail.com"    # example email id as it can ban my mail id.
    sender_password = getpass.getpass(prompt="Enter your email password (hidden input): ")

    msg = EmailMessage()
    msg['Subject'] = 'Process Log File - Marvellous Infosystems'
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content('Please find attached the process log file.')

    with open(file_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(file_path)
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as eobj:
        print(f"Failed to send email: {eobj}")

def main():
    directory = input("Enter directory to save log file: ")
    recipient_email = input("Enter recipient email address: ").strip()

    if not os.path.exists(directory):
        os.makedirs(directory)

    processes = ProcessScan()
    log_path = CreateLog(processes, directory)
    SendMail(log_path, recipient_email)

if __name__ == "__main__":
    main()
