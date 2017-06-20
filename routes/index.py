# -*- coding: utf-8 -*-
from flask import (
    render_template,
    request,
    flash,
    redirect,
    url_for,
    Blueprint,
)

main = Blueprint('index', __name__)

@main.route('/')
def index():
	return  render_template('index.html')