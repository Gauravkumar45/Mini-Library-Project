class Library:
    def __init__(self, list, name):
        self.name = name
        self.booksList = list
        self.lendDict = {}

    def dispalyBook(self):
        print(f"we have following books in our library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender - book database has been updated. You can take the book now")
        else:
            print(f"book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("book has been added to the book list")

    def returnBook(self):
        self.lendDict.pop(book)

if __name__ == '__main__':
    gaurav= Library(['python', 'let us c','c++ basics','algorithms by CLRS','harry potter'], "GauravBookStore")


while(True):
    print(f"welcome to the {gaurav.name} library, Enter your choice to continue")
    print("1. Display books")
    print("2. Lend a books")
    print("3. Add a books")
    print("4. Return a books")
    uesr_choice = input()
    if uesr_choice not in ['1','2','3','4']:
        print("please enter a valid option")
        continue

    else:
        uesr_choice = int(uesr_choice)

    if uesr_choice == 1:
        gaurav.dispalyBook()

    elif uesr_choice == 2:
        book = input("Enter the name of the book you want to lend:")
        user = input("Enter your name")
        gaurav.lendBook(user, book)

    elif uesr_choice == 3:
        book = input("Enter the name of the book you want to add:")
        gaurav.addBook(book)

    elif uesr_choice == 4:
        book = input("Enter the name of the book you want to return:")
        gaurav.returnBook(book)

    else:
        print("Not a valid option")

    print("press q to quit and c to continue")

    uesr_choice2 = ""
    while(uesr_choice2!= "c" and uesr_choice2!="q"):

        uesr_choice2 = input()
        if uesr_choice2 == "q":
             exit()

        elif uesr_choice2 == "c":
             continue







