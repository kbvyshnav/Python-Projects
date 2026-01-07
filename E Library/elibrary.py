class Elibrary:
    def __init__(self):
        self.books=[]

    #adding method ➡️ used to add a new book

    def add(self,t,a):
        self.books.append({"title":t,"author":a,"status":"Available"})
        print("\n Book Added !\n")

    #view method ➡️ used to see all books

    def view(self):
        if not self.books:
            print("\nNo books yet!\n");return
        
        print("\n------ Book List ------\n")

        for i,b in enumerate(self.books,1):
            print(f"{i}. {b['title']} by {b['author']} - {b['status']}")
        print()

    #borrowing method ➡️ used o borrow a book

    def borrow(self,i):
        if 0<i<=len(self.books):
            if self.books[i-1]['status']=="Available":
                self.books[i-1]['status']="Borrowed"
                print("\nBook borrowed!\n")
            else:
                print("\nNot available!\n")
    
    #returning method - used to return a borrowed book

    def ret(self,i):
        if 0<i<=len(self.books):
            if self.books[i-1]['status']=="Borrowed":
                self.books[i-1]['status']="Available"
                print("\nBook returned !\n")
            else:
                print("\nInvalid return !\n")

    #seaching method ➡️ used to search a book by title ot author

    def search(self,k):
        print("\n----Search Results----")
        f=False
        for b in self.books:
            if k.lower() in b['title'].lower() or k.lower() in b['author'].lower():
                print(f"{b['title']} by {b['author']} - {b['status']}")
                f=True

        if not f: print("No match found!")
        print()

    #removing method ➡️ used to remove  book from library

    def rem(self,i):
        if 0<i<=len(self.books):
            print("\nRemoved :" , self.books[i-1]['title'] , "\n")
            self.books.pop(i-1)
    
    #statitics method ➡️ used to show library stats

    def stats(self):
        t=len(self.books)
        br=sum(b['status']=="Borrowed" for b in self.books)
        print(f"\n Total : {t} | Borrowed : {br} | Available : {t-br}\n")

lib=Elibrary()

while True:
    print("\n=== E-Library Menu ===\n")
    print("1. Add ➡️ Add new book")
    print("2. View ➡️ View all books")
    print("3. Borrow ➡️ Borrow a book")
    print("4. Return ➡️ Return a book")
    print("5. Search ➡️ Search a title/author")
    print("6. Remove ➡️ Remove a book")
    print("7. Statitics ➡️ Show library stats")
    print("8. Exit ➡️ Quit program\n")

    c=input("Choice : ")

    if c=="1": lib.add(input("Title :"), input("Author :"))
    elif c=="2" : lib.view()
    elif c=="3" : lib.borrow(int(input("Book No : ")))
    elif c=="4" : lib.ret(int(input("Book No : ")))
    elif c=="5" : lib.search(int(input("Keyword : ")))
    elif c=="6" : lib.rem(int(input("Book No : ")))
    elif c=="7" : lib.stats()
    elif c=="8" : break









        

            