class Library:
    def __init__(self, bookname):
        self.books = bookname

    def displaybooks(self):
        if self.books == []:
            print("--No books available in Library At the moment!--")
        else:
            print("The books available in our library are: ")
            for book in self.books:
                print("--> "+ book )

    def requestbook(self, nameofbooktorequest):
        if nameofbooktorequest in self.books:
            print(f"'{nameofbooktorequest}' book has been issued... Thanks for Choosing Our Library!")
            self.books.remove(nameofbooktorequest)
        else:
            print(f"'{nameofbooktorequest}' book is not available! Please try later...")

    def returnbook(self, nameofbooktoreturn):  
        if nameofbooktoreturn in self.books:
            self.books.append(nameofbooktoreturn)
            print(f"Thanks for returning '{nameofbooktoreturn}' book... Hope you enjoyed it!")
        else:
            print(f"Thanks for donating '{nameofbooktoreturn}' book... Have a good day!")
            self.books.append(nameofbooktoreturn)


class Student:
    def requestbook(self):
        self.book = input("Enter the name of Book to Request: ")
        return self.book

    def returnbook(self):
        self.book = input("Enter the name of Book to Add/Return: ")
        return self.book

nexusLibrary = Library(["python","java","html","css"]) 
student = Student()

welcomemsg = '''=====Welcome to Nexus Library=====
    Please Choose an Option:
    1) List of Books Available
    2) Request a Book
    3) Add/Return a Book
    4) Exit the Library'''

while True:
    print(welcomemsg)
    userinput = int(input("Enter Your Option: "))
    if userinput == 1:
        nexusLibrary.displaybooks()
    elif userinput == 2: 
        nexusLibrary.requestbook(student.requestbook())
    elif userinput == 3:
        nexusLibrary.returnbook(student.returnbook())
    elif userinput == 4:
        print("Thanks for choosing Nexus Library... Hope you had a nice time with us!")
        exit()
    else:
        print("Invalid Input")

