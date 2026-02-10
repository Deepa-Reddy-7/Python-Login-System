### **Python Login System using Tkinter \& MySQL**



##### **Project Overview**



This project is a desktop-based login application built using Python, where a user can log in through a graphical interface and have their credentials validated against a MySQL database.



The main objective of this project was to understand how Python applications interact with databases in real-world scenarios, while also gaining hands-on experience with GUI development, database connectivity, and authentication logic.



##### **Why I Built This Project**



I built this project to move beyond basic Python scripts and work on a complete application that connects multiple concepts together. Instead of working only in the terminal, I wanted to create a user-facing application that:



* Takes input from a GUI
* Communicates with a database
* Validates data using SQL queries



This project helped me understand how backend logic, databases, and frontend interfaces work together in a single application.



##### **Features**



* Graphical user interface built using Tkinter
* Login authentication using MySQL database
* Validates username and password using SQL queries
* Clean separation of GUI logic and database logic
* Displays login success or failure based on database records



##### **Technologies Used**



* Python
* Tkinter (for GUI development)
* MySQL
* mysql-connector-python



##### **Project Structure**

Python-Login-System-MySQL

│

├── app.py            # Tkinter GUI and user interaction

├── database.py       # Database connection and authentication logic

├── schema.sql        # SQL script to create database and table

├── requirements.txt  # Required Python libraries

└── README.md



##### **Database Structure**



The application uses a MySQL database with the following structure:



Database Name: projectdb

Table Name: igldetails



Column Name	Data Type	Description

id	INT	Primary key (auto-increment)

username	VARCHAR	Stores username

password	VARCHAR	Stores password



\*\* Database credentials are not included in the code for security reasons.\*\*



##### **How the Application Works**



-> The user enters a username and password in the Tkinter login form

-> When the Login button is clicked, the input values are sent to the backend

-> The application connects to the MySQL database

-> A SQL query checks whether the entered credentials exist in the table

-> If a matching record is found, login is successful

-> If no record is found, login fails



###### Note

For security reasons, database credentials are not hardcoded in this repository.

Users must update the database connection details in database.py before running the application.



##### **Key Learnings**



* Learned how to connect Python applications with MySQL databases
* Gained hands-on experience in GUI development using Tkinter
* Understood how SQL queries are used for authentication
* Improved skills in writing modular and reusable Python code
* Developed a better understanding of real-world application flow



This project helped me strengthen my Python fundamentals and gave me confidence in building small but complete applications. It represents my learning journey in Python development, database integration, and application design.

