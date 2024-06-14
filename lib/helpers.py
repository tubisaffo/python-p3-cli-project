from connection import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            programme VARCHAR(255) NOT NULL,
            gender VARCHAR(50) NOT NULL,
            email VARCHAR(255) NOT NULL
        )
    ''')

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY,
            room_number VARCHAR(50) NOT NULL,
            capacity INT NOT NULL,
            gender VARCHAR(50) NOT NULL,
            occupied INT NOT NULL DEFAULT 0
        )
    ''')

   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS allocations (
            id INTEGER PRIMARY KEY,
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

def add_room(room_number, capacity, gender):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO rooms (room_number, capacity, gender) VALUES (?,?,?)', 
                   (room_number, capacity, gender))
    conn.commit()
    room_id = cursor.lastrowid
    conn.close()
    return room_id

def get_available_rooms(gender=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rooms WHERE occupied = 0')
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
    
def view_allocation_history():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT students.name AS student_name, rooms.room_number, rooms.capacity
        FROM allocations
        JOIN students ON allocations.student_id = students.id
        JOIN rooms ON allocations.room_id = rooms.id
    ''')
    rows = cursor.fetchall()
    conn.close()
    
    allocations = []
    for row in rows:
        allocation = {
            'student_name': row[0],
            'room_number': row[1],
            'capacity': row[2]
        }
        allocations.append(allocation)
    
    return allocations


    
create_tables()
