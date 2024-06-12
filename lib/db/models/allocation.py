class Allocation:
    def __init__(self, id, student_id, room_id, start_date, end_date):
        self.id = id
        self.student_id = student_id
        self.room_id = room_id
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Allocation[ID={self.id}, Student ID={self.student_id}, Room ID={self.room_id}, Start Date={self.start_date}, End Date={self.end_date}]"