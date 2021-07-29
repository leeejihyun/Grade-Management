def getaverage(student):
    average = (student['Midterm'] + student['Final'])/2
    average = round(average,1)
    return average

def getgrade(student):
    average = student['Average']
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

def showhead():
    print("{:>10}\t{:^15}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\n".format("Student", "Name", "Midterm", "Final", "Average", "Grade"))
    print("-" * 100)

def showrecord(student):
    print("{:>10}\t{:^15}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\n".format(student['Student'], student['Name'], student['Midterm'], student['Final'], student['Average'], student['Grade']))

def find(stu_list, column, key):
    for student in stu_list:
        if student[column] == key:
            return student
    return False
    
def show(stu_list):
    stu_list.sort(key=lambda student : student['Average'], reverse=True) # 평균 점수를 기준으로 내림차순 정렬
    showhead()
    for student in stu_list:
        showrecord(student)
        
def search(stu_list):
    studentID = input("Student ID: ")
    if find(stu_list, 'Student', studentID):
        student = find(stu_list, 'Student', studentID)
        showhead()
        showrecord(student)
    else:
        print("NO SUCH PERSON.\n")

def changescore(stu_list):
    studentID = input("Student ID: ")
    if find(stu_list, 'Student', studentID):
        student = find(stu_list, 'Student', studentID)
        choice = input("Mid/Final? ")
        if (choice == "mid") | (choice == "final"):
            score = int(input("Input new score: "))
            if (0 <= score <= 100):
                showhead()
                showrecord(student)
                if choice == "mid":
                    student['Midterm'] = score
                else:
                    student['Final'] = score
                student['Average'] = getaverage(student)
                student['Grade'] = getgrade(student)
                print("Score changed.")
                showrecord(student)
            else:
                print()
        else:
            print()
    else:
        print("NO SUCH PERSON.\n")
            
def add(stu_list):
    student = {}
    studentID = input("Student ID: ")
    if not find(stu_list, 'Student', studentID):
        student['Student'] = studentID
        name = input("Name: ")
        student['Name'] = name
        mid = int(input("Midterm Score: "))
        student['Midterm'] = mid
        final = int(input("Final Score: "))
        student['Final'] = final
        student['Average'] = getaverage(student)
        student['Grade'] = getgrade(student)
        stu_list.append(student)
        print("Student added.\n")
    else:
        print("ALREADY EXISTS.\n")
    
def searchgrade(stu_list):
    grade = input("Grade to search: ")
    if grade in "ABCDF":
        if find(stu_list, 'Grade', grade):
            showhead()
            for student in stu_list:
                if student['Grade'] == grade:
                    showrecord(student)
        else:
            print("NO RESULTS.\n")
    else:
        print()

def remove(stu_list):
    if stu_list:
        studentID = input("Student ID: ")
        if find(stu_list, 'Student', studentID):
            student = find(stu_list, 'Student', studentID)
            stu_list.remove(student)
            print("Student removed.\n")
        else:
            print("NO SUCH PERSON.\n")
    else:
        print("List is empty.\n")
    
def quit(stu_list):
    save = input("Save data?[yes/no] ")
    if save == "yes":
        filename = input("File name: ")
        with open(filename, 'w') as f:
            for student in stu_list:
                line = '\t'.join(list(map(str, student.values())))
                f.write(line + '\n')
                
def menu():
    import sys

    try:
        file_name = sys.argv[1]
    except:
        file_name = 'students.txt'
    
    with open(file_name, 'r') as f:
        stu_list = []
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip().split('\t')
            student = {}
            student['Student'] = line[0]
            student['Name'] = line[1]
            student['Midterm'] = int(line[2])
            student['Final'] = int(line[3])
            student['Average'] = getaverage(student)
            student['Grade'] = getgrade(student)
            stu_list.append(student)

    show(stu_list)
    
    print('''
    show: 전체 학생 정보 출력
    search: 특정 학생 검색
    changescore: 점수 수정
    add: 학생 추가
    searchgrade: 학점으로 검색
    remove: 특정 학생 삭제
    quit: 종료
    ''')
    
    while True:        
        cmd = input("# ")

        if cmd.upper() == "SHOW":
            show(stu_list)
        elif cmd.upper() == "SEARCH":
            search(stu_list)
        elif cmd.upper() == "CHANGESCORE":
            changescore(stu_list)
        elif cmd.upper() == "ADD":
            add(stu_list)
        elif cmd.upper() == "SEARCHGRADE":
            searchgrade(stu_list)
        elif cmd.upper() == "REMOVE":
            remove(stu_list)
        elif cmd.upper() == "QUIT":
            quit(stu_list)
            return False
                
menu()