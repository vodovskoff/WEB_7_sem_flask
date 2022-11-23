import constants
from app import app
from flask import render_template, request
@app.route('/olympiad/<sub>')
def olympiad(sub):
    html = render_template(
    'olympiad.html',
    sub = sub,
    discription = constants.olympiads_dict[sub]
    )
    return html