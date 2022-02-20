from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class student(db.Model):
    student_id = db.Column(db.Integer, primary_key = True, nullable = False)
    roll_number = db.Column(db.String, unique = True, nullable = False)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String)
    s_enrollment = db.relationship("enrollments", backref="stud")

    def __repr__(self):
        return "<Student %r>" % self.roll_number

class course(db.Model):
    course_id = db.Column(db.Integer, primary_key = True, nullable = False)
    course_code = db.Column(db.String, nullable = False, unique = True)
    course_name = db.Column(db.String, nullable = False)
    course_description = db.Column(db.String)
    c_enrollment = db.relationship("enrollments", backref="cours")

    def __repr__(self):
        return "<Course %r>" % self.course_code

class enrollments(db.Model):
    enrollment_id = db.Column(db.Integer, primary_key = True, nullable = False)
    estudent_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable = False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable = False)
    #stud
    #cours
    def __repr__(self):
        return "<Enrollment %r>" % self.enrollment_id