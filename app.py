from flask import Flask, render_template, jsonify, request
from database import load_jobs_fromdb, load_job_fromdb, add_application_to_db

app = Flask(__name__)
'''
jobs_l = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'India',
    'salary': 'rs.1000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'India',
    'salary': 'rs.1500'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'rs.1200'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco',
    'salary':'rs.1900'
  }
]
'''


  

@app.route("/")
def hello_world():
  jobs = load_jobs_fromdb()
  return render_template('home.html',
                        jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_fromdb()
  return jsonify(jobs)

@app.route("/jobs/<id>")
def show_job(id):
  job = load_job_fromdb(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html',
                        job=job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form   #args get from url
  job = load_job_fromdb(id)
  
  add_application_to_db(id, data)
  return render_template('application_submitted.html',
                        application=data,
                        job=job)

  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)