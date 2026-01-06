# College-ERP
A college management system built using Django framework. It is designed for interactions between students and teachers. Features include attendance, marks and time table.

## Installation

Python and Django need to be installed

```bash
pip install django
```

## Usage

Go to the College-ERP folder and run

```bash
python manage.py runserver
```

Then go to the browser and enter the url **http://127.0.0.1:8000/**


## Login

The login page is common for students and teachers.  
The username is their name and password for everyone is 'project123'.  

Example usernames:  
student- 'anna'  
teacher- 'trisila'  

You can access the django admin page at **http://127.0.0.1:8000/admin** and login with username 'admin' and the above password.

Also a new admin user can be created using

```bash
python manage.py createsuperuser
```

## Users

New students and teachers can be added through the admin page. A new user needs to be created for each. 

The admin page is used to modify all tables such as Students, Teachers, Departments, Courses, Classes etc.

**For more details regarding the system and features please refer the reports included.**

## Update (29/11/2020)

Added method to reset attendance time range in Django Admin page.

![alt_text](https://i.imgur.com/0xOWmUZ.png)

This is present in Django Admin -> Attendance (http://127.0.0.1:8000/admin/info/attendanceclass/).  
Start Date: Start Date of Attendance period  
End Date: End Date of Attendance period

This will delete all present attendance data and create new attendance objects for the given time range. 

## Screenshots
### Login Page
<img width="1918" height="971" alt="Screenshot 2026-01-06 224730" src="https://github.com/user-attachments/assets/e4f6ecf8-498f-4bd5-a7d8-a55d4a8282d1" />

### Teacher Page
<img width="1919" height="974" alt="image" src="https://github.com/user-attachments/assets/65127382-5e0b-4818-9f4f-a491a848950a" />
<img width="1918" height="972" alt="Screenshot 2026-01-06 225410" src="https://github.com/user-attachments/assets/99c92da3-eb96-4b09-b449-ec3707c03831" />
<img width="1918" height="968" alt="teacher marks" src="https://github.com/user-attachments/assets/d871bdc0-ed6d-4748-800b-2de3003ccda8" />

### Student Page
<img width="1918" height="972" alt="Screenshot 2026-01-06 224819" src="https://github.com/user-attachments/assets/2566258c-e4ae-4708-ad7a-3b7312176f36" />
<img width="1918" height="971" alt="timetable" src="https://github.com/user-attachments/assets/ac6544a4-1bd7-4b75-bb41-a3fe0b32d569" />

### Admin Page

<img width="1255" height="617" alt="image" src="https://github.com/user-attachments/assets/2c7eb1ba-bf8f-4245-b88c-f24c9fec5b36" />
<img width="1633" height="800" alt="image" src="https://github.com/user-attachments/assets/a25840ad-4824-4251-ab19-dd9c263d94b7" />
<img width="1632" height="793" alt="image" src="https://github.com/user-attachments/assets/aa98b484-0769-41dd-942a-699d879c2682" />

