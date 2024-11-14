class books:
  def __init__(self, title, author):
    self.title = title
    self.author = author
  def describe(self):
    print(f'{self.title} by {self.author}')
class fictionbooks(books):
  def __init__(self, title, author, genre):
    super().__init__(title, author)
    self.genre = genre
  def describe(self):
    super().describe()
    print(f'Genre: {self.genre}')
class nonfictionbooks(books):
  def __init__(self, title, author, subject):
    super().__init__(title, author)
    self.subject = subject
  def describe(self):
    super().describe()
    print (f' Genre :{self.subject}')
object = fictionbooks ("Round the World in 80 days", "James Fitzgerald", "fantasy")
object.describe()
object = nonfictionbooks("History of Rocks", "Mary Peters","Geology")
object.describe()