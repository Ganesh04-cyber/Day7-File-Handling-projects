from datetime import datetime

time=datetime.now().strftime("%Y-%M-%D %H-%M-%S")
with open("notes.txt","a") as file:
    file.write(f"{time}-User logged in")
    file.write(f"\n{time}-Profile updated")
    file.write(f"\n{time}-Uploaded assignment")
    file.write(f"\n{time}-Logged out")
