day = input()

weekWorkdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

if day in weekWorkdays:
    print("Working day")
elif day in weekend:
    print("Weekend")
else:
    print("Error")