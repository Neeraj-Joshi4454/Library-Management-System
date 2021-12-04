class Libarary:

    def __init__(self,bookList):
        self.books = bookList

    def availableBooks(self):
        for i in self.books:
            print("*",i)

    def borrowBook(self,bookname):
        self.books.remove(bookname)
        print("Thank you!, You have been issued a book, Please keep it safe!")

    def returnBook(self,bookname):
        self.books.append(bookname)
        print("Thank you for choosing Pune Central Library, Visit again.")



class Student:
    
    def borrowB(self):
        bname = input("Enter the name of book You want to borrow: ")
        return bname

    def returnB(self):
        bname = input("Enter the name of book you want to return: ")
        return bname

if __name__ == "__main__":

    lib = Libarary(["python","Django","java","c++"])
    st = Student()

    # lib.availableBooks()

    welcometag = '''******Welcome to Pune Central Library******
    1)List of Available Books
    2)Borrow a Book
    3)Add or Return a Book
    4)Exit
    '''
    while(True):
        try:
            print(welcometag)
            ch = int(input("Enter your choice: "))
            if(ch == 1):
                lib.availableBooks()
            elif(ch == 2):
                lib.borrowBook(st.borrowB())
            elif(ch == 3):
                lib.returnBook(st.returnB())
            elif(ch == 4):
                print("Thank you for choosing Pune Central Library, Visit again.")
                break
            else:
                print("Invalid Choice")
        except Exception as e:
            print("invalid input, please Enter the valid input!")