# 🎓 University Course Management System

## 📌 Overview
The **University Course Management System** is a Python-based application designed to efficiently manage university operations, including courses, student enrollments, professors, and teaching assistants. The system tracks courses, validates student credits, and facilitates multi-level inheritance to simulate real-world university structures.

---

## 🚀 Features
- 🏫 **University Management**: Track total courses and students.
- 📚 **Course Management**: Add and validate courses with credit requirements.
- 👨‍🏫 **Professor Module**: Manage professors assigned to departments.
- 🎓 **Student Enrollment**: Students can enroll in courses with major and year tracking.
- 🏆 **Teaching Assistant Role**: Inherits from both Student and Professor, working across multiple disciplines.
- ✅ **Credit Validation**: Determines full-time/part-time student status based on credits.

---

## 🛠 Technologies Used
This project demonstrates core **Python** concepts:
- **Object-Oriented Programming (OOP)**: Uses `University`, `Course`, `Person`, `Student`, `Professor`, and `TeachingAssistant` classes.
- **Multi-Level Inheritance**: `TeachingAssistant` inherits from both `Student` and `Professor`.
- **Encapsulation & Methods**: Implements encapsulated data and relevant class methods.
- **Static & Class Methods**: Uses static methods for validation and class methods for tracking statistics.
- **Polymorphism**: Implements `introduce()` across multiple classes for customized behavior.

---

## 🔹 How to Use
1️⃣ **Clone the Repository**:
   ```bash
   git clone https://github.com/dodginfeds/university-course-manager.git
   cd university-course-manager
   ```
2️⃣ **Run the Application**:
   ```bash
   python university_course_manager.py
   ```

---

## 📌 Example Usage
```python
# Creating a university instance
uni = University("Columbia University")

# Adding courses
course1 = Course("Computer Organization", True, 13)
course2 = Course("Biology", False, 8)
uni.add_course(course1)
uni.add_course(course2)

# Creating a student
student1 = Student("Nazir", "nazirlopez123@gmail.com", "Computer Organization", True, 16, "Computer Science", "Sophomore")
print(student1.introduce())
print(student1.enrollment_status())
```
🔹 **Output:**
```
--- University Information ---
University Name: Columbia University | Total Courses: 2

--- Student 1 ---
Name: Nazir | Major: Computer Science | Year: Sophomore
Nazir IS enrolled in Computer Organization.
Total credits for Computer Organization: 13
You are full-time!
```

---

## 🔮 Future Enhancements
- 📊 **Course Catalog API**: Fetch course details from external university APIs.
- 📱 **GUI Interface**: Develop a graphical interface for better user experience.
- 🎯 **Student Performance Tracking**: Introduce grade tracking for each course.
- 📝 **Automated Enrollment**: Implement an automated system for course registration.

---

For any inquiries, feel free to reach out via [GitHub](https://github.com/dodginfeds).
