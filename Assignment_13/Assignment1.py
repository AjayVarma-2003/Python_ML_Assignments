class Bookstore:
    NoOfBooks = 0
    
    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        
    def Display(self):
        Bookstore.NoOfBooks += 1
        print(f"{self.Name} by {self.Author}. Number of books : {Bookstore.NoOfBooks}")

def main():
    Obj1 = Bookstore("Linux system programming", "Robert Love")
    Obj1.Display()
    
    Obj2 = Bookstore("C programming", "Dennis Ritchie")
    Obj2.Display()

if __name__ == "__main__":
    main()