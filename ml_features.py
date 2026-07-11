import joblib
import pandas as pd
from ui import header, pause

placement_model = joblib.load("placement_model.pkl")
performance_model = joblib.load("performance_model.pkl")


def ml_placement_prediction(cursor):
    header("ML PLACEMENT ANALYSIS")

    rollno = input("Enter Roll Number: ").strip()

    query = """
    SELECT
        name,
        marks,
        attendance,
        projects,
        communication,
        internships,
        cgpa
    FROM students
    WHERE rollno=%s
    """

    cursor.execute(query, (rollno,))
    record = cursor.fetchone()

    if not record:
        print("\nStudent not found!")
        pause()
        return

    # Student Data
    name = record[0]
    marks = record[1]
    attendance = record[2]
    projects = record[3]
    communication = record[4]
    internships = record[5]
    cgpa = record[6]

    # Communication Mapping
    communication_map = {
        "Poor": 1,
        "Average": 2,
        "Good": 3,
        "Very Good": 4,
        "Excellent": 5
    }

    communication_score = communication_map.get(
        str(communication).title(),
        3
    )

    # ML Features
    features = pd.DataFrame([[
        marks,
        attendance,
        projects,
        communication_score,
        internships,
        cgpa
    ]], columns=[
        "marks",
        "attendance",
        "projects",
        "communication",
        "internships",
        "cgpa"
    ])

    # Prediction
    prediction = placement_model.predict(features)[0]

    # Probability
    probability = placement_model.predict_proba(features)

    confidence = probability[0][prediction] * 100

    score = int(confidence)

    filled = score // 5
    empty = 20 - filled

    progress_bar = "█" * filled + "░" * empty

    # Status
    if score >= 90:
        overall_status = "EXCELLENT"

    elif score >= 75:
        overall_status = "GOOD"

    elif score >= 60:
        overall_status = "AVERAGE"

    else:
        overall_status = "NEEDS IMPROVEMENT"

    # Strengths
    strengths = []

    if marks >= 85:
        strengths.append("Excellent Academic Performance")

    if attendance >= 90:
        strengths.append("Excellent Attendance")

    if projects >= 3:
        strengths.append("Strong Project Portfolio")

    if internships >= 1:
        strengths.append("Industry Experience")

    if cgpa >= 8:
        strengths.append("Excellent CGPA")

    # Weaknesses
    weaknesses = []

    if marks < 80:
        weaknesses.append("Improve Academic Performance")

    if attendance < 90:
        weaknesses.append("Improve Attendance")

    if projects < 3:
        weaknesses.append("Build More Projects")

    if internships < 1:
        weaknesses.append("Complete Internship")

    if communication_score < 4:
        weaknesses.append("Improve Communication Skills")

    if cgpa < 8:
        weaknesses.append("Increase CGPA")

    # Company Eligibility
    companies = []

    if prediction == 1:

        if cgpa >= 8.5:
            companies.append("Product Companies")
            companies.append("Service Companies")
            companies.append("Startups")

        elif cgpa >= 7:
            companies.append("Service Companies")
            companies.append("Startups")

        else:
            companies.append("Startups")

    else:
        companies.append("Need More Preparation")

    # Salary Estimation
    if prediction == 1:

        if cgpa >= 9:
            salary = "₹12 LPA - ₹18 LPA"

        elif cgpa >= 8:
            salary = "₹8 LPA - ₹12 LPA"

        elif cgpa >= 7:
            salary = "₹5 LPA - ₹8 LPA"

        else:
            salary = "₹3 LPA - ₹5 LPA"

    else:
        salary = "Not Ready for Placement"

    # Recommendations
    recommendations = []

    if attendance < 90:
        recommendations.append("Improve attendance above 90%.")

    if projects < 3:
        recommendations.append("Build at least 3 real-world projects.")

    if internships < 1:
        recommendations.append("Complete at least one internship.")

    if cgpa < 8:
        recommendations.append("Maintain CGPA above 8.0.")

    if communication_score < 4:
        recommendations.append("Improve communication and presentation skills.")

    if marks < 80:
        recommendations.append("Improve academic performance.")

    if prediction == 1:
        recommendations.append("Practice DSA regularly.")
        recommendations.append("Prepare for coding interviews.")
        recommendations.append("Apply for campus placements.")

    # Display
    print("\n" + "=" * 65)
    print("STUDENT PROFILE")
    print("=" * 65)

    print(f"Student Name      : {name}")
    print(f"Marks             : {marks}")
    print(f"Attendance        : {attendance}%")
    print(f"Projects          : {projects}")
    print(f"Communication     : {communication}")
    print(f"Internships       : {internships}")
    print(f"CGPA              : {cgpa}")

    print("\n" + "=" * 65)
    print("MACHINE LEARNING ANALYSIS")
    print("=" * 65)

    if prediction == 1:
        print("Placement Status  : PLACED")
    else:
        print("Placement Status  : NOT PLACED")

    print(f"Confidence        : {confidence:.2f}%")

    print("\nPlacement Readiness")
    print("-" * 65)
    print(progress_bar)
    print(f"{score}%")

    print(f"\nOverall Status    : {overall_status}")

    print("\nTOP STRENGTHS")
    print("-" * 65)

    if strengths:
        for s in strengths:
            print("✓", s)
    else:
        print("No major strengths identified.")

    print("\nAREAS TO IMPROVE")
    print("-" * 65)

    if weaknesses:
        for w in weaknesses:
            print("•", w)
    else:
        print("No major weaknesses.")

    print("\nCOMPANY ELIGIBILITY")
    print("-" * 65)

    for company in companies:
        print("✓", company)

    print("\nESTIMATED SALARY")
    print("-" * 65)
    print(salary)

    print("\nPERSONALIZED RECOMMENDATIONS")
    print("-" * 65)

    if recommendations:
        for rec in recommendations:
            print("✓", rec)
    else:
        print("Excellent profile! Keep it up.")

    print("\n" + "=" * 65)

    pause()

