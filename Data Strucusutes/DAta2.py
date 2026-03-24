#Seb Ellis 2/19/2026 St paul schools
# Creates the classes with a dictionary
course_catalog = {
    "CS101": 'Intro to Programming',
    "MATH202": 'Calculus II',
    }
Student1 = (100, 'Alice Anderson')

registrations ={
    Student1: ["CS101", "MATH202"]

}

offered_courses = {"CS101", "MATH202"}
"""
Tuple- Added ID and name of student + shows registering. 
"""
def register_course(student_tuple, course_code):
    if course_code in offered_courses:
        registrations[student_tuple].append(course_code)
        print(f"Registered {student_tuple[1]} for {course_code}.")
    else:
        print(f"Error: {course_code} is not offered.")

register_course(Student1, course_code = "CS101")

registrations[Student1].append("CS101")
print(f"\nBefore cleaning: {registrations[Student1]}")
#Code duplicated

for student in registrations:

   registrations[student] = list(set(registrations[student]))

print(f"\nAfter cleaning':' {registrations[Student1]}" )



print("--- Course Registration Report ---")
for student_record, courses in registrations.items():
    student_id, student_name = student_record
    print(f"Student: {student_name} (ID: {student_id}")
    if not courses:
        print(" Not registered for any courses.")
    else:
        for course in courses:

            print(f" - {course}: {course_catalog.get(course, 'default''Unknown Course')}")
    print("-" * 30)