import mysql.connector
from datetime import date, datetime

def create_connection(db):
	return mysql.connector.connect(host='localhost', user='root', password='assambalers', database='baxi_staff')

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

'''insert_employee({'personnel_code': None,
				 'shaba_number': '1',
				 'password': '72126',
				 'first_name': 'arishiamionio',
				 'last_name': 'dehghanio',
				 'birth_date': date(2002, 9, 15),
				 'salary': 5000,
				 'department': 'sails',
				 'signup_time': datetime.now().date(),
				 'proficiency': 'basic',
				 'education': 'none',
				 'position': 'basic employee',
				 'profile_picture_path': None,})'''
