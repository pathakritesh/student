class student:
    def __init__(self, rollno, firstname, lastname, email, dob, fathername):
        self.rollno = rollno
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.dob = dob
        self.fathername = fathername

    def display(self):
        print(self, rollno, end='\t\t')
        print(self, firstname, end='\t\t')
        print(self, lastname, end='\t\t')
        print(self, email, end='\t\t')
        print(self, dob, end='\t\t')
        print(self, fathername)


st = list()
n = int(input('enter no. of students : '))
print('students details entry...')
for i in range(n):
    print('student : ', i + 1)
    rollno = input('\t rollno : ')
    firstname = input('\t firstname : ')
    lastname = input('\t lastname : ')
    email = input('\t email : ')
    dob = input('\t dob : ')
    fathername = input('\t fathername : ')
    st.append(student(rollno, firstname, lastname, email, dob, fathername))

for i in range(n):
    for j in range(i + 1, n):
        if (st[i].rollno > st[j].rollno):
            tmp = st[i]
            st[i] = st[j]
            st[j] = tmp

print('student information')
print('rollno\t\tfirstname\t\tlastname\t\temail\t\tdob\t\tfathername')
for i in range(n):
    st[i].display()