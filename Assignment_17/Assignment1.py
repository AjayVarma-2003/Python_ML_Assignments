import schedule
import time

def fun():
    print("Jay Ganesh ...")

def main():
    schedule.every(2).seconds.do(fun)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()