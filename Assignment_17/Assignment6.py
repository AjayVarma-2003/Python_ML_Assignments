import schedule
import time

def LunchTime():
    print("Lunch Time ...")

def EndTime():
    print("Wrap the work ...")

def main():
    schedule.every().day.at('13:00').do(LunchTime)
    schedule.every().day.at('18:00').do(EndTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()