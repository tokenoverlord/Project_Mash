# app/models.py

# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash

from app import db

class Job(db.Model):
    """
    Create an Job table
    """

    # Ensures the table will be named in plural
    __tablename__ = 'jobs'

    jobID = db.Column(db.Integer, primary_key=True)
    recordType = db.Column(db.Integer)
    jobTitle = db.Column(db.String(60))
    employerName = db.Column(db.String(60))
    jobDescription = db.Column(db.String(256))
    locations = ""
    url = db.Column(db.String(256))
    postedDate = db.Column(db.String(60))
    expiryDate = db.Column(db.String(60))
    salaryType = db.Column(db.String(60))
    salaryMultiplier = db.Column(db.Integer)
    salaryMin = db.Column(db.Integer)
    salaryMax = db.Column(db.Integer)
    jobType = ""
    majorProject = ""

class Location(db.Model):
    """
    Create an Location table
    """

    # Name the for locations
    __tablename__ = 'locations'

    city = db.Column(db.String(60), primary_key=True)
    region = ""
    regionName = db.Column(db.String(60))
    province = db.Column(db.String(60))

class Job_Location(db.Model):
    """
    Create an Job Location table that represents the many to many
    """

    # Name the table for jobs_locations
    __tablename__ = 'jobs_locations'

    jlid = db.Column(db.String(60), primary_key=True)
    jobID = db.Column(db.Integer, db.ForeignKey('jobs.jobID'))
    city = db.Column(db.String(60), db.ForeignKey('locations.city'))

class JobType(db.Model):
    """
    Create an Job Type table
    """

    # Name the for jobtypes
    __tablename__ = 'jobtypes'

    jtid = db.Column(db.String(60), primary_key=True)
    id = db.Column(db.Integer)
    jobID = db.Column(db.Integer, db.ForeignKey('jobs.jobID'))
    caption = db.Column(db.String(60))

class Region(db.Model):
    """
    Create an Region table
    """

    __tablename__ = 'regions'

    rid = db.Column(db.String(60), primary_key=True)
    id = db.Column(db.Integer)
    city = db.Column(db.String(60), db.ForeignKey('locations.city'))
    caption = db.Column(db.String(60))

class MajorProject(db.Model):
    """
    Create an Major Projects table
    """

    __tablename__ = 'majorprojects'

    mpid = db.Column(db.String(60), primary_key=True)
    id = db.Column(db.Integer)
    jobID = db.Column(db.Integer, db.ForeignKey('jobs.jobID'))
    caption = db.Column(db.String(60))
