# LR1 Group 4
# This program navigates through a book and prints the requested line.

book = input("Enter book name: ").lower()
lines = list()
filepath = f"books\\{book}.txt"

with open(filepath, 'r', encoding="utf-8") as f:
    for line in f:
        lines.append(line.strip())

print(f"{book.title()} has {len(lines)} lines.")

print("\nEnter 0 to quit.")
n = int(input("Enter line n: ")) - 1

while(n > -1 and n < len(lines)):
    print(lines[n] + '\n')
    n = int(input("Enter line n: ")) - 1
