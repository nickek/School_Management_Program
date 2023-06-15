import sqlite3

# ===========================
# Assignment 3 - Ek
# ===========================

# Connect to the database
conn = sqlite3.connect('assignment3.db')
cursor = conn.cursor()

# ===========================
# Functions
# ===========================


# Function to print all students
def print_all_students():
    query = 'SELECT * FROM student'
    cursor.execute(query)
    rows = cursor.fetchall()

    print('Students:\n'
          '| ID |  First  |  Last  |  Exp | Major |  Email |')
    for row in rows:
        print(row)
    print('\n')


# Function to print all instructors
def print_all_instructors():
    query = 'SELECT * FROM instructor'
    cursor.execute(query)
    rows = cursor.fetchall()

    print('Instructors:\n'
          '| ID |  First  |   Last   |   Title  |  Hired  | Department | Email |')
    for row in rows:
        print(row)
    print('\n')


# Function to print all admins
def print_all_admins():
    query = 'SELECT * FROM admin'
    cursor.execute(query)
    rows = cursor.fetchall()

    print('Admins:\n'
          '| ID |   First   |   Last   |   Title   |   Office   |   Email   |')
    for row in rows:
        print(row)
    print('\n')


# Function to print all records from the "course" table
def print_all_courses():
    query = 'SELECT * FROM COURSE'
    cursor.execute(query)
    rows = cursor.fetchall()

    print('Courses:\n'
          '| CRN | Subject | Department | Time | Day | Semester | Year | Credit |')
    for row in rows:
        print(row)
    print('\n')


# Search functions
def search_student():
    username = input('Who do you want to search: ')
    query = ''' 
            SELECT * FROM student WHERE name = "{}"    
            '''.format(username)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print('\n')


def search_instructor():
    username = input('Who do you want to search: ')
    query = ''' 
            SELECT * FROM instructor WHERE name = "{}"    
            '''.format(username)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print('\n')


def search_admin():
    username = input('Who do you want to search: ')
    query = ''' 
            SELECT * FROM admin WHERE name = "{}"
            '''.format(username)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print('\n')


