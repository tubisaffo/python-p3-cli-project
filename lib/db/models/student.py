class Student:
    def __init__(self, id, name, programme, gender, email):
        self.id = id
        self.name = name
        self.programme = programme
        self.gender = gender
        self.email = email

    def __str__(self):
        return f"Student[ID={self.id}, Name={self.name}, Programme={self.programme}, Gender={self.gender}, Email={self.email}]"
