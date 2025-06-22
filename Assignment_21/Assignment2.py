import psutil

def DisplayProcess(name):
    Result = {}
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == name:
            Result = proc.as_dict(attrs = ['pid', 'name'])
        print(Result)

def main():
    print("Enter the name of process : ")
    process = input()

    DisplayProcess(process)

if __name__ == "__main__":
    main()