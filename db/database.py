import mysql.connector
from datetime import date, datetime

def create_connection(db):
	return mysql.connector.connect(host='localhost', user='root', password='assambalers', database='baxi_staff')

'''{'personnel_code':		None/INT,
	'shaba_number':			CHAR(26),
 	'password':				VARCHAR(50),
	'first_name': 			VARCHAR(50),
	'last_name':			VARCHAR(50),
	'birth_date':			DATE,
	'salary':				INT,
	'signup_time':			DATETIME,
	'department':			'marketing'/'accounting'/'finance'/'HR'/'support'/'development'
	'proficiency':			'basic'/'intermediate'/'advanced'/'proficient'/'expert'
	'education':			'none'/'high school diploma'/'associate degree'/'bachelor''s degree'/'master''s degree'/'phd'
	'position':				'department manager'/'basic employee'/'programmer'
	'profile_picture_path':	VARCHAR(50)}'''
def insert_employee(values):
	cnx = create_connection('baxi_staff')
	cur = cnx.cursor()
	query = '''INSERT INTO employees VALUES (%(personnel_code)s, %(shaba_number)s,
			%(password)s, %(first_name)s, %(last_name)s, %(birth_date)s, %(salary)s,
			%(department)s, %(signup_time)s, %(proficiency)s, %(education)s,
			%(position)s, %(profile_picture_path)s)'''
	cur.execute(query, values)
	cnx.commit()
	cnx.close()

