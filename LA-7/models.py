from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key = True, nullable = False)
    roll_number = db.Column(db.String, unique = True, nullable = False)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String)

    def __repr__(self):
        return "<Student %r>" % self.roll_number

class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key = True, nullable = False)
    course_code = db.Column(db.String, nullable = False, unique = True)
    course_name = db.Column(db.String, nullable = False)
    description = db.Column(db.String)

    def __repr__(self):
        return "<Course %r>" % self.course_code

class Enrollments(db.Model):
    enrollment_id = db.Column(db.Integer, primary_key = True, nullable = False)
    estudent_id = db.Column(db.Integer, ForeignKey('student.student_id'), nullable = False)
    ecourse_id = db.Column(db.Integer, ForeignKey('course.course_id'), nullable = False)

    def __repr__(self):
        return "<Enrollment %r>" % self.enrollment_id