import mysql.connector
from datetime import date, datetime


def create_connection(db):
    return mysql.connector.connect(host='manaslu.liara.cloud', user='root', password='qYpFg1HGZ2S29jBzRnIiwXBf',
                                   database=db, port=34251)


'''{'personnel_code':		None/INT,
	'shaba_number':			CHAR(26),
	'signup_time':			None/DATETIME,
 	'password':				VARCHAR(50),
	'first_name': 			VARCHAR(50),
	'last_name':			VARCHAR(50),
	'birth_date':			DATE,
	'salary':				INT,
	'department':			'marketing'/'accounting'/'finance'/'HR'/'support'/'development',
	'proficiency':			'basic'/'intermediate'/'advanced'/'proficient'/'expert',
	'education':			'none'/'high school diploma'/'associate degree'/'bachelor''s degree'/'master''s degree'/'phd',
	'position':				'department manager'/'basic employee'/'programmer',
	'profile_picture_path':	None/VARCHAR(50)}'''


def insert_employee(values):
    cnx = create_connection('baxi_staff')
    cur = cnx.cursor()
    query = '''INSERT INTO employees VALUES (%(personnel_code)s, %(shaba_number)s, %(signup_time)s,%(password)s,
											%(first_name)s, %(last_name)s, %(birth_date)s, %(salary)s, %(department)s,
											%(proficiency)s, %(education)s, %(position)s, %(profile_picture_path)s)'''
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


def insert_baar(values):
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


def insert_box(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO baxi_box VALUES (%(vehicle_license_plate)s, %(vehicle_capacity)s,
											%(vehicle_color)s, %(vehicle_name)s, %(vehicle_production_date)s,
											%(vehicle_card_photo)s, %(driver_id)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'pickup_location':	POINT,
	'pickup_province':	VARCHAR(50),
	'pickup_city':		VARCHAR(50),
	'client_id':		INT,
 	'request_time':		DATETIME}'''


def insert_request(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO service_requests VALUES (%(pickup_location)s, %(pickup_province)s
													%(pickup_city)s, %(client_id)s, %(request_time)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'tracking_code':	VARCHAR(20),
	'time':				DATETIME/None,
	'shaba_number':		CHAR(26),
	'amount':			INT,
	'state':			'failed'/'declined'/'pending'/'cancelled'/'completed'/'returned',
	'type':				'card-to-wallet'/'wallet-to-card'}'''


def insert_transaction(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO transactions VALUES (%(tracking_code)s, %(time)s, %(shaba_number)s,
												%(amount)s, %(state)s, %(type)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'id':									None/INT,
	'referral_code':						CHAR(10),
	'phone_number':							CHAR(11),
	'shaba_number':							CHAR(26),
	'wallet_balance':						INT,
	'signup_time':							DATETIME,
	'disability':							'none'/'alzheimer's disease'/'epilepsy'
											/'hearing loss'/'paralysis'/'reduced limb or finger function'
											/'weakened muscles'/'parkinson's disease'/
											'developmental disabilities'/'physical disabilities'
	'first_name':							VARCHAR(50),
	'last_name':							VARCHAR(50),
	'birth_date':							DATE,
	'national_code':						CHAR(10),
	'license_photo_path':					VARCHAR(50),
	'national_card_photo_path':				VARCHAR(50),
	'sex':									'M'/'F',
	'license_verification_date':			None/DATE,
	'judicial_letter_path':					None/VARCHAR(50),
	'judicial_letter_verification_date':	None/DATE,
	'final_verification_date':				None/DATE,
	'location':								None/POINT,
	'profile_picture_path':					None/VARCHAR(50),
	'verifier_personnel_code':				None/INT}'''


def insert_driver(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO drivers VALUES (%(id)s, %(phone_number)s,%(shaba_number)s, %(referral_code)s,
											%(wallet_balance)s, %(signup_time)s, %(disability)s, %(first_name)s,
											%(last_name)s, %(birth_date)s, %(national_code)s, %(license_photo_path)s,
											%(national_card_photo_path)s, %(sex)s, %(license_verification_date)s,
											%(judicial_letter_path)s, %(judicial_letter_verification_date)s,
											%(final_verification_date)s, %(location)s, %(profile_picture_path)s,
											%(verifier_personnel_code)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'cost':			INT,
	'round_trip':	None/'no'/'yes',
	'client_id':	INT,
	'request_time':	DATETIME}'''


def insert_trip(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO baxi_trips VALUES (%(cost)s, %(round_trip)s ,c%(client_id)s, %(request_time)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'cost':				INT,
	'cargo_weight':		INT,
	'cargo_value':		INT,
	'dropoff_location':	POINT,
	'dropoff_city':		VARCHAR(50),
	'cargo_type':		'unfragile'/'fragile',
	'client_helped':	'no'/'yes',
	'client_id':		'none'/'alzheimer''s disease'/'epilepsy',
	'request_time':		DATETIME}'''


def insert_heavy(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO heavy_transports VALUES (%(cost)s, %(cargo_weight)s, %(cargo_value)s, %(dropoff_location)s,
													%(dropoff_city)s, %(cargo_type)s, %(client_helped)s, %(client_id)s,
													%(request_time)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'cost':				INT,
	'cargo_weight':		INT,
	'cargo_value':		INT,
	'dropoff_location':	POINT,
	'dropoff_city':		VARCHAR(50),
	'insurance_cost':	INT,
	'cargo_type':		'unfragile'/'fragile',
	'client_id':		INT,
	'request_time':		DATETIME}'''


def insert_light(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO light_transports VALUES (%(cost)s, %(cargo_weight)s, %(cargo_value)s, %(dropoff_location)s,
													%(dropoff_city)s, %(insurance_cost)s, %(cargo_type)s, %(client_id)s,
													%(request_time)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'referrer_id':	INT,
	'referred_id':	INT}'''


def insert_referral(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO referrals VALUES (%(referrer_id)s, %(referred_id)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'type':				'daily'/'momentary',
	'tracking_code':	VARCHAR(20),
	'driver_id':		INT}'''


def insert_withdrawal(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO withdrawals VALUES (%(type)s, %(tracking_code)s, %(driver_id)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'tracking_code':	VARCHAR(20),
	'client_id':		INT}'''


def insert_deposit(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO deposits VALUES (%(tracking_code)s, %(client_id)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'estimated_end_time':	DATETIME,
	'end_time':				DATETIME,
	'driver_id:				INT,
	'method_of_payment':	'direct'/'cash'/'wallet-to-wallet',
	'wait_time':			'0-to-5 minutes'/'5-to-10 minutes'/'10-to-30 minutes'/'30-to-60 minutes',
	'driver_rating':		None/'0-star'/'1-star'/'2-star'/'3-star'/'4-star'/'5-star',
	'client_rating':		None/'0-star'/'1-star'/'2-star'/'3-star'/'4-star'/'5-star',
	'client_id':			INT,
	'request_time':			DATETIME,
	'tracking_code':		VARCHAR(20)}'''


def insert_acceptance(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO service_acceptances VALUES (%(estimated_end_time)s, %(end_time)s,%(driver_id)s, %(method_of_payment)s,
														%(wait_time)s, %(driver_rating)s, %(client_rating)s,
														%(client_id)s, %(request_time)s, %(tracking_code)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'description':	VARCHAR(100),
	'state':		'pending'/'under investigation'/'dismissed'/
					'driver''s account deactivated'/'client''s account deactivated',
	'client_id':	INT,
	'driver_id':	INT}'''


def insert_report(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO reports VALUES (%(description)s, %(state)s, %(client_id)s, %(driver_id)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'location':		POINT,
	'client_id':	INT,
	'address_name':	VARCHAR(50)}'''


def insert_address(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO addresses VALUES (%(location)s, %(client_id)s, %(address_name)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'city':			VARCHAR(50),
	'client_id':	INT,
	'request_time':	DATETIME,
	'latitude':		INT
	'longitude':	INT}'''


def insert_destination(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO destinations VALUES (%(city)s, %(client_id)s, %(request_time)s,
				%(latitude)s, %(longitude)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'client_id':	INT,
	'request_time':	DATETIME,
	'point':		baxi:
					'safe driving'/'enjoyable music'/
					box and baar:
					'safe shipment'/
					all:
					'neat vehicle'/'respectful behavior'/
					'punctuality'/'proper routing'/'moderate temperature'}'''


def insert_compliment(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO compliments VALUES (%(client_id)s, %(request_time)s, %(point)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'client_id':	INT,
	'request_time':	DATETIME,
	'point':		baxi:
					'dangerous driving'/'immoderate temperature'/
					box and baar:
					'unsafe shipment'/
					all:
					'improper routing'/'demand for extra money'/
					'demand for cash payment'/'discrepancy in description'/
					'disrespectful behavior'/'poor vehicle condition'/unpunctuality'}'''


def insert_complaint(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO complaints VALUES (%(client_id)s, %(request_time)s, %(point)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'amount':					INT,
	'time':						DATETIME,
	'type':						'reward'/'fuel quota',
	'employee_personnel_code':	INT,
	'driver_id':				INT}'''


def insert_company_deposit(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO company_deposits VALUES (%(amount)s, %(time)s,%(type)s, %(employee_personnel_code)s, %(driver_id)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'tracking_code':	VARCHAR(20),
	'driver_id':		INT}'''


def insert_compensatory_deposit(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO compensatory_deposits VALUES (%(tracking_code)s, %(driver_id)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()


'''{'client_id':		None/INT,
	'phone_number':		CHAR(11),
	'wallet_balance':	INT,
	'signup_time':		DATETIME,
	'first_name':		VARCHAR(50),
	'last_name':		VARCHAR(50),
	'birth_date':		DATE,
	'sex':				'M'/'F',
	'email':			None/VARCHAR(50)}'''


def insert_client(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO clients VALUES (%(client_id)s, %(phone_number)s, %(wallet_balance)s, %(signup_time)s,
											%(first_name)s, %(last_name)s, %(birth_date)s, %(sex)s, %(email)s)'''
    cur.execute(query, values)
    cnx.commit()
    cnx.close()

def query1():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT       D.*
                FROM		drivers D, baxi B, baxi_baar BB
                WHERE		(D.id = B.driver_id AND B.vehicle_color  = 'blue' AND B.vehicle_name  LIKE '%pride%') OR 
			                (D.id = BB.driver_id AND B.vehicle_color = 'blue' AND BB.vehicle_name LIKE '%pride%'))'''
    cur.execute(query)
    result = cur.fetchall()
    cnx.close()
    return result

def query2():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT		drivers.*
                FROM		drivers JOIN baxi ON id = driver_id
                WHERE 		D.sex = 'F' AND vehicle_color = 'blue' AND TIMESTAMPDIFF(YEAR, birth_date,CURDATE()) > 30'''
    cur.execute(query)
    result = cur.fetchall()
    cnx.close()
    return result


def query4():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT		c.*
				FROM		clients c join addresses
				USING		(client_id)
				WHERE		wallet_balance > 50
				GROUP BY	c.client_id, phone_number, wallet_balance, signup_time, first_name, last_name, birth_date, sex, email
				HAVING		COUNT(*) >= 2'''
    cur.execute(query)
    result = cur.fetchall()
    cnx.close()
    return result


'''	sign-in phone number lookup
	return format: tuple(id, wallet_balance, first_name, last_name, profile_picture_path)'''


def client_phone_number_lookup(number):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT	id, wallet_balance, first_name, last_name
				FROM	clients
				WHERE	phone_number = %s'''
    cur.execute(query, (number,))
    result = cur.fetchall()
    cnx.close()
    return result


def driver_phone_number_lookup(number):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT	id, wallet_balance, first_name, last_name, profile_picture_path
				FROM	drivers
				WHERE	phone_number = %s'''
    cur.execute(query, (number,))
    result = cur.fetchall()
    cnx.close()
    return result


# call after driver sign-in
def update_location(driver_id, location):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	drivers
				SET		location = %s
				WHERE	id = %s'''
    cur.execute(query, (location, driver_id))
    cur.commit()
    cnx.close()


# return format: tuple(first_name, last_name, request_time, end_time, method_of_payment, driver_rating, client_rating, wait_time)
def driver_service_history(id):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT	first_name, last_name, request_time, end_time, method_of_payment, driver_rating, client_rating, wait_time
				FROM	service_acceptances JOIN clients ON client_id = id
				WHERE	driver_id = %s'''
    cur.execute(query, (id,))
    result = cur.fetchall()
    cnx.close()
    return result


# return format: tuple(first_name, last_name, request_time, end_time, method_of_payment, driver_rating, client_rating, wait_time)
def client_service_history(id):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT	first_name, last_name, request_time, end_time, method_of_payment, driver_rating, client_rating, wait_time
				FROM	service_acceptances JOIN drivers ON driver_id = id
				WHERE	client_id = %s'''
    cur.execute(query, (id,))
    result = cur.fetchall()
    cnx.close()
    return result


# return format: tuple(address_name, location)
def client_favorites(id):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT	address_name, location
				FROM	addresses
				WHERE	client_id = %s'''
    cur.execute(query, (id,))
    result = cur.fetchall()
    cnx.close()
    return result


''' side panel information
	return format: tuple(email, sex, birth_date, phone_number)'''


def client_panel_info(id):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT	email, sex, birth_date, phone_number
				FROM	clients
				WHERE	id = %s'''
    cur.execute(query, (id,))
    result = cur.fetchall()
    cnx.close()
    return result


''' on service acceptance
	return format: tuple(first_name, last_name, phone_number, vehicle_license_plate, vehicle_name, vehicle_production_date, vehicle_color, vehicle_capacity)'''


def baxi_driver_info(id):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT	first_name, last_name, phone_number, vehicle_license_plate, vehicle_name, vehicle_production_date, vehicle_color, vehicle_capacity
				FROM	drivers JOIN baxi ON id = driver_id
				WHERE	id = %s'''
    cur.execute(query, (id,))
    result = cur.fetchall()
    cnx.close()
    return result


''' on service acceptance
	return format: tuple(first_name, last_name, phone_number, vehicle_license_plate, vehicle_name, vehicle_production_date, vehicle_color, vehicle_capacity)'''


def baar_driver_info(id):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT	first_name, last_name, phone_number, vehicle_license_plate, vehicle_name, vehicle_production_date, vehicle_color, vehicle_capacity
				FROM	drivers JOIN baxi_baar ON id = driver_id
				WHERE	id = %s'''
    cur.execute(query, (id,))
    result = cur.fetchall()
    cnx.close()
    return result


''' on service acceptance
	return format: tuple(first_name, last_name, phone_number, vehicle_license_plate, vehicle_name, vehicle_production_date, vehicle_color, vehicle_capacity)'''


def box_driver_info(id):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT	first_name, last_name, phone_number, vehicle_license_plate, vehicle_name, vehicle_production_date, vehicle_color, vehicle_capacity
				FROM	drivers JOIN baxi_box ON id = driver_id
				WHERE	id = %s'''
    cur.execute(query, (id))
    result = cur.fetchall()
    cnx.close()
    return result


def is_manager(pcode):
    cnx = create_connection('baxi_staff')
    cur = cnx.cursor()
    query = """SELECT	personnel_code
				FROM	employees
				WHERE	personnel_code = %s AND department = 'HR' AND position = 'department manager'"""
    cur.execute(query, (pcode,))
    result = cur.fetchall()
    cnx.close()
    return result


''' called upon employee sign-in attempt
	return format: tuple(first_name, last_name)'''


def employee_info(pcode, password):
    cnx = create_connection('baxi_staff')
    cur = cnx.cursor()
    query = '''SELECT	first_name, last_name
				FROM	employees
				WHERE	personnel_code = %s AND password = %s'''
    cur.execute(query, (pcode, password))
    result = cur.fetchall()
    cnx.close()
    return result


def get_unverified_drivers():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT	*
				FROM	drivers
				WHERE	verifier_personnel_code IS NULL'''
    cur.execute(query)
    result = cur.fetchall()
    cnx.close()
    return result


def set_license_verification_date(id, date):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	drivers
				SET		licensce_verification_date = %s
				WHERE	id = %s'''
    cur.execute(query, (date, id))
    cur.commit()
    cnx.close()


def set_judicial_letter_path(id, path):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	drivers
				SET		judicial_letter_path = %s
				WHERE	id = %s'''
    cur.execute(query, (path, id))
    cur.commit()
    cnx.close()


def set_judicial_letter_verification_date(id, date):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	drivers
				SET		judicial_letter_verification_date = %s
				WHERE	id = %s'''
    cur.execute(query, (date, id))
    cur.commit()
    cnx.close()


def set_judicial_letter_verification_date(id, date):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	drivers
				SET		judicial_letter_verification_date = %s
				WHERE	id = %s'''
    cur.execute(query, (date, id))
    cur.commit()
    cnx.close()


def set_final_verification_date(id, date):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	drivers
				SET		final_verification_date = %s
				WHERE	id = %s'''
    cur.execute(query, (date, id))
    cur.commit()
    cnx.close()


def set_verifier_personnel_code(id, code):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	drivers
				SET		verifier_personnel_code = %s
				WHERE	id = %s'''
    cur.execute(query, (code, id))
    cur.commit()
    cnx.close()


def set_employee_pppath(pcode, path):
    cnx = create_connection('baxi_staff')
    cur = cnx.cursor()
    query = '''UPDATE	employees
				SET		profile_picture_path = %s
				WHERE	personnel_code = %s'''
    cur.execute(query, (path, pcode))
    cur.commit()
    cnx.close()


def set_driver_pppath(id, path):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	drivers
				SET		profile_picture_path = %s
				WHERE	id = %s'''
    cur.execute(query, (path, id))
    cur.commit()
    cnx.close()


def set_email(id, path):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	clients
				SET		email = %s
				WHERE	id = %s'''
    cur.execute(query, (path, id))
    cur.commit()
    cnx.close()


def is_female(id):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = """SELECT	id
				FROM	drivers
				WHERE	id = %s AND sex = 'F'"""
    cur.execute(query, (id,))
    result = cur.fetchall()
    cnx.close()
    return result


def is_driver_account_inactive(id):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = """SELECT	id
				FROM	drivers JOIN reports ON id = driver_id
				WHERE	id = %s AND (verifier_personnel_code IS NULL OR state = 'driver''s account deactivated)'"""
    cur.execute(query, (id,))
    result = cur.fetchall()
    cnx.close()
    return result


def is_client_account_inactive(id):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = """SELECT	id
				FROM	clients JOIN reports ON id = client_id
				WHERE	id = %s AND state = 'client''s account deactivated'"""
    cur.execute(query, (id,))
    result = cur.fetchall()
    cnx.close()
    return result


def ref_code_exists(code):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = """SELECT	id
				FROM	drivers
				WHERE	referral_code = %s"""
    cur.execute(query, (code,))
    result = cur.fetchall()
    cnx.close()
    return result


def requests_within_range(lat, lon):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = """SELECT	first_name, last_name, pickup_location, pickup_province, pickup_city, city, latitude, longitude
				FROM	(service_requests JOIN clients ON client_id = id) JOIN destinations USING (client_id, request_time)
				WHERE	(6371 * acos(cos(radians(%s)) * cos(radians(ST_Y(pickup_location))) * cos(radians(ST_X(pickup_location))) - radians(%s)) + sin(radians(%s)) * sin(radians(ST_Y(pickup_location)))) <= 5"""
    cur.execute(query, (lat, lon, lat))
    result = cur.fetchall()
    cnx.close()
    return result
