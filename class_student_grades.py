from re import *
from statistics import *

grade_dict = {}


def is_numeric(input_value):
    value_regex = compile('[0-9]')
    if value_regex.match(input_value) is None:
        return False
    else:
        return True


def main_menu():
    will_exit = False
    choice = ''
    print('\tWelcome to Grade Central\n')
    print('\t[1] - Enter Grades')
    print('\t[2] - Remove Student')
    print('\t[3] - Student Average Grades')
    print('\t[4] - Exit\n')
    while not will_exit:
        choice = input('What would you like to do today? (Enter a number): ')
        choice_regex = compile('[0-9]')
        if not is_numeric(choice) or int(choice) < 1 or int(choice) > 4:
            print('Invalid choice entered. Please try again.\n')
        else:
            will_exit = True
    return int(choice)


def enter_grades():
    student_grade = 'None'
    student_name = input('Student Name: ')
    while not is_numeric(student_grade):
        student_grade = input('Enter a Numeric Grade: ')
    print('Adding Grade...')
    if student_name not in grade_dict:
        grade_dict[student_name] = [int(student_grade)]
    else:
        grade_dict[student_name].append(int(student_grade))


def remove_student():
    student_name = input('What student to remove? ')
    try:
        grade_dict.pop(student_name)
        print('Removing student...')
    except Exception as e:
        print('Student name not found.')


def average_grades():
    student_name = input("Which student's average should be displayed? ")
    try:
        print('Student', student_name, 'has an average score of', mean(grade_dict[student_name]))
    except Exception as e:
        print(e)
        print('Student name not found.')


def main():
    login_password = input('Enter admin password for access: ')
    while login_password != '999':
        print("Invalid password.")
        login_password = input('Enter admin password for access: ')
    menu_choice = 0
    while menu_choice != 4:
        menu_choice = main_menu()
        match menu_choice:
            case 1:
                enter_grades()
            case 2:
                remove_student()
            case 3:
                average_grades()
        print(grade_dict)
    print('Program terminated.')
