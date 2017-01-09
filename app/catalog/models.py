# -*- coding: utf-8 -*-
from app import db

class Classifier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), index=True)
    tag_lv = db.Column(db.String(255), index=True)
    tag_en = db.Column(db.String(255), index=True)
    tag_ru = db.Column(db.String(255), index=True)
    skills = db.relationship('Skill', backref='classifier', lazy='dynamic')

    def __init__(self, category='', tag_en='', tag_lv='', tag_ru=''):
        self.category = category
        self.tag_en = tag_en
        self.tag_lv = tag_lv
        self.tag_ru = tag_ru

    def __repr__(self):
        return '<Classifier %d>' % self.id

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classifier_id = db.Column(db.Integer, db.ForeignKey('classifier.id'), index=True)

    def __repr__(self):
        return '<Skill %d>' % self.id


