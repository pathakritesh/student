class student:
    def __init__(self, rollno, firstname, lastname, fathername, dob, email):
        self.rollno = rollno
        self.firstname = firstname
        self.lastname = lastname
        self.fathername = fathername
        self.dob = dob
        self.email = email

    def display(self):
        print(self.rollno, end='\t\t')
        print(self.firstname, end='\t\t')
        print(self.lastname, end='\t\t')
        print(self.fathername, end='\t\t')
        print(self.dob, end='\t\t')
        print(self.email)


st_list = []


def add_student(student):
    st_list.append(student)


def get_all_student():
    return st_list


def print_all_data():
    local_std_lst = get_all_student()
    for item in local_std_lst:
        item.display()


def search_by_first_name(first_name):
    get_list1 = get_all_student()
    for item in get_list1:
        if item.firstname == first_name:
            return item


def search_by_rollno(roll_no):
    get_list1 = get_all_student()
    for item in get_list1:
        if item.rollno == roll_no:
            return item


def search_by_email(email_id):
    get_list1 = get_all_student()
    for item in get_list1:
        if item.email == email_id:
            return item


def del_by_email(email_id):
    get_list1 = get_all_student()
    for item in get_list1:
        if item.email == email_id:
            return get_list1.remove(item)


def del_by_rollno(roll_no):
    get_list1 = get_all_student()
    for item in get_list1:
        if item.rollno == roll_no:
            return get_list1.remove(item)


def get_siblings():
    lib1 = {}
    lib2 = {}
    for item in st_list:
        if item.fathername not in lib1:
            list1 = [item]
            lib1[item.fathername] = list1
        else:
            lib1[item.fathername].append(item)
    for mapKey in lib1:
        if len(lib1[mapKey]) > 1:
            lib2[mapKey] = lib1[mapKey]
    return lib2


def user_input():
    rollno = input('enter rollno: ')
    firstname = input('enter firstname: ')
    lastname = input('enter lastname: ')
    fathername = input('enter fathername: ')
    dob = input('enter dob: ')
    email = input('enter email: ')
    iserror = False

    if len(rollno) > 8:
        print('invalid rollno ')
        iserror = True

    if len(firstname) > 50:
        print('invalid firstname ')
        iserror = True

    if len(lastname) > 50:
        print('invalid lastname')
        iserror = True

    if len(fathername) > 100:
        print('invalid fathername')
        iserror = True

    if len(dob) > 8:
        print('invalid dob')
        iserror = True

    if len(email) > 250:
        print('invalid email')
        iserror = True

    if iserror == False:
        add_student(student(rollno, firstname, lastname, fathername, dob, email))


if __name__ == '__main__':
    add_student(student(1, 'eva1', 'john1', 'smith', 1993, 'in1@com'))
    add_student(student(2, 'eva2', 'john2', 'smith', 1993, 'in2@com'))
    add_student(student(3, 'eva3', 'ramesh', 'smith3', 1994, 'in3@com'))
    add_student(student(4, 'eva4', 'joginder', 'smith4', 1995, 'in4@com'))
    add_student(student(5, 'eva5', 'ramkishan', 'smith5', 1996, 'in5@com'))
    x = int(input("""enter number to get details below 
    1. get user by first name     
    2. get user details by roll number    
    3. get user by email               
    4. show all user
    5. delete user by roll number      
    6. delete user by email address    
    7. validate user inputs 
    8. sort details by student last name   
    9. sort student by roll number
    10. find brother if they in same collage 
    11. update user information by roll number 
    
    Enter Number to Get Details: """))

    if x== 1:
        student1 = search_by_first_name('eva3')
        student1.display()
    if x== 2:
        student2 = search_by_rollno(1)
        student2.display()
    if x== 3:
        student3 = search_by_email('in4@com')
        student3.display()
    if x == 4:
        print_all_data()
    if x == 5:
        del_by_rollno(2)
    if x == 6:
        del_by_email('in1@com')
    if x == 7:
        user_input()

    if x == 8:
        n = len(st_list)
        for i in range(n):
            for j in range(i + 1, n):
                if st_list[i].rollno > st_list[j].rollno:
                    tmp = st_list[i]
                    st_list[i] = st_list[j]
                    st_list[j] = tmp
        for i in range(n):
            st_list[i].display()

    if x == 9:
        n = len(st_list)
        for i in range(n):
            for j in range(i + 1, n):
                if st_list[i].lastname > st_list[j].lastname:
                    tmp = st_list[i]
                    st_list[i] = st_list[j]
                    st_list[j] = tmp
        for i in range(n):
            st_list[i].display()

    if x == 10:
        lib1 = get_siblings()
        for Key in lib1:
            print('father name', Key)
            for item in lib1[Key]:
                print('student first name', item.firstname)