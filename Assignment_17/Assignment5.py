import schedule
import time
import datetime

def CurrentTimeLogFile():
    fobj = open("Marvellous.txt", "a")                  # opening file in append mode cause write mode is erasing last data.
    fobj.write(str(datetime.datetime.now()) + "\n")
    print("Entry in log file...")
    fobj.close()

def main():
    schedule.every(1).minutes.do(CurrentTimeLogFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()