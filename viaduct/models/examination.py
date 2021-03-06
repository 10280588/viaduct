import datetime

from viaduct import db

from viaduct.models.course import Course
from viaduct.models.education import Education
from viaduct.models.user import User
from viaduct.models import BaseEntity


class Examination(db.Model, BaseEntity):
    __tablename__ = 'examination'

    title = db.Column(db.String(128))
    path = db.Column(db.String(256))
    answer_path = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime)
    course_id = db.Column(db.Integer,
                          db.ForeignKey('course.id'))
    education_id = db.Column(db.Integer,
                             db.ForeignKey('education.id'))

    user = db.relationship(User,
                           backref=db.backref('examinations', lazy='dynamic'))
    course = db.relationship(Course,
                             backref=db.backref('examinations', lazy='dynamic')
                             )
    education = db.relationship(Education,
                                backref=db.backref('examinations',
                                                   lazy='dynamic'))

    def __init__(self, path, title, course_id, education_id,
                 timestamp=datetime.datetime.utcnow(), answers=''):
        self.timestamp = timestamp
        self.path = path
        self.title = title
        self.course_id = course_id
        self.education_id = education_id
        self.answer_path = answers
