def main():
    fobj = open("Student.txt", "w")
    
    fobj.write("Ajay Varma" + "\n")
    fobj.write("HUI HUI" + "\n")
    fobj.write("Shakira" + "\n")
    fobj.write("BURI BURI" + "\n")
    fobj.write("Unknown" + "\n")

    fobj.close()

if __name__ == "__main__":
    main()