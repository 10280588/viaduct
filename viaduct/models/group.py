#!/usr/bin/python

from viaduct import db
from viaduct.models import BaseEntity

user_group = db.Table('user_group', db.Column('user_id', db.Integer,
                                              db.ForeignKey('user.id')),
                      db.Column('group_id', db.Integer,
                                db.ForeignKey('group.id')))


<<<<<<< HEAD
group_group = db.Table('group_group',
    db.Column('super_id', db.Integer, db.ForeignKey('group.id')),
    db.Column('sub_id', db.Integer, db.ForeignKey('group.id'))
)

class Group(db.Model, BaseEntity):
    __tablename__ = 'group'

    name = db.Column(db.String(256), unique=True)

    users = db.relationship('User', secondary=user_group,
                            backref=db.backref('groups', lazy='dynamic'),
                            lazy='dynamic')

    groups = db.relationship('Group', secondary=group_group,
            primaryjoin=id==group_group.c.super_id,
            secondaryjoin=id==group_group.c.sub_id,
            backref=db.backref('super_groups', lazy='dynamic'), lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def has_user(self, user):
        if not user:
            return False
        else:
            return self.users.filter(user_group.c.user_id == user.id)\
                .count() > 0

    def add_user(self, user):
        if not self.has_user(user):
            self.users.append(user)

            return self

    def delete_user(self, user):
        if self.has_user(user):
            self.users.remove(user)

    def get_users(self):
        # FIXME: backwards compatibility.
        return self.users

    def has_group(self, group):
        if not group:
            return False
        else:
            return self.groups.filter(group_group.c.super_id == group.id).count() > 0

    def add_group(self, group):
        if not self.has_group(group):
            self.groups.append(group)

    def delete_group(self, group):
        if self.has_group(group):
            self.groups.remove(group)

    def get_group(self):
        return self.groups
