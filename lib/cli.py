from helpers import (
    add_student,
    get_available_rooms,
    allocate_room,
    view_allocation_history,
    add_room
)

def main():
    print("Welcome to the Hostel Management System")

    while True:
        print("\nMenu:")
        print("1. Student Management")
        print("2. Room Management")
        print("3. Booking")
        print("4. View Allocation History")
        print("5. Exit")

        choice = input("> ")

        if choice == "1":
            student_management()

        elif choice == "2":
            room_management()

        elif choice == "3":
            booking()

        elif choice == "4":
            view_allocations()

        elif choice == "5":
            print("Exiting Hostel Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


def student_management():
    print("\nStudent Management:")
    print("1. Register Student")

    choice = input("> ")

    if choice == "1":
        name = input("Enter student's name: ")
        programme = input("Enter student's programme: ")
        gender = input("Enter student's gender (Male/Female/Other): ")
        email = input("Enter student's email: ")

        student_id = add_student(name, programme, gender, email)
        print(f"Student {name} added with ID {student_id}.")
        
    else:
        print("Invalid choice.")


def room_management():
    print("\nRoom Management:")
    print("1. View Available Rooms")
    print("2. Add Room")

    choice = input("> ")

    if choice == "1":
        rooms = get_available_rooms()
        if not rooms:
            print(f"No available rooms at the moment.")
            return

        print(f"\nAvailable Rooms:")
        single_rooms = [room for room in rooms if room[2] == 1]
        double_rooms = [room for room in rooms if room[2] == 2]
        over_double = [room for room in rooms if room[2] > 2]
        print("\nSingle Rooms:")
        for room in single_rooms:
            print(f"Room ID: {room[0]}, Room Number: {room[1]}")

        print("\nDouble Rooms:")
        for room in double_rooms:
            print(f"Room ID: {room[0]}, Room Number: {room[1]}")
            
        print("\nMore Than Double Rooms:")
        for room in over_double:
            print(f"Room ID: {room[0]}, Room Number: {room[1]}")
        
    elif choice == "2":
        room_number = input("Enter Room Number:> ")
        capacity = int(input("Enter Room Capacity:> "))
        gender = input("Enter Room Gender (Male/Female): ").capitalize()
        
        id = add_room(room_number, capacity, gender)
        print(f"Room {room_number} added with ID {id}.")
    else:
        print("Invalid choice.")


def booking():
    print("\nBooking:")
    student_id = int(input("Enter student ID: "))
    gender = input("Enter student's gender (Male/Female): ").capitalize()
    rooms = get_available_rooms(gender)
    if not rooms:
        print(f"No available {gender.lower()} rooms at the moment.")
        return

    print(f"\nAvailable {gender} Rooms:")
    single_rooms = [room for room in rooms if room[2] == 1][:5]
    double_rooms = [room for room in rooms if room[2] == 2][:5]
    over_double = [room for room in rooms if room[2] > 2]

    print("\nSingle Rooms:")
    for room in single_rooms:
        print(f"Room ID: {room[0]}, Room Number: {room[1]}")

    print("\nDouble Rooms:")
    for room in double_rooms:
        print(f"Room ID: {room[0]}, Room Number: {room[1]}")
        
    print("\nMore Than Double Rooms:")
    for room in over_double:
        print(f"Room ID: {room[0]}, Room Number: {room[1]}")

    room_id = int(input("\nEnter the Room ID you want to book: "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    allocate_room(student_id, room_id, start_date, end_date)
    print(f"Room {room_id} allocated to student {student_id} from {start_date} to {end_date}.")


def view_allocations():
    print("\nAllocation History:")
    allocations = view_allocation_history()
    if not allocations:
        print("No allocations found.")
        return
    
    for allocation in allocations:
        student_name = allocation['student_name']
        room_number = allocation['room_number']
        room_type = "Single" if allocation['capacity'] == 1 else "Double" if allocation['capacity'] == 2 else "More than Double"
        print(f"Student: {student_name}, Room Number: {room_number}, Room Type: {room_type}")


if __name__ == "__main__":
    main()
