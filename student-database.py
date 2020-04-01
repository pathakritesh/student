print('''Welcome to student Data base
         Press 1 to get user detail by roll number
         Press 2 to get user detail by first name
         Press 3 to get user detail by email address
         Press 4 to delete user detail by roll number
         Press 5 to show all user
         Press 6 to update user detail by roll number
         Press 7 to delete user detail by roll number
         Press 8 to find user siblings by father name
         Press 9 to sort user detail by last name
         Press 10 to sort user detail by roll number
         Press 11 to validate user inputs

         ''')
student1 = input(str('Enter your choice: '))

if student1 == '1':
    print(rahul)
elif student1 == '2':
    print(rahul)
elif student1 == '3':
    print(rahul)
    rahul = {
            'first_name': 'rahul',
            'last_name': 'singh',
            'father_name': 'shyam singh',
            'date_of_birth': '1993',
            'email_address': 'rahul@in.com',
            'roll_number': 'IN001'}