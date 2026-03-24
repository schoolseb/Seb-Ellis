course_catalog = {
"CS101": "Intro to Programming",
"MATH202": "Calculus II", }
Student1 = (100, "Alice Anderson")
registrations = { Student1: ["CS101", "MATH202"] }
offered_courses = {"CS101", "MATH202"}
def register_course(student_tuple, course_code):
    if course_code in offered_courses: # Make sure the student exists in the registrations dictionary
        if [student_tuple] not in registrations:
            registrations[student_tuple] = []
        registrations[student_tuple].append(course_code)
        print(f"Registered {student_tuple[1]} for {course_code}.")
    else:
        print(f"Error: {course_code} is not offered.")

        register_course(Student1, "CS101")
        register_course(Student1, "MATH202")
print(registrations)
