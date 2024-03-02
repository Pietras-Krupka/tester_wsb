with open("C:\\Users\\User\\tester-wsb\\tester-wsb\\my_file.txt", 'r') as f:
    lines = f.read()
    print(lines)
    print(lines.split())

    for i in lines:
        print(i)