class Vehicle:
    def start(self):
        print("Engine on and Vehicle sound...")
        
class Car(Vehicle):
    def start(self):
        print("Car engine on and Car sound...")

def main():
    obj = Car()
    
    obj.start()

if __name__ == "__main__":
    main()  