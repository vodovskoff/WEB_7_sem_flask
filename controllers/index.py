from app import app
from flask import render_template, request
import constants
@app.route('/', methods=['GET'])
def index():
 name=None
 gender=None
 program_id = -1
 submit=None
 subjects_select = list()
 olympiads_select = list()
 subject_id=list()
 olympiad_id=list()

 subject_id1=list()
 olympiad_id1=list()




 if(request.values.get('submit')):
  name = request.values.get('username')
  submit = request.values.get('submit')
  gender = request.values.get('gender')
  program_id = request.values.get('program')
  subject_id = request.values.getlist('subject[]')
  for sub in subject_id:
   subject_id1.append(int(sub))
  subjects_select = [constants.subjects[int(i)] for i in subject_id]
  olympiad_id = request.values.getlist('olympiads[]')
  for olym in olympiad_id:
   olympiad_id1.append(int(olym))
  olympiads_select = [constants.olympiads[int(i)] for i in olympiad_id]

 print(subject_id)
 html = render_template(
  'index.html',
  program_list=constants.programs,
  subject_list=constants.subjects,
  olympiads_list=constants.olympiads,
  len=len,
  name=name,
  submit=submit,
  gender=gender,
  program = constants.programs[int(program_id)],
  subjects_select = subjects_select,
  olympiads_select=olympiads_select,
  program_id=int(program_id),
  subject_id=subject_id1,
  olympiad_id=olympiad_id1
 )
 return html