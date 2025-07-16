import csv

attendance = [
    {"Name": "Ganesh", "Status": "Present"},
    {"Name": "Riya", "Status": "Absent"},
    {"Name": "Aman", "Status": "Present"},
    {"Name": "Sneha", "Status": "Present"}
]

with open("attendance.csv", "w", newline="") as file:
    fieldnames = ["Name", "Status"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for entry in attendance:
        writer.writerow(entry)

print("Attendance recorded.")
