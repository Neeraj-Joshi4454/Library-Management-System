

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
    def libMaintanance():

        def addbooks():
           i = int(input("Enter how many books you want to add: "))
           bks = []
           while(i>0):
                j = input(f"Enter the name of book whose number is {i}")
                bks.append(j)
                i -= 1 
           return bks              



        greet = '''******Welcome to Pune Central Library Maintainance Portal******
        1)Add Books
        '''
        while(True):
            print(greet)
            x = int(input("Enter your choice: "))

            if(x == 1):
              returnbks = addbooks()
              return returnbks
            else:
                break
    
    
greetmsg = '''******Welcome to Pune Central Library******'''
print(greetmsg)   
ans = input("There is a need of maintainance? :  (please type y or n)")

if(ans == 'y'):
    def withmaintainance():
        returnbks = libMaintanance()
        lib = Libarary(returnbks)
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
    withmaintainance()
        
else:
    def withoutMaintainance():
        lib = Libarary(["python","java","c++","machine learning"])
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
    
    withoutMaintainance()
            