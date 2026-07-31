class Invalid_id(Exception):
    pass

class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
        self.books_taken = []

class Book:
    def __init__(self,name, flag):
        self.name = name
        self.flag = flag

    def show_books(self):
        return self.name

    def take_book(self,bk_name):
        if bk_name in self.name:
            if self.flag == True:
                stu.books_taken.append(bk_name)
                print(f"book {bk_name} taken by {stu.name}")
                for i in books:
                    if i.name == bk_name:
                        i.flag = False
            else:
                print("sorry! book is inavailable")
        else:
            print( "book name is incorrect!")
    def return_book(self):
        pass

students = {
    121 : Student(121,"sumanth"),
    122 : Student(122,"surender"),
    123 : Student(123,"chetak")
}

books = [
    Book("python",True),
    Book("sql", True),
    Book("html", True),
    Book("dsa", True),
    Book("java", True)
]



while True:
    try:
        num = int(input("enter u r id : "))
        flag = 1
        if num in students:
            stu = students[num]
            print(f"welcome to book store {stu.name}")
        else:
            print("student id not found")
            flag = 0
        
        if flag == 0:
            break
        else:
            print("1.Display books")
            print("2.Take book")
            print("3.return book")
            print("4.exit menu")
            
            choice = int(input("enter u r choice: "))
            
            if choice == 1:
                print("we have the books:")
                for i in books:
                    if i.flag == True:
                        print(i.show_books())
                    else:
                        continue
                print("\n")
            
            elif choice == 2:
                for j,i in enumerate(books,start=1):
                    if i.flag == True:
                        print(f"{j}. {i.show_books()}")
                    else:
                        continue
                bk_name = input("pls enter the book name :")
                for i in books:
                    if i.name == bk_name:
                        i.take_book(bk_name)
            
            elif choice == 3:
                pass
            
            elif choice ==4:
                print(f"thank you {stu.name}")
                break
    except Invalid_id as ii:
        print("ERROR : ",ii)