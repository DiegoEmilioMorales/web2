
from sqlalchemy import create_engine, text

#my_secret = os.environ['DB_CONNECTION_STRING']
#db_string = os.environ['DB_CONNECTION_STRING']


db_string = "mysql+pymysql://xlfq1bklw70z9b61aygu:pscale_pw_c4O3R0auYyvto4cLQyfRJlLdYVgQoQ51u459CVdi5W@gcp-us-central1.connect.psdb.cloud/diegocarrers?charset=utf8mb4"
engine = create_engine(db_string,
                      connect_args={
                        "ssl":{"ssl_ca":""}})

def load_jobs_fromdb():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs_db = []
    for row in result.all():
      jobs_db.append(dict(row._asdict()))
  return jobs_db

def load_job_fromdb(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id = {id}"))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0]._asdict())

def add_application_to_db(job_id, data):
  with engine.connect() as conn:

    query = text(f"INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES ({job_id}, '{data['full_name']}', '{data['email']}', '{data['linkedin_url']}', '{data['education']}', '{data['work_experience']}', '{data['resume_url']}')")

    conn.execute(query)



'''
with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))

  result_dicts = []

  for row in result.all():
    result_dicts.append(dict(row._asdict()))

  print(result_dicts)

    print(type(result))
    result_all = result.all()
    #result_li = result.all()
    print("\n")
    print(type(result_all))
    first = result_all[0]
    print(type(first))
    first_dic = dict(result_all[0]._asdict())
    print("first_dic type:", type(first_dic))
    print(first_dic)
    '''
