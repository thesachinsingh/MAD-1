import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, student, course, enrollments

app = Flask(__name__)

curr_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(curr_dir, 'week7_database.sqlite3')
db.init_app(app)




#1
@app.route('/')
def homepage():
    all_list = student.query.all()
    return render_template("index.html", all_list = all_list)    


#2
@app.route('/student/create', methods=['POST', 'GET'])
def student_create():
    if request.method == 'POST':
        # Retrieving Data from form
        roll_no = request.form['roll']
        f_name = request.form['f_name']
        l_name = request.form['l_name']
        

        # checking if the data already exists in the db
        # if data already exists, return already-exists.html page, else move to pushing data into db
        checker = student.query.filter_by(roll_number = roll_no).first()
        if checker != None:
            return render_template("already-exists.html")

        #inserting in student table
        s = student(roll_number = roll_no, first_name = f_name, last_name = l_name)
        db.session.add(s)
        db.session.commit()

        # course_dict = {
        #     "course_1": "MAD I",
        #     "course_2": "DBMS",
        #     "course_3": "PDSA",
        #     "course_4": "BDM"
        # }

        # course_list = []
        # for cs in course_s:
        #     course_list.append(course_dict[cs])
        #     c = course.query.filter_by(course_name = course_dict[cs]).first()
        #     e = enrollments(estudent_id = s.student_id, ecourse_id = c.course_id)
        #     db.session.add(e)
        
        # db.session.commit()
        return redirect('/')
    
    return render_template("add_student.html")


#3
@app.route("/student/<int:student_id>/update", methods = ['GET', 'POST'])
def update_student(student_id):
    if request.method == 'POST':
        pass
    
    all_courses = course.query.all()
    return render_template("update_student.html")



#4
@app.route("/student/<int:student_id>/delete")
def del_student(student_id):
    s = student.query.filter_by(student_id = student_id)
    if s:
        student.query.filter_by(student_id = student_id).delete()
        e_details = enrollments.query.filter_by(estudent_id = student_id)
        if e_details:
            enrollments.query.filter_by(estudent_id = student_id).delete()
        
        db.session.commit()

    return redirect('/')


#5
@app.route("/student/<int:student_id>")
def get_student(student_id):
    s = student.query.get(student_id)
    if s:
        return render_template("student.html", stud = s)
    return render_template("404.html", data = "Student")


#6
@app.route("/student/<int:student_id>/withdraw/<int:course_id>")
def del_enrollment(student_id, course_id):
    e = enrollments.query.filter_by(ecourse_id = course_id, estudent_id = student_id)
    if e:
        enrollments.query.filter_by(ecourse_id = course_id, estudent_id = student_id).delete()
        db.session.commit()

    return redirect('/')



#7
@app.route("/courses")
def all_courses():
    c = course.query.all()
    
    return render_template("all_courses.html", c = c)




#8
@app.route("/course/create", methods = ['GET', 'POST'])
def create_course():
    if request.method == "POST":
        course_code = request.form['code']
        course_name = request.form['c_name']
        course_description = request.form.get('desc', '')

        checking = course.query.filter_by(course_code = course_code).first()
        if checking:
            return render_template("course_already_exists")


        course_item = course(course_code = course_code, course_name = course_name, course_description = course_description)
        db.session.add(course_item)
        db.session.commit()

        return redirect("/courses")

    return render_template("add_course.html")
    



#9
@app.route("/course/<int:course_id>/update", methods = ['GET', 'POST'])
def update_course(course_id):
    if request.method == 'POST':
        course_code = request.form['code']
        course_name = request.form['c_name']
        course_description = request.form.get('desc', '')

        c = course.query.get(course_id)
        c.course_name = course_name
        c.course_description = course_description
        db.session.commit()

        return redirect('/courses')
        

    data = course.query.get(course_id)
    return render_template("update_course.html", data = data)



#10
@app.route("/course/<int:course_id>/delete")
def del_course(course_id):
    course_detail = course.query.get(course_id)
    if course_detail:
        course.query.get(course_id).delete()
        if enrollments.query.filter_by(ecourse_id = course_id):
            enrollments.query.filter_by(ecourse_id = course_id).delete()
        db.session.commit()
    
    return redirect("/")


#11
@app.route("/course/<int:course_id>")
def course_details(course_id):
    course_data = course.query.get(course_id)
    e_data = enrollments.query.get(ecourse_id = course_id)
    return render_template("course_details.html", course_data = course_data)
    



if __name__ == '__main__':
    app.run(debug=True)