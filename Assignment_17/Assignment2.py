import schedule
import time
import datetime

def DisplayDateTime():
    timestamp = datetime.datetime.now()
    print(timestamp)

def main():
    schedule.every(1).minutes.do(DisplayDateTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()