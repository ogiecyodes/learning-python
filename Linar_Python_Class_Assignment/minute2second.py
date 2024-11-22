def minute_to_seconds(minutes=int)->str:
  seconds = minutes * 60
  return f'{seconds} seconds '
cal = minute_to_seconds(minutes=(int(input("Enter Minutes: "))))
print (cal)