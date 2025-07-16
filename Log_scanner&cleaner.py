import re

with open("logs.txt", "r") as file:
    lines = file.readlines()

count = 0
updated = []
for line in lines:
    if re.search(r"error|warning", line, re.IGNORECASE):
        count += 1
        updated.append(re.sub(r"error|warning", "ALERT", line, flags=re.IGNORECASE))
    else:
        updated.append(line)

with open("logs.txt", "w") as file:
    file.writelines(updated)

print("Scan complete.")
print("Total ALERTS:", count)