def search_course():
    crn_in = input('Please enter CRN of course: ')
    select_query = '''
                   SELECT * FROM COURSE WHERE CRN = "{}"
                   '''.format(crn_in)
    cursor.execute(select_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        instructor_query = '''
                           SELECT * FROM instructor WHERE dept = "{}"
                           '''.format(row[2])
        cursor.execute(instructor_query)
        rows2 = cursor.fetchall()
        for row2 in rows2:
            print(row2)

    print('\n')


def insert_student():
    id_in = int(input('Please enter WIT ID: '))
    name_in = input('Please enter Name: ')
    surname_in = input('Please enter Surname: ')
    grad_year_in = int(input('Please enter Expected Graduation Year: '))
    major_in = input('Please enter Major: ')
    email_in = input('Please enter Email: ')
    cursor.execute(''' INSERT INTO student VALUES (?,?,?,?,?,?)'''
                   , (id_in, name_in, surname_in, grad_year_in, major_in, email_in))
    conn.commit()


def insert_instructor():
    id_in = int(input('Please enter WIT ID: '))
    name_in = input('Please enter Name: ')
    surname_in = input('Please enter Surname: ')
    title_in = input('Please enter Title: ')
    hire_year_in = int(input('Please enter Hire Year: '))
    department_in = input('Please enter Department: ')
    email_in = input('Please enter Email: ')
    cursor.execute(''' INSERT INTO instructor VALUES (?,?,?,?,?,?,?)'''
                   , (id_in, name_in, surname_in, title_in, hire_year_in, department_in, email_in))
    conn.commit()


def insert_admin():
    id_in = int(input('Please enter WIT ID: '))
    name_in = input('Please enter Name: ')
    surname_in = input('Please enter Surname: ')
    title_in = input('Please enter Title: ')
    office_in = input('Please enter Office: ')
    email_in = input('Please enter Email: ')
    cursor.execute(''' INSERT INTO admin VALUES (?,?,?,?,?,?)'''
                   , (id_in, name_in, surname_in, title_in, office_in, email_in))
    conn.commit()


def remove_instructor():
    name_in = input('Please enter the name of the instructor you would like to remove: ')
    select_query = '''
                    SELECT * FROM instructor WHERE name = ?
                   '''
    cursor.execute(select_query, (name_in,))
    existing_user = cursor.fetchone()
    if existing_user:
        delete_query = '''
                        DELETE FROM instructor WHERE name = ?
                       '''
        cursor.execute(delete_query, (name_in,))
        conn.commit()
        print(name_in, ' Has been successfully deleted!')
    else:
        print(name_in, 'Does not exist')


def update_admin():
    name_in = input("Who are you editing: ")
    new_title = input("Input new title: ")
    select_query = 'UPDATE admin SET title = "{}" WHERE name ="{}"'.format(new_title, name_in)
    cursor.execute(select_query)
    conn.commit()
    print(name_in, ' Successfully updated to ', new_title)

# ===========================
# Main program loop
# ===========================


# Adding 5 courses in database
cursor.execute('''DROP TABLE IF EXISTS COURSE''')
cursor.execute('''CREATE TABLE IF NOT EXISTS COURSE (
    CRN INTEGER,
    SUBJECT TEXT,
    DEPARTMENT TEXT,
    TIME TEXT,
    DAYS TEXT,
    SEMESTER TEXT,
    YEAR INTEGER,
    CREDIT INTEGER
)''')
# Insert the values into the COURSE table
cursor.executemany('''INSERT INTO COURSE VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', [
    ('50001', 'Analog Circuits', 'BSEE', '8-9', 'MWF', 'Spring/Fall', '1', '4'),
    ('50002', 'IO Physiology', 'HUSS', '10-11', 'TT', 'Spring/Fall', '1', '4'),
    ('50003', 'Intro to Code', 'BSCO', '10-11', 'MWF', 'Spring/Fall', '1', '4'),
    ('50004', 'Machine Learning', 'BSME', '1-3', 'MF', 'Fall', '2', '4'),
    ('50005', 'Calculus', 'BCOS', '8-10', 'MWF', 'Spring', '3', '4')
])
# Commit the changes and close the connection
conn.commit()


while True:

    print('Welcome user to Nicks Database Management Application!\n'
          '\n'
          ' Please select a function:\n'
          '[1] - Search\n'
          '[2] - Insert\n'
          '[3] - Print\n'
          '[4] - Delete\n'
          '[5] - Edit\n'
          '[6] - Exit\n')

    option = int(input(''))

    if option == 1:
        while True:
            print('Who do you want to search:\n'
                  '[1] - Students\n'
                  '[2] - Instructors\n'
                  '[3] - Admins\n'
                  '[4] - Courses\n'
                  '[5] - Exit\n')
            option1 = int(input(''))
            if option1 == 1:
                search_student()
            elif option1 == 2:
                search_instructor()
            elif option1 == 3:
                search_admin()
            elif option1 == 4:
                search_course()
            elif option1 == 5:
                break
            else:
                print('Invalid! Try again')
    elif option == 2:
        while True:
            print_all_students()
            print_all_instructors()
            print_all_admins()
            print('Please select who you would like to insert:\n'
                  '[1] - Students\n'
                  '[2] - Instructors\n'
                  '[3] - Admins\n'
                  '[4] - Exit\n')
            option2 = int(input(''))
            if option2 == 1:
                insert_student()
            elif option2 == 2:
                insert_instructor()
            elif option2 == 3:
                insert_admin()
            elif option2 == 4:
                break
            else:
                print('Invalid! Try again')
    elif option == 3:
        while True:
            print('Please select what to print:\n'
                  '[1] - Students\n'
                  '[2] - Instructors\n'
                  '[3] - Admins\n'
                  '[4] - All\n'
                  '[5] - Courses\n'
                  '[6] - Exit\n')
            option3 = int(input(''))
            if option3 == 1:
                print_all_students()
            elif option3 == 2:
                print_all_instructors()
            elif option3 == 3:
                print_all_admins()
            elif option3 == 4:
                print_all_students()
                print_all_instructors()
                print_all_admins()
            elif option3 == 5:
                print_all_courses()
            elif option3 == 6:
                break
            else:
                print('Invalid! Try again')

    elif option == 4:
        while True:
            print_all_students()
            print_all_instructors()
            print_all_admins()
            print('Please select who you would like to delete:\n'
                  '[1] - Students\n'
                  '[2] - Instructors\n'
                  '[3] - Admins\n'
                  '[4] - Exit\n')
            option4 = int(input(''))
            if option4 == 1:
                print('working on')
            elif option4 == 2:
                remove_instructor()
            elif option4 == 3:
                print('working on')
            elif option4 == 4:
                break
            else:
                print('Invalid! Try again')

    elif option == 5:
        update_admin()
    elif option == 6:
        break

    else:
        print('Invalid! Try again')
