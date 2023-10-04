from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

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
def load_jobs_fromdb():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs_db = []
    for row in result.all():
      jobs_db.append(dict(row._asdict()))
  return jobs_db

  

@app.route("/")
def hello_world():
  jobs = load_jobs_fromdb()
  return render_template('home.html',
                        jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs_l)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)