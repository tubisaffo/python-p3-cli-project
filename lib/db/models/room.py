class Room:
    def __init__(self, id, room_number, capacity, gender, occupied):
        self.id = id
        self.room_number = room_number
        self.capacity = capacity
        self.gener = gender
        self.occupied = occupied

    def __str__(self):
        return f"Room[ID={self.id}, Room Number={self.room_number}, Capacity={self.capacity}, Occupied={self.occupied}]"