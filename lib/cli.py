from helpers import (
    add_student,
    get_available_rooms,
    allocate_room,
    # view_students,
    # view_allocation_history,
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
            view_allocation_history()

        elif choice == "5":
            print("Exiting Hostel Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


def student_management():
    print("\nStudent Management:")
    print("1. Register Student")
    print("2. View Registered Students")

    choice = input("> ")

    if choice == "1":
        name = input("Enter student's name: ")
        programme = input("Enter student's programme: ")
        gender = input("Enter student's gender (Male/Female/Other): ")
        email = input("Enter student's email: ")

        student_id = add_student(name, programme, gender, email)
        print(f"Student {name} added with ID {student_id}.")

    elif choice == "2":
        view_students()

    else:
        print("Invalid choice.")


def room_management():
    print("\nRoom Management:")
    print("1. View Available Rooms")

    choice = input("> ")

    if choice == "1":
        rooms = get_available_rooms()
        if not rooms:
            print("No available rooms at the moment.")
            return

        print("\nAvailable Rooms:")
        for room in rooms:
            print(f"Room ID: {room['id']}, Room Number: {room['room_number']}, Capacity: {room['capacity']}")

    else:
        print("Invalid choice.")


def booking():
    print("\nBooking:")
    student_id = int(input("Enter student ID: "))
    rooms = get_available_rooms()
    if not rooms:
        print("No available rooms at the moment.")
        return

    print("\nAvailable Rooms:")
    for room in rooms:
        print(f"Room ID: {room['id']}, Room Number: {room['room_number']}, Capacity: {room['capacity']}")

    room_id = int(input("\nEnter the Room ID you want to book: "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    allocate_room(student_id, room_id, start_date, end_date)
    print(f"Room {room_id} allocated to student {student_id} from {start_date} to {end_date}.")


if __name__ == "__main__":
    main()
