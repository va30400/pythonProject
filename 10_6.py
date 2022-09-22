
if __name__ == '__main__':
    info = marks = []
    for _ in range(int(input())):
        element = []
        name = input()
        score = float(input())
        element.append(name)
        element.append(score)
        marks.append(score)
        info.append(element)

# second lowest
    print (marks)
    marks = sorted(marks)
    secondLowest = marks[1]

    for i in info:
        if secondLowest in i:
            print (i[0])