# traffic signal system using if elif

signal_color = input("Enter the signal color(red/yellow/green):")
color = signal_color.lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("GO!")
else:
    print("Invalid color.")
