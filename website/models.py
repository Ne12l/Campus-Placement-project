from . import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Student(db.Model, UserMixin):
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    type = db.Column(db.String(50), nullable=False)
    cgpa = db.Column(db.Float())
    password = db.Column(db.String(150))


class Employee(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    type = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(150))

class Job(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    employee = db.relationship('Employee', backref='job')
    def get_applications(self):
        return Application.query.filter_by(job_id=self.id).all()

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    student_id = db.Column(db.String(30), db.ForeignKey('student.id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    job_app = db.relationship('Job', backref=db.backref('application', lazy=True))
    student = db.relationship('Student', backref=db.backref('application', lazy=True))
    employee = db.relationship('Employee', backref=db.backref('application', lazy=True))

class Accepted(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    accept = db.Column(db.String(10), nullable=False)  # Changed to String for more flexibility

    # Add a ForeignKey relationship back to Application, Job, Student, and Employee
    application = db.relationship('Application', backref=db.backref('accepted', lazy=True))
    job = db.relationship('Job', backref=db.backref('accepted', lazy=True))
    student = db.relationship('Student', backref=db.backref('accepted', lazy=True))
    employee = db.relationship('Employee', backref=db.backref('accepted', lazy=True))


