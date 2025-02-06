# ---------------------------------------------
# University Course Management System
# ---------------------------------------------
# This system manages:
# 1. Universities with course tracking.
# 2. Courses with credit validation.
# 3. Professors and students with multilevel inheritance.
# 4. Teaching Assistants who inherit from both Student and Professor.
# ---------------------------------------------

# ---------------------------------------------
# University Class
# ---------------------------------------------

class University:
    """
    Represents a university with courses and student enrollment tracking.
    """

    total_courses = 0  # Total number of courses
    total_students = 0  # Total number of students

    def __init__(self, name):
        self.name = name
        self.courses = []  # List to store courses

    def add_course(self, course):
        """
        Adds a course to the university's course list.
        """
        self.courses.append(course)
        University.total_courses += 1  # Increment course count

    def get_info(self):
        """
        Retrieves information about the university.
        """
        return f"University Name: {self.name} | Total Courses: {len(self.courses)}"

    @staticmethod
    def validate_credits(credits):
        """
        Determines eligibility based on the number of credits for financial aid.
        """
        if credits < 4:
            return "You are ineligible for FASFA!"
        elif 4 <= credits < 12:
            return "You are part-time!"
        else:
            return "You are full-time!"

# ---------------------------------------------
# Course Class
# ---------------------------------------------

class Course:
    """
    Represents a university course with enrollment and credit information.
    """

    def __init__(self, course_name, is_enrolled, credits):
        self.course_name = course_name
        self.is_enrolled = is_enrolled
        self.credits = credits

    def credits_amount(self):
        """
        Returns the number of credits for the course.
        """
        return f"Total credits for {self.course_name}: {self.credits}"

# ---------------------------------------------
# Person Class
# ---------------------------------------------

class Person:
    """
    Represents a person with a name and email.
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def introduce(self):
        """
        Returns a brief introduction of the person.
        """
        return f"Hi, my name is {self.name} and my email is {self.email}."

# ---------------------------------------------
# Professor Class
# ---------------------------------------------

class Professor(Person):
    """
    Represents a professor associated with a department.
    """

    def __init__(self, name, email, department):
        super().__init__(name, email)
        self.department = department

    def introduce(self):
        """
        Returns a detailed introduction of the professor.
        """
        return f"Hi, my name is {self.name}, and my email is {self.email}. I am in the {self.department} department."

# ---------------------------------------------
# Student Class
# ---------------------------------------------

class Student(Person, Course):
    """
    Represents a student enrolled in a university.
    """

    def __init__(self, name, email, course_name, is_enrolled, credits, major, year):
        Person.__init__(self, name, email)  # Inherit name & email
        Course.__init__(self, course_name, is_enrolled, credits)  # Inherit course details
        self.major = major
        self.year = year
        University.total_students += 1  # Increment student count

    def introduce(self):
        """
        Returns a detailed introduction of the student.
        """
        return f"Name: {self.name} | Major: {self.major} | Year: {self.year}"

    def enrollment_status(self):
        """
        Checks if the student is enrolled in a course.
        """
        return f"{self.name} {'IS' if self.is_enrolled else 'is NOT'} enrolled in {self.course_name}."

# ---------------------------------------------
# Teaching Assistant Class
# ---------------------------------------------

class TeachingAssistant(Student, Professor):
    """
    Represents a Teaching Assistant who is both a student and a professor.
    """

    def __init__(self, name, email, course_name, is_enrolled, credits, major, year, department, hours_per_week):
        Student.__init__(self, name, email, course_name, is_enrolled, credits, major, year)
        Professor.__init__(self, name, email, department)
        self.hours_per_week = hours_per_week

    def hours_a_week(self):
        """
        Returns the number of hours worked per week by the TA.
        """
        return f"Hours worked per week: {self.hours_per_week}"

    def introduce(self):
        """
        Returns a combined introduction of the Teaching Assistant.
        """
        return f"{Student.introduce(self)}\n{Professor.introduce(self)}"

# ---------------------------------------------
# Example Usage
# ---------------------------------------------

# Creating a university
uni = University("Columbia University")

# ------ Student details -------
student1 = Student(name="Nazir", email="nazirlopez123@gmail.com", course_name="Computer Organization", is_enrolled=True, credits=16, major="Computer Science", year="Sophomore")
student2 = Student(name="Diana", email="drodri891@gmail.com", course_name="Biology", is_enrolled=True, credits=16, major="Biology", year="Sophomore")

# ------ Professor details ------
professor1 = Professor(name="Arden", email="amendez@gmail.com", department="Computer Science")

# ------ Course details ------
course1 = Course(course_name="Computer Organization", is_enrolled=True, credits=13)
course2 = Course(course_name="Biology", is_enrolled=False, credits=8)

# Adding courses to the university
uni.add_course(course1)
uni.add_course(course2)

# Display university information
print("\n--- University Information ---")
print(uni.get_info())

# Student 1 details
print("\n--- Student 1 ---")
print(student1.introduce())
print(student1.enrollment_status())
print(course1.credits_amount())
print(University.validate_credits(course1.credits))

# Student 2 details
print("\n--- Student 2 ---")
print(student2.introduce())
print(student2.enrollment_status())
print(course2.credits_amount())
print(University.validate_credits(course2.credits))

# Professor details
print("\n--- Professor ---")
print(professor1.introduce())

# Assigning a teaching assistant
ta = TeachingAssistant(name="Maria", email="maria123@gmail.com", course_name="Physics 101", is_enrolled=True, credits=3, major="Psychology", year="Sophomore", department="Physics", hours_per_week=25)

# TA details
print("\n--- Teaching Assistant ---")
print(ta.introduce())
print(ta.hours_a_week())
