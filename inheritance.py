class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructer Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name -", self.last_name)
        print("Eye Color -", self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructer Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name -", self.last_name)
        print("Eye Color -", self.eye_color)
        print("Number of Toys -", self.number_of_toys)




billy_cyrus = Parent("Cyrus","blue")
print(billy_cyrus.last_name)

goose_cyrus = Child("Cyrus","black","90")
print(goose_cyrus.last_name)
print(goose_cyrus.number_of_toys)
goose_cyrus.show_info()