print('''Welcome to student Data base
         1.Get user detail by roll number
         2.Get user detail by first name
         3.Get user detail by email address
         4.Delete user detail by roll number
         5.Show all user
         6.Update user detail by roll number
         7.Delete user detail by roll number
         8.Find user siblings by father name
         9.Sort user detail by last name
         10.Sort user detail by roll number
         11.Validate user inputs

         ''')

student1 = input(str("Enter the details: "))

if student1 == 'IN001':
    print(rahul)
elif student1 == 'rahul':
    print(rahul)
elif student1 == 'singh':
    print(rahul)
if student1 == 'IN002':
    print(dave)
elif student1 == 'dave':
    print(dave)
elif student1 == 'smith':
    print(dave)
if student1 == 'IN003':
    print(ava)
elif student1 == 'ava':
    print(ava)
elif student1 == 'smith':
    print(ava)

    rahul = {
        'first_name': 'rahul',
        'last_name': 'singh',
        'father_name': 'shyam singh',
        'date_of_birth': '1993',
        'email_address': 'rahul@in.com',
        'roll_number': 'IN001'}

    dave = {
        'first_name': 'dave',
        'last_name': 'smith',
        'father_name': 'john smith',
        'date_of_birth': '1990',
        'email_address': 'dave@in.com',
        'roll_number': 'IN002'}
    ava = {
        'first_name': 'ava',
        'last_name': 'smith',
        'father_name': 'john smith',
        'date_of_birth': '1992',
        'email_address': 'ava@in.com',
        'roll_number': 'IN003'}