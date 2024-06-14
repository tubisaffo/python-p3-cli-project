### Hostel Management System

### Date: 2024/6/14

## By: [SAFFO MOHAMED TUBI]

### Overview

The Hostel Management System is a Python Command-Line Interface (CLI) application aimed at streamlining the process of managing student accommodations in a hostel. This tool is designed for hostel administrators to efficiently allocate rooms and for students to easily find available accommodations. The system offers functionalities to register students, manage room inventory, book rooms, and review booking history.

### Getting Started

To set up the Hostel Management System on your local machine, follow these steps:

1. Ensure Python is installed on your system.

2. Fork and clone the repository to your local machine.

3. Navigate to the project directory via the terminal: cd Hostel-Management-System.

4. Run the application by executing: python cli.py.

## Directory Structure

The project structure is organized as follows:

1. cli.py: Main script that serves as the entry point for the application. It provides the menu interface and handles user interactions.

2. helpers.py: Contains utility functions for database operations and core functionalities such as student registration, room management, and booking. Key functions include:

create_tables(): Sets up the necessary database tables.

add_student(): Registers a new student.

add_room(): Adds a new room to the inventory.

get_available_rooms(): Lists all available rooms.

allocate_room(): Assigns a room to a student.

view_allocation_history(): Displays the history of room allocations.

3. connection.py: Manages database connectivity using SQLite. It includes:

get_db_connection(): Establishes and returns a connection to the SQLite database.

4. README.md: This file, which provides comprehensive details about the project.

## Technologies Utilized

Python: A versatile and easy-to-learn programming language, used to develop the application's logic and CLI.

SQLite: A self-contained, serverless database engine used to store data related to students, rooms, and bookings.

GitHub: A platform for version control and collaborative development, hosting the project's source code.

## Design and Implementation

The application adheres to procedural programming principles with clearly defined functions to handle specific tasks. Database interactions are managed via SQLite, ensuring efficient data storage and retrieval. The CLI interface offers a straightforward way for users to interact with the system.

## Support and Contributions

For questions, suggestions, or contributions, please contact:

## GitHub: [github.com//tubisaffo]

## License

This project is licensed under the MIT license.

© 2024 [TubiSaffo]
