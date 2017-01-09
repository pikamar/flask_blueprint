# -*- coding: utf-8 -*-
from flask import Blueprint
from app import db, manager, admin
from app.catalog.models import Classifier, Skill
from flask.ext.admin.contrib.sqla import ModelView

catalog = Blueprint('catalog', __name__)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Classifier, methods=['GET'], results_per_page=None, exclude_columns=['skills'])

admin.add_view(ModelView(Classifier, db.session))

