import os.path

file= os.path.isfile("input.txt")

if file:
    with open("input.txt") as f:
        line_count=1
        word_count = 0
        char_count=0
        for line in f:
            word_count=len(line.split(" "))
            char_count = len(line)
            print(f"Line {line_count} => words: {word_count},characters: {char_count}")
            line_count += 1
        print("\nTotal no of lines:", line_count)
else:
    print("file won't exist")