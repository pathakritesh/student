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
    rerun()


def search_by_rollno(roll_no):
    get_list1 = get_all_student()
    for item in get_list1:
        if item.rollno == roll_no:
            return item
    rerun()


def search_by_email(email_id):
    get_list1 = get_all_student()
    for item in get_list1:
        if item.email == email_id:
            return item
    rerun()


def del_by_email(email_id):
    get_list1 = get_all_student()
    for item in get_list1:
        if item.email == email_id:
            return get_list1.remove(item)
    rerun()


def del_by_rollno(roll_no):
    get_list1 = get_all_student()
    for item in get_list1:
        if item.rollno == roll_no:
            return get_list1.remove(item)
    rerun()


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
    rollno = str(input('enter rollno: '))
    firstname = str(input('enter firstname: '))
    lastname = str(input('enter lastname: '))
    fathername = str(input('enter fathername: '))
    dob = str(input('enter dob: '))
    email = str(input('enter email: '))
    iserror = False

    if len(rollno) > 8:
        print('invalid rollno character more than 8')
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
        print('invalid dob character more than 8 digit')
        iserror = True

    if len(email) > 250:
        print('invalid email')
        iserror = True

    if iserror == False:
        add_student(student(rollno, firstname, lastname, fathername, dob, email))


def again():
    run_again = input("""enter 'y' for run again
    the application and 'n' for quit: """)
    if run_again.lower() == 'y':
        rerun()

    elif run_again.lower() == 'n':
        print('See you later.')
    else:
        again()


if __name__ == '__main__':
    add_student(student('1', 'eva1', 'john1', 'smith', '1993', 'in1@com'))
    add_student(student('2', 'eva2', 'john2', 'smith', '1993', 'in2@com'))
    add_student(student('3', 'eva3', 'ramesh', 'smith3', '1994', 'in3@com'))
    add_student(student('4', 'eva4', 'joginder', 'smith4', '1995', 'in4@com'))
    add_student(student('5', 'eva5', 'ramkishan', 'smith5', '1996', 'in5@com'))



    def rerun():
        x = str(input("""enter number to get details below 
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

        if x == '1':
            m = input('enter first name: ')
            student1 = search_by_first_name(m)
            student1.display()

        elif x == '2':
            n = input('enter rollno: ')
            student2 = search_by_rollno(n)
            student2.display()
        elif x == '3':
            p = input('enter email')
            student3 = search_by_email(p)
            student3.display()
        elif x == '4':
            print_all_data()
        elif x == '5':
            f = input('enter rollno')
            del_by_rollno(f)
        elif x == '6':
            g = input('enter email')
            del_by_email(g)
        elif x == '7':
            user_input()

        elif x == '8':
            n = len(st_list)
            for i in range(n):
                for j in range(i + 1, n):
                    if st_list[i].rollno > st_list[j].rollno:
                        tmp = st_list[i]
                        st_list[i] = st_list[j]
                        st_list[j] = tmp
            for i in range(n):
                st_list[i].display()

        elif x == '9':
            n = len(st_list)
            for i in range(n):
                for j in range(i + 1, n):
                    if st_list[i].lastname > st_list[j].lastname:
                        tmp = st_list[i]
                        st_list[i] = st_list[j]
                        st_list[j] = tmp
            for i in range(n):
                st_list[i].display()

        elif x == '10':
            lib1 = get_siblings()
            for Key in lib1:
                print('father name', Key)
                for item in lib1[Key]:
                    print('student first name', item.firstname)

        else:
            print('Wrong Entry Please enter within limit')
        again()
    rerun()