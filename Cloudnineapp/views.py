from flask import Blueprint, render_template, request, session, flash
from flask import redirect, url_for



bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')