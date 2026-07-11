
# 🎓 Student Management System (Python + MySQL)


from database import connect_database
from student_operations import *
from ui import *
from ai_features import *
from ml_features import *
from analytics import *


try:
    connection, cursor = connect_database()
    print("MySQL Connected Successfully")

    while True:
        header("AI & ML STUDENT MANAGEMENT SYSTEM")

        print("""
=========== STUDENT MANAGEMENT ===========

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student

=============== AI FEATURES ==============

6. AI Resume Summary
7. AI Chatbot

============= ML FEATURES ================

8. ML Placement Prediction
9. ML Performance Prediction
10. ML Student Analytics

11. Exit
""")

        ch = input("Enter Option: ").strip()

        if ch == '1':
            add(cursor, connection)

        elif ch == '2':
            view(cursor)

        elif ch == '3':
            search(cursor)

        elif ch == '4':
            update(cursor, connection)

        elif ch == '5':
            delete(cursor, connection)

        elif ch == '6':
            ai_resume_summary(cursor)

        elif ch == '7':
            ai_chatbot()

        elif ch == '8':
            ml_placement_prediction(cursor)
        
        elif ch == '9':
            ml_performance_prediction(cursor) 
        
        elif ch == '10':
            analytics_dashboard(cursor)

        elif ch == '11':
            print("\nThank you for using AI & ML Student Management System.")
            break

        else:
            print("\nInvalid Option!")
            pause()
except Exception as e:
    print(e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySql connection closed")