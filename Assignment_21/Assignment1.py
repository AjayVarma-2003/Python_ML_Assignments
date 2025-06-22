import psutil

def DisplayProcesses():
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ['pid', 'name'])
        print(info)

def main():
    DisplayProcesses()

if __name__ == "__main__":
    main()