import mysql.connector

def authenticate(id_no, password):
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="identities"
    )
    cursor = conn.cursor()

    # Execute the query to fetch the user's data
    cursor.execute("SELECT Id, Password FROM ids WHERE Id=%s AND Password=%s", (id_no, password))
    result = cursor.fetchone()

    if result is not None:
        stored_id_no, stored_password = result
        if password == stored_password:
            return True

    # Close the database connection
    conn.close()
    return False

def get_user_data(id_no):
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="identities"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT Id, Name FROM ids WHERE Id=%s", (id_no,))
    result = cursor.fetchone()

    # Close the database connection
    conn.close()
    
    if result is not None:
        user_data = {
            "id_no": result[0],
            "name": result[1]
        }
        return user_data
    else:
        return None
    
def update_name(id_no, new_name):
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="identities"
    )
    cursor = conn.cursor()

    # Update the name in the database
    cursor.execute("UPDATE ids SET Name = %s WHERE Id = %s", (new_name, id_no))
    conn.commit()

    # Close the database connection
    conn.close()


# Browse the database
def browse():
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="identities"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT Id, Name FROM ids")
    result = cursor.fetchall()
    
    return result

# Search the database
def search_data_by_id(search_text):
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="identities"
    )
    cursor = conn.cursor(dictionary=True)

    # Execute the query to fetch the user's data
    Search_text = "%" + search_text + "%"
    cursor.execute("SELECT Id, Name FROM ids WHERE Id LIKE %s", (Search_text,))
    filtered_data = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    return filtered_data


