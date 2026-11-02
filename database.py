import os
from dotenv import load_dotenv
load_dotenv()

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME")
    )


def get_all_students():
    conn = get_connection()

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results


def insert_student(student):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)",
                   (student.name, student.age) )
    conn.commit()
    cursor.close()
    conn.close()

    return {"message" : "Student added successfully"} 


def update_student(student_id, student):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name = %s, age = %s WHERE id = %s",
                   (student.name, student.age, student_id))
    updated = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return updated > 0
    

def delete_students(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s",
                   (student_id, ) )
    deleted = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return deleted > 0


def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * from students WHERE id = %s", 
                   (student_id,) )
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

