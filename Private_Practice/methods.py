course = "python for beginners"
#the course variable is storing a string object
#when a function is part of an a string object it is referred to as method
print(course.upper())
print(course.find('b'))
print(course.replace("for" , "4"))
print("python " in course)
# Format method
txt = "the merch cost {:>4} pounds"
print(txt.format( 30))
txt = "the merch cost {price:.2f} pounds"
print(txt.format( price =30))
txt2 = " give me my {0} or you {1}"
print(txt2.format("money", "die"))
#removal of whitespace
print(txt2.strip())
#Split method, splits a string into a list
a= "Father, Son, Holyspirit"
print(a.split(","))
#Escape Characters
Q= "we\'re a \"chosen\" generation!"
print(Q)
print(Q.replace('"', ''))
w = " yes \\ no"
print(w)
e = "white\t black" #\b for backspace
print (e)
print(course.count("n"))