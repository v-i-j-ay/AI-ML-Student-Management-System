import os
import google.generativeai as genai
from ui import header, pause
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")




def ai_resume_summary(cursor):
    header("AI RESUME SUMMARY")
    roll = input("Enter roll number: ").strip()

    query = """
    SELECT name, marks, skills, business_idea
    FROM students
    WHERE rollno=%s
    """

    cursor.execute(query, (roll,))
    record = cursor.fetchone()

    if not record:
        print("Student not found")
        return

    name = record[0]
    marks = record[1]
    skills = record[2]
    idea = record[3]

    print("\n===== AI Resume Summary =====\n")

    print(f"""
{name} is a motivated student with strong knowledge in {skills}.

Scored {marks} marks and interested in innovative ideas like "{idea}".

Passionate about software development, problem solving and learning new technologies.
""")
    pause()

def ai_chatbot():
    header("AI STUDENT ASSISTANT")

    chat = model.start_chat(history=[])

    print("Type 'exit' to return")

    while True:

        question = input("\n👨 You : ")

        if question.lower() == "exit":
            break

        try:
            response = chat.send_message(question)

            print("\n🤖 AI :")
            print("-" * 50)
            print(response.text)
            print("-" * 50)

        except Exception as e:
            print("Error:", e)
    pause()