class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"Book: {self.name}, Author: {self.author}, Pages: {self.pages}")


class Magazine(Publication):
     def __init__(self, name, chief_editor):
         super().__init__(name)
         self.chief_editor = chief_editor

     def  print_information(self):
        print(f"Magazine: {self.name}, Chief Editor: {self.chief_editor}")


# MAIN
mag = Magazine("Donald Duck", "Aki Hyppä")
book = Book("Compartment No. 6", "Rosa Liksom", 192)

mag.print_information()
book.print_information()