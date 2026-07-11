from ui import header

def admin_login(cursor):

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    query = """
    SELECT *
    FROM admin
    WHERE username=%s
    AND password=%s
    """

    cursor.execute(query, (username, password))

    record = cursor.fetchone()

    if record:
        print("Admin login successful.")
        return True

    print("Invalid admin credentials.")
    return False