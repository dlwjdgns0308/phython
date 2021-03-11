absent = [2, 5] # 결석
no_book = [7] # 책을 두고옴
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("{0}, 빠따 맞자".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))