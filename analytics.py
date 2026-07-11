import matplotlib.pyplot as plt
from ui import header, pause

def analytics_dashboard(cursor):

    header("ANALYTICS DASHBOARD")

    # ----------------------------
    # Dashboard Statistics
    # ----------------------------

    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM students WHERE placement_status='yes'")
    placed = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM students WHERE placement_status='no'")
    not_placed = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(marks) FROM students")
    avg_marks = cursor.fetchone()[0] or 0

    cursor.execute("SELECT AVG(attendance) FROM students")
    avg_attendance = cursor.fetchone()[0] or 0

    cursor.execute("SELECT AVG(cgpa) FROM students")
    avg_cgpa = cursor.fetchone()[0] or 0

    cursor.execute("SELECT MAX(marks) FROM students")
    highest_marks = cursor.fetchone()[0]

    cursor.execute("SELECT MIN(marks) FROM students")
    lowest_marks = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM students WHERE internships > 0")
    internship_students = cursor.fetchone()[0]

    placement_rate = 0

    if total_students > 0:
        placement_rate = (placed / total_students) * 100

    print("=" * 70)
    print("                 STUDENT ANALYTICS DASHBOARD")
    print("=" * 70)

    print(f"Total Students             : {total_students}")
    print(f"Placed Students            : {placed}")
    print(f"Not Placed Students        : {not_placed}")
    print(f"Placement Rate             : {placement_rate:.2f}%")

    print()

    print(f"Average Marks              : {avg_marks:.2f}")
    print(f"Average Attendance         : {avg_attendance:.2f}%")
    print(f"Average CGPA               : {avg_cgpa:.2f}")

    print()

    print(f"Highest Marks              : {highest_marks}")
    print(f"Lowest Marks               : {lowest_marks}")
    print(f"Students with Internship   : {internship_students}")

    print("=" * 70)

    pause()

    # ----------------------------
    # Placement Pie Chart
    # ----------------------------

    if total_students == 0:
        print("No student records available.")
        return

    plt.figure(figsize=(7,7))

    plt.pie(
        [placed, not_placed],
        labels=["Placed", "Not Placed"],
        autopct="%1.1f%%",
        startangle=90,
        explode=(0.08, 0),
        shadow=True
    )

    plt.title(
        "Student Placement Distribution",
        fontsize=16,
        fontweight="bold"
    )

    plt.legend(
        [
            f"Placed ({placed})",
            f"Not Placed ({not_placed})"
        ],
        loc="best"
    )

    plt.tight_layout()

    plt.show()
