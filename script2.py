
# 1. Tuple: Immutable student info (ID, Name)
# -------------------------
student1 = (101, "Alice")
student2 = (102, "Bob")
student3 = (103, "Charlie")

# -------------------------
# 2. List: Mutable list of courses for each student
# -------------------------
courses_student1 = ["Math", "Physics"]
courses_student2 = ["Biology", "Chemistry"]
courses_student3 = ["History", "Math"]

# -------------------------
# 3. Set: Unique skills (no duplicates allowed)
# -------------------------
skills_student1 = {"Python", "Data Analysis", "Python"}  # Duplicate "Python" will be removed
skills_student2 = {"Biology Research", "Lab Work"}
skills_student3 = {"Writing", "Public Speaking", "Writing"}  # Duplicate removed

# -------------------------
# 4. Dictionary: Mapping student tuple to their courses and skills
# -------------------------
students_data = {
    student1: {"courses": courses_student1, "skills": skills_student1},
    student2: {"courses": courses_student2, "skills": skills_student2},
    student3: {"courses": courses_student3, "skills": skills_student3},
}

# -------------------------
# Display all student data
# -------------------------
print("=== Student Management System ===")
for student, details in students_data.items():
    student_id, name = student  # unpack tuple
    print(f"\nID: {student_id}, Name: {name}")
    print(f"Courses: {', '.join(details['courses'])}")
    print(f"Skills: {', '.join(details['skills'])}")

# -------------------------
# Example operations
# -------------------------

# Add a new course to Alice's list
students_data[student1]["courses"].append("Computer Science")

# Add a new skill to Bob's set
students_data[student2]["skills"].add("Microscopy")

# Remove a course from Charlie
if "Math" in students_data[student3]["courses"]:
    students_data[student3]["courses"].remove("Math")

print("\n=== Updated Data ===")
for student, details in students_data.items():
    student_id, name = student
    print(f"\nID: {student_id}, Name: {name}")
    print(f"Courses: {', '.join(details['courses'])}")
    print(f"Skills: {', '.join(details['skills'])}")


