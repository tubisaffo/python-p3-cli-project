from connection import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            programme VARCHAR(255) NOT NULL,
            gender VARCHAR(50) NOT NULL,
            email VARCHAR(255) NOT NULL
        )
    ''')

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
            id INT AUTO_INCREMENT PRIMARY KEY,
            room_number VARCHAR(50) NOT NULL,
            capacity INT NOT NULL,
            occupied BOOLEAN NOT NULL DEFAULT FALSE
        )
    ''')

   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS allocations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT,
            room_id INT,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (room_id) REFERENCES rooms (id)
        )
    ''')

    conn.commit()
    conn.close()

def add_student(name, programme, gender, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, programme, gender, email) VALUES (?,?,?,?)', 
                   (name, programme, gender, email))
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    return student_id

def get_available_rooms():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rooms WHERE occupied = FALSE')
    rooms = cursor.fetchall()
    conn.close()
    return rooms

def allocate_room(student_id, room_id, start_date, end_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO allocations (student_id, room_id, start_date, end_date) VALUES (?,?,?,?)', 
                   (student_id, room_id, start_date, end_date))
    cursor.execute('UPDATE rooms SET occupied = TRUE WHERE id = ?', (room_id,))
    conn.commit()
    conn.close()
    
create_tables()
