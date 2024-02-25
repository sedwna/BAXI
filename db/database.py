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
	'signup_time':			None/DATETIME,
	'department':			'marketing'/'accounting'/'finance'/'HR'/'support'/'development',
	'proficiency':			'basic'/'intermediate'/'advanced'/'proficient'/'expert',
	'education':			'none'/'high school diploma'/'associate degree'/'bachelor''s degree'/'master''s degree'/'phd',
	'position':				'department manager'/'basic employee'/'programmer',
	'profile_picture_path':	None/VARCHAR(50)}'''
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

'''{'vehicle_license_plate':	CHAR(9),
	'vehicle_capacity':			INT,
 	'vehicle_color':			VARCHAR(50),
	'vehicle_name': 			VARCHAR(50),
	'vehicle_production_date':	DATE,
	'vehicle_card_photo':		VARCHAR(50),
	'vehicle_fuel_type':		'gasoline'/'CNG'/'dual'/'electricity',
	'driver_id':				INT}'''
def insert_baxi(values):
	cnx = create_connection('baxi_users')
	cur = cnx.cursor()
	query = '''INSERT INTO baxi VALUES (%(vehicle_license_plate)s, %(vehicle_capacity)s,
			%(vehicle_color)s, %(vehicle_name)s, %(vehicle_production_date)s,
			%(vehicle_card_photo)s, %(vehicle_fuel_type)s, %(driver_id)s)'''
	cur.execute(query, values)
	cnx.commit()
	cnx.close()

'''{'vehicle_license_plate':	CHAR(9),
	'vehicle_capacity':			INT,
 	'vehicle_color':			VARCHAR(50),
	'vehicle_name': 			VARCHAR(50),
	'vehicle_production_date':	DATE,
	'vehicle_card_photo':		VARCHAR(50),
	'vehicle_fuel_type':		'gasoline'/'CNG'/'dual'/'electricity',
	'driver_id':				INT}'''
def insert_baxi_baar(values):
	cnx = create_connection('baxi_users')
	cur = cnx.cursor()
	query = '''INSERT INTO baxi_baar VALUES (%(vehicle_license_plate)s, %(vehicle_capacity)s,
			%(vehicle_color)s, %(vehicle_name)s, %(vehicle_production_date)s,
			%(vehicle_card_photo)s, %(vehicle_fuel_type)s, %(driver_id)s)'''
	cur.execute(query, values)
	cnx.commit()
	cnx.close()

'''{'vehicle_license_plate':	CHAR(9),
	'vehicle_capacity':			INT,
 	'vehicle_color':			VARCHAR(50),
	'vehicle_name': 			VARCHAR(50),
	'vehicle_production_date':	DATE,
	'vehicle_card_photo':		VARCHAR(50),
	'driver_id':				INT}'''
def insert_baxi_box(values):
	cnx = create_connection('baxi_users')
	cur = cnx.cursor()
	query = '''INSERT INTO baxi_box VALUES (%(vehicle_license_plate)s, %(vehicle_capacity)s,
			%(vehicle_color)s, %(vehicle_name)s, %(vehicle_production_date)s,
			%(vehicle_card_photo)s, %(driver_id)s)'''
	cur.execute(query, values)
	cnx.commit()
	cnx.close()

'''{'pickup_location':	POINT,
	'client_id':		INT,
 	'request_time':		DATETIME}'''
def insert_request(values):
	cnx = create_connection('baxi_users')
	cur = cnx.cursor()
	query = '''INSERT INTO service_requests VALUES (%(pickup_location)s, %(client_id)s,
			%(request_time)s)'''
	cur.execute(query, values)
	cnx.commit()
	cnx.close()
