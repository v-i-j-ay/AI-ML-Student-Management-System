from ui import header, pause
from admin import admin_login



def add(cursor, connection):
    header("ADD STUDENT")

    print("\n--- Admin Verification Required ---")

    if not admin_login(cursor):
        print("Access denied. Returning to main menu.")
        pause()
        return

    # Student Details
    name = input("Enter Student Name: ").strip()
    rollno = input("Enter Roll Number: ").strip()
    marks = int(input("Enter Marks: "))
    attendance = int(input("Enter Attendance (%): "))
    projects = int(input("Enter Number of Projects: "))
    communication = input("Enter Communication (Poor/Average/Good): ").strip()
    internships = int(input("Enter Number of Internships: "))
    cgpa = float(input("Enter CGPA: "))
    skills = input("Enter Skills (comma separated): ").strip()
    business_idea = input("Enter Business Idea: ").strip()
    placement_status = input("Placement Status (Yes/No): ").strip()

    query = """
    INSERT INTO students
    (name, rollno, marks, attendance, projects,
     communication, internships, cgpa,
     skills, business_idea, placement_status)

    VALUES
    (%s, %s, %s, %s, %s,
     %s, %s, %s,
     %s, %s, %s)
    """

    cursor.execute(query, (
        name,
        rollno,
        marks,
        attendance,
        projects,
        communication,
        internships,
        cgpa,
        skills,
        business_idea,
        placement_status
    ))

    connection.commit()

    print("\nStudent record added successfully.")
    pause()

def view(cursor):
    header("VIEW STUDENTS")

    query = """
    SELECT
        name,
        rollno,
        marks,
        skills,
        business_idea,
        attendance,
        projects,
        communication,
        internships,
        cgpa,
        placement_status
    FROM students
    """

    cursor.execute(query)
    records = cursor.fetchall()

    if records:

        print("=" * 100)

        for row in records:

            print(f"""
Name              : {row[0]}
Roll Number       : {row[1]}
Marks             : {row[2]}
Skills            : {row[3]}
Business Idea     : {row[4]}
Attendance        : {row[5]}%
Projects          : {row[6]}
Communication     : {row[7]}
Internships       : {row[8]}
CGPA              : {row[9]}
Placement Status  : {row[10]}
""")

            print("-" * 100)

    else:
        print("No student records found.")

    pause()
    

def search(cursor):
    header("SEARCH STUDENT")

    rollno = input("Enter Roll Number: ").strip()

    query = """
    SELECT
        name,
        rollno,
        marks,
        skills,
        business_idea,
        attendance,
        projects,
        communication,
        internships,
        cgpa,
        placement_status
    FROM students
    WHERE rollno=%s
    """

    cursor.execute(query, (rollno,))
    record = cursor.fetchone()

    if record:

        print("\nStudent Record Found")
        print("=" * 100)

        print(f"""
Name              : {record[0]}
Roll Number       : {record[1]}
Marks             : {record[2]}
Skills            : {record[3]}
Business Idea     : {record[4]}
Attendance        : {record[5]}%
Projects          : {record[6]}
Communication     : {record[7]}
Internships       : {record[8]}
CGPA              : {record[9]}
Placement Status  : {record[10]}
""")

        print("=" * 100)

    else:
        print("\nStudent Record Not Found.")

    pause()

def delete(cursor, connection):
    header("DELETE STUDENT")

    print("\n--- Admin Verification Required ---")

    if not admin_login(cursor):
        print("Access denied. Returning to main menu.")
        pause()
        return

    rollno = input("Enter Roll Number to Delete: ").strip()

    # Check whether student exists
    query = """
    SELECT
        name,
        rollno,
        marks,
        skills,
        business_idea,
        attendance,
        projects,
        communication,
        internships,
        cgpa,
        placement_status
    FROM students
    WHERE rollno=%s
    """

    cursor.execute(query, (rollno,))
    record = cursor.fetchone()

    if not record:
        print("\nStudent not found.")
        pause()
        return

    print("\nStudent Details")
    print("-" * 60)

    print(f"Name              : {record[0]}")
    print(f"Roll Number       : {record[1]}")
    print(f"Marks             : {record[2]}")
    print(f"Skills            : {record[3]}")
    print(f"Business Idea     : {record[4]}")
    print(f"Attendance        : {record[5]}%")
    print(f"Projects          : {record[6]}")
    print(f"Communication     : {record[7]}")
    print(f"Internships       : {record[8]}")
    print(f"CGPA              : {record[9]}")
    print(f"Placement Status  : {record[10]}")

    choice = input("\nAre you sure you want to delete this student? (Y/N): ").strip().upper()

    if choice != "Y":
        print("\nDeletion cancelled.")
        pause()
        return

    delete_query = "DELETE FROM students WHERE rollno=%s"

    cursor.execute(delete_query, (rollno,))
    connection.commit()

    print("\nStudent record deleted successfully.")

    pause()

def update(cursor, connection):
    header("UPDATE STUDENT")

    print("\n--- Admin Verification Required ---")

    if not admin_login(cursor):
        print("Access denied. Returning to main menu.")
        pause()
        return

    rollno = input("Enter Roll Number to Update: ").strip()

    # Check whether student exists
    query = """
    SELECT
        name,
        rollno,
        marks,
        skills,
        business_idea,
        attendance,
        projects,
        communication,
        internships,
        cgpa,
        placement_status
    FROM students
    WHERE rollno=%s
    """

    cursor.execute(query, (rollno,))
    record = cursor.fetchone()

    if not record:
        print("\nStudent not found.")
        pause()
        return

    print("\nCurrent Student Details")
    print("-" * 60)
    print(f"Name              : {record[0]}")
    print(f"Marks             : {record[2]}")
    print(f"Skills            : {record[3]}")
    print(f"Business Idea     : {record[4]}")
    print(f"Attendance        : {record[5]}")
    print(f"Projects          : {record[6]}")
    print(f"Communication     : {record[7]}")
    print(f"Internships       : {record[8]}")
    print(f"CGPA              : {record[9]}")
    print(f"Placement Status  : {record[10]}")

    print("\nEnter New Details")

    name = input("Enter Student Name: ").strip()
    marks = int(input("Enter Marks: "))
    attendance = int(input("Enter Attendance (%): "))
    projects = int(input("Enter Number of Projects: "))
    communication = input("Enter Communication (Poor/Average/Good): ").strip()
    internships = int(input("Enter Number of Internships: "))
    cgpa = float(input("Enter CGPA: "))
    skills = input("Enter Skills (comma separated): ").strip()
    business_idea = input("Enter Business Idea: ").strip()
    placement_status = input("Placement Status (Yes/No): ").strip()

    update_query = """
    UPDATE students
    SET
        name=%s,
        marks=%s,
        skills=%s,
        business_idea=%s,
        attendance=%s,
        projects=%s,
        communication=%s,
        internships=%s,
        cgpa=%s,
        placement_status=%s
    WHERE rollno=%s
    """

    cursor.execute(update_query, (
        name,
        marks,
        skills,
        business_idea,
        attendance,
        projects,
        communication,
        internships,
        cgpa,
        placement_status,
        rollno
    ))

    connection.commit()

    print("\nStudent record updated successfully.")

    pause()