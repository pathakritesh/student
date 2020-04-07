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


if __name__ == '__main__':
    add_student(student(1, 'eva1', 'john1', 'smith', 1993, 'in1@com'))
    add_student(student(2, 'eva2', 'john2', 'smith', 1993, 'in2@com'))
    add_student(student(3, 'eva3', 'ramesh', 'smith3', 1994, 'in3@com'))
    add_student(student(4, 'eva4', 'joginder', 'smith4', 1995, 'in4@com'))
    add_student(student(5, 'eva5', 'ramkishan', 'smith5', 1996, 'in5@com'))
    print_all_data()
    print('-------------')
    student1 = search_by_first_name('eva3')
    student1.display()
    student2 = search_by_rollno(1)
    student2.display()
    student3 = search_by_email('in4@com')
    student3.display()

    n = int(input('enter no. of students : '))
    print('sorting students details by roll no')
    for i in range(n):
        for j in range(i + 1, n):
            if st_list[i].rollno > st_list[j].rollno:
                tmp = st_list[i]
                st_list[i] = st_list[j]
                st_list[j] = tmp
    print('student information')
    print('rollno\tfirstname\t\tlastname\t\tfathername\t\tdob\t\temail')
    for i in range(n):
        st_list[i].display()
