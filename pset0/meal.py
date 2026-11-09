#implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. 
# If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. 
# And assume that each meal’s time range is inclusive.

time = input("whats the time:")
hours , minutes = time.split(":")
hours = int(hours)
minutes = int(minutes)
time = hours + minutes / 60

if  7 <= time <= 8:
   print (" its breakfast time")
elif  12 <= time <= 13:
   print (" its lunch time ")
elif 18 <= time <= 19:
   print("its dinner time ")

