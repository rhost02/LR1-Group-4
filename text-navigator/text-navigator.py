# This program navigates through a book and prints the specified instance of the inputted text.

book = input("Enter book name: ").lower()
search_lines = list()
filepath = f"LR1-Group-4\\text-navigator\\books\\{book}.txt"
occur = dict()

print("Enter quit to stop search.")
while True:
    text = input("Search: ").lower()
    if text == "quit":
        break
    search_lines.append(text)

print("Instance in line:", end=" ")
with open(filepath, 'r', encoding="utf-8") as f:
    for n, line in enumerate(f):
        for foo in search_lines:
            if foo in line.lower():
                _ = occur.setdefault(n, line.strip())
                print(n, end=', ')

print("\nEnter 0 to quit.")
line_n = int(input("Enter line n: ")) 

while(line_n > 0) and line_n in occur.keys():
    print(occur[line_n], '\n')
    line_n = int(input("Enter line n: ")) 