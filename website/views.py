from sqlite3 import IntegrityError
from flask import Blueprint, redirect, render_template, request, flash,url_for
from flask_login import login_required, current_user
from .models import Application, Job, Employee , Student, Accepted
from . import db




views = Blueprint('views', __name__)

jobs = []
@views.route('/ed', methods=['GET','POST'])
@login_required
def ed():
    return render_template('ed.html')


@views.route('/post_jobs', methods=['GET','POST'])
def post_jobs():
    # If the request method is POST, process the form submission
    if request.method == 'POST':
        # Check if the current user is authorized to post a job
        if current_user.is_authenticated and current_user.type=="employee":
            title = request.form['title']
            description = request.form['description']
            
            # Create a new job object
            job = Job(title=title, description=description, employee_id=current_user.id)
            
            # Add the job to the database session and commit changes
            db.session.add(job)
            db.session.commit()
            
            flash('Job posted successfully!', 'success')
            # After posting the job, redirect to the same page
            return redirect(url_for('views.ed'))  
        else:
            flash('You are not authorized to post a job.', 'error')

    # Render the ed.html template with the job posting form
    return render_template('ed.html') # Redirect to the employee dashboar

@views.route('/sd')
def sd():
    jobs=Job.query.all()
    return render_template('sd.html',jobs=jobs)

@views.route('/apply/<int:job_id>', methods=['POST'])
def apply(job_id):
    if current_user.is_authenticated and current_user.type == "student":
        # Check if the job ID is valid
        job = Job.query.get(job_id)
        if not job:
            flash('Job not found!', 'error')
            return redirect(url_for('views.sd'))

        # Check if the student has already applied for this job
        existing_application = Application.query.filter_by(job_id=job_id, student_id=current_user.id).first()
        if existing_application:
            flash('You have already applied for this job.', 'error')
            return redirect(url_for('views.sd'))

        # Create a new application
        application = Application(
            job_id=job_id,
            job_title=job.title,
            job_description=job.description,
            student_id=current_user.id,
            employee_id=job.employee_id
        )

        # Add the application to the database
        try:
            db.session.add(application)
            db.session.commit()
            flash('Applied successfully!', 'success')
        except IntegrityError as e:
            db.session.rollback()
            flash('Failed to apply for the job.', 'error')
            print(e)  # Log the error for debugging purposes

    else:
        flash('You must be logged in as a student to apply for jobs.', 'error')
    return redirect(url_for('views.sd'))



@views.route('/profile')
@login_required


def profile():
   
   if current_user.type == "student":
    student = Student.query.filter_by(id=current_user.id).first()
    
    # Fetch applications for the current student along with their acceptance status
    jobs_applied = []
    applications = Application.query.filter_by(student_id=current_user.id).all()
    for application in applications:
        employee = Employee.query.filter_by(id=application.employee_id).first()
        acceptance_status = Accepted.query.filter_by(application_id=application.id).first()
        if acceptance_status:
            accepted = acceptance_status.accept
        else:
            accepted = None
        
        # Assigning 1 for accepted, 0 for rejected, and None for not yet processed
        if accepted == '1':
         status = "Accepted"
        elif accepted == '0':
         status = "Rejected"
        else:
         status = "Not Yet Processed"
        
        job_applied = {
            'job_title': application.job_title,
            'job_description': application.job_description,
            'employee_name': employee.name,
            'status': status
        }
        
        jobs_applied.append(job_applied)

    return render_template('studentprofile.html', student=student, jobs_applied=jobs_applied)



   elif current_user.type == "employee":
    employee = Employee.query.filter_by(id=current_user.id).first()
    jobs_posted = Job.query.filter_by(employee_id=current_user.id).all()

    # Fetch applications for each job
    job_applications = {}
    for job in jobs_posted:
        applications = Application.query.filter_by(job_id=job.id).all()
        student_applications = []
        for app in applications:
            student = Student.query.filter_by(id=app.student_id).first()
            if student:
                student_applications.append((app, student))
        job_applications[job] = student_applications

    return render_template('employeeprofile.html', employee=employee, job_applications=job_applications)


@views.route('/employee/profile/applications/<int:application_id>', methods=['POST'])
@login_required
def process_application(application_id):
    application = Application.query.get_or_404(application_id)
    action = request.form.get('action')

    if Accepted.query.filter_by(application_id=application_id, employee_id=current_user.id).first():
        flash('You have already processed this application.', 'warning')
        return redirect(url_for('views.profile'))

    if action == 'accept':
        accepted_application = Accepted(
            application_id=application_id,
            student_id=request.form.get('student_id'),
            employee_id=current_user.id,
            job_id=request.form.get('job_id'),
            accept=True
        )
    elif action == 'reject':
        accepted_application = Accepted(
            application_id=application_id,
            student_id=request.form.get('student_id'),
            employee_id=current_user.id,
            job_id=request.form.get('job_id'),
            accept=False
        )

    db.session.add(accepted_application)
    db.session.commit()
    flash('Application processed.', 'success')
    return redirect(url_for('views.profile'))