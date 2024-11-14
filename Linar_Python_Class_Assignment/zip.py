#use the zip() in built function to unvundle two lists
player_name = ["segun", "Ayo", "John", "BJ", "Ade"]
player_score = [100, 90, 80, 70, 50]
py = zip(player_name, player_score) # the zip function assigns values in list one to a corresponding value
for x, y in py :# use of for loop to iterate each pair out of assigned bracket
  print(f'{x} scored {y}')
#print(list(py))