def ml_performance_prediction(cursor):
    header("ML PERFORMANCE PREDICTION")

    rollno = input("Enter Roll Number: ").strip()

    query = """
    SELECT
        name,
        marks,
        attendance,
        projects,
        internships,
        cgpa
    FROM students
    WHERE rollno=%s
    """

    cursor.execute(query, (rollno,))
    record = cursor.fetchone()

    if not record:
        print("\nStudent not found!")
        pause()
        return

    # Student Details
    name = record[0]
    marks = record[1]
    attendance = record[2]
    projects = record[3]
    internships = record[4]
    cgpa = record[5]

    # Create DataFrame
    features = pd.DataFrame([[
        marks,
        attendance,
        projects,
        internships,
        cgpa
    ]], columns=[
        "marks",
        "attendance",
        "projects",
        "internships",
        "cgpa"
    ])

    # Predict
    predicted_marks = performance_model.predict(features)[0]

    growth = predicted_marks - marks

    # Performance Level
    if predicted_marks >= 90:
        level = "EXCELLENT"

    elif predicted_marks >= 75:
        level = "GOOD"

    elif predicted_marks >= 60:
        level = "AVERAGE"

    else:
        level = "NEEDS IMPROVEMENT"

    # Progress Bar
    score = int(predicted_marks)

    filled = score // 5
    empty = 20 - filled

    progress = "█" * filled + "░" * empty

    print("\n" + "=" * 65)
    print("STUDENT PROFILE")
    print("=" * 65)

    print(f"Student Name      : {name}")
    print(f"Current Marks     : {marks}")
    print(f"Attendance        : {attendance}%")
    print(f"Projects          : {projects}")
    print(f"Internships       : {internships}")
    print(f"CGPA              : {cgpa}")

    print("\n" + "=" * 65)
    print("PERFORMANCE FORECAST")
    print("=" * 65)

    print(f"Predicted Marks   : {predicted_marks:.2f}")

    if growth >= 0:
        print(f"Growth            : +{growth:.2f} Marks")
    else:
        print(f"Growth            : {growth:.2f} Marks")

    print("\nExpected Performance")
    print("-" * 65)

    print(progress)
    print(f"{predicted_marks:.1f}/100")

    print(f"\nPerformance Level : {level}")

    print("\nSUGGESTIONS")
    print("-" * 65)

    if attendance < 90:
        print("✓ Improve attendance.")

    if projects < 3:
        print("✓ Build more real-world projects.")

    if internships < 1:
        print("✓ Complete at least one internship.")

    if cgpa < 8:
        print("✓ Improve your CGPA.")

    if marks < 80:
        print("✓ Spend more time on academics.")

    print("✓ Practice DSA daily.")
    print("✓ Improve aptitude skills.")
    print("✓ Revise core subjects.")

    print("\n" + "=" * 65)

    pause()
