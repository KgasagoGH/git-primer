from fatetime import datetime

name = input("What is your name")
hour = datetime.now().time().hour
greeting = "Good morning" if 4 <= hour < else "Good afternoon" if 12 <= hour < 16 else "Good night"
print(f"{greeting}",{name}!)
