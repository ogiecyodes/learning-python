class Book():
  def __init__(self, title = "", author = "", status= "checked out"):
    self.title = title
    self.author = author
    self.status = status
  def input_book(self):
    self.author = input('Enter Author' )
    self.title = input("Enter Title: ")
  def display_info(self):
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")
    return self.status
  def check_out (self):
    if self.status == "available":
      print (f'You can check out {self.title} by {self.author}')
    else:
      self.status == "checked out"
      print("not available")
testing1 = Book()
testing1.input_book()
testing1.display_info()
testing1.check_out()
      