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

'''{'tracking_code':	VARCHAR(20),
	'time':				DATETIME/None,
	'shaba_number':		CHAR(26),
	'amount':			INT,
	'state':			None/'failed'/'declined'/'pending'/'cancelled'/'completed'/'returned',
	'type':				'card-to-wallet'/'wallet-to-card'}'''			 
def insert_transaction(values):
	cnx = create_connection('baxi_users')
	cur = cnx.cursor()
	query = '''INSERT INTO transactions VALUES (%(tracking_code)s, %(time)s,
				%(shaba_number)s, %(amount)s, %(state)s, %(type)s)'''
	cur.execute(query, values)
	cnx.commit()
	cnx.close()

'''{'id':									INT,
	'phone_number':							CHAR(11),
	'shaba_number':							CHAR(26),
	'referral_code':						CHAR(10),
	'wallet_balance':						INT,
	'disability':							None/'none'/'alzheimer''s disease'/'epilepsy'
											/hearing loss'/'paralysis'/'reduced limb or finger function'
											/'weakened muscles'/'parkinson's disease'/
											'developmental disabilities'/'physical disabilities'
	'first_name':							VARCHAR(50),
	'last_name':							VARCHAR(50),
	'birth_date':							DATE,
	'national_code':						CHAR(10),
	'license_photo_path':					VARCHAR(50),
	'national_card_photo_path':				VARCHAR(50),
	'license_verification_date':			DATE,
	'judicial_letter_path' :				VARCHAR(50),
	'judicial_letter_verification_date':	DATE,
	'final_verification_date':				DATE,
	'signup_time':							DATETIME/None,
	'sex':									None/'M'/'F',
	'profile_picture_path':					VARCHAR(50),
	'verifier_personnel_code':				INT}'''
def insert_driver(values):
	cnx = create_connection('baxi_users')
	cur = cnx.cursor()
	query = '''INSERT INTO drivers VALUES (%(id)s, %(phone_number)s,%(shaba_number)s, %(referral_code)s,
											%(wallet_balance)s, %(disability)s, %(first_name)s, %(last_name)s, %(birth_date)s, 
											%(national_code)s, %(license_photo_path)s, %(national_card_photo_path)s,
											%(license_verification_date)s, %(judicial_letter_path)s, %(judicial_letter_verification_date)s,
											%(final_verification_date)s, %(signup_time)s, %(sex)s, %(profile_picture_path)s,
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
	query = '''INSERT INTO baxi_trips VALUES (%(cost)s, %(round_trip)s,%(client_id)s, %(request_time)s)'''
	cur.execute(query, values)
	cnx.commit()
	cnx.close()

'''{'cost':				INT,
	'cargo_weight':		INT,
	'cargo_value':		INT,
	'cargo_type':		None/'unfragile'/'fragile',
	'client_helped':	None/'no'/'yes',
	'client_id':		None/'none'/'alzheimer''s disease'/'epilepsy',
	'request_time':		DATETIME}'''
def insert_heavy(values):
	cnx = create_connection('baxi_users')
	cur = cnx.cursor()
	query = '''INSERT INTO heavy_transports VALUES (%(cost)s, %(cargo_weight)s,%(cargo_value)s, %(cargo_type)s,
													%(client_helped)s, %(client_id)s, %(request_time)s)'''
	cur.execute(query, values)
	cnx.commit()
	cnx.close()

'''{'cost':				INT,
	'cargo_weight':		INT,
	'cargo_value':		INT,
	'insurance_cost':	INT,
	'cargo_type':		None/'unfragile'/'fragile',
	'client_id':		INT,
	'request_time':		DATETIME}'''
def insert_light(values):
	cnx = create_connection('baxi_users')
	cur = cnx.cursor()
	query = '''INSERT INTO light_transports VALUES (%(cost)s, %(cargo_weight)s,%(cargo_value)s, %(insurance_cost)s,
													%(cargo_type)s, %(client_id)s, %(request_time)s)'''
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

'''{'type':				None/'daily'/'momentary',
	'tracking_code':	VARCHAR(20),
	'driver_id':		INT}'''
def insert_withdrawal(values):
	cnx = create_connection('baxi_users')
	cur = cnx.cursor()
	query = '''INSERT INTO withdrawals VALUES (%(type)s, %(tracking_code)s,%(driver_id)s)'''
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
	'driver_rating':		None/'0-star'/'1-star'/'2-star'/'3-star'/'4-star'/'5-star',
	'client_rating':		None/'0-star'/'1-star'/'2-star'/'3-star'/'4-star'/'5-star',
	'wait_time':			None/'0-to-5 minutes'/'5-to-10 minutes'/'10-to-30 minutes'/'30-to-60 minutes',
	'client_id':			INT,
	'request_time':			DATETIME,
	'tracking_code':		VARCHAR(20)}'''
def insert_acceptance(values):
	cnx = create_connection('baxi_users')
	cur = cnx.cursor()
	query = '''INSERT INTO service_acceptances VALUES (%(estimated_end_time)s, %(end_time)s,%(driver_id)s, %(method_of_payment)s,
														%(driver_rating)s, %(client_rating)s, %(wait_time)s,
														%(client_id)s, %(request_time)s, %(tracking_code)s)'''
	cur.execute(query, values)
	cnx.commit()
	cnx.close()

'''{'description':	VARCHAR(100),
	'state':		None/'pending'/'under investigation'/'dismissed'/
					'driver''s account deactivated'/'client''s account deactivated',
	'client_id':	INT,
	'driver_id':	INT}'''
def insert_report(values):
	cnx = create_connection('baxi_users')
	cur = cnx.cursor()
	query = '''INSERT INTO reports VALUES (%(description)s, %(state)s,%(client_id)s, %(driver_id)s)'''
	cur.execute(query, values)
	cnx.commit()
	cnx.close()

'''{'location':		POINT,
	'client_id':	INT,
	'address_name':	VARCHAR(50)}'''
def insert_address(values):
	cnx = create_connection('baxi_users')
	cur = cnx.cursor()
	query = '''INSERT INTO addresses VALUES (%(location)s, %(client_id)s,%(address_name)s)'''
	cur.execute(query, values)
	cnx.commit()
	cnx.close()

'''{'client_id':	INT,
	'request_time':	DATETIME,
	'location':		POINT}'''
def insert_destination(values):
	cnx = create_connection('baxi_users')
	cur = cnx.cursor()
	query = '''INSERT INTO destinations VALUES (%(client_id)s, %(request_time)s,%(location)s)'''
	cur.execute(query, values)
	cnx.commit()
	cnx.close()

'''{'client_id':	INT,
	'request_time':	DATETIME,
	'point':		None/
					baxi:
					'safe driving'/'enjoyable music'/
					box and baar:
					'safe shipment'/
					all:
					'neat vehicle'/'respectful behavior'/
					'punctuality'/'proper routing'/'moderate temperature'}'''
def insert_compliment(values):
	cnx = create_connection('baxi_users')
	cur = cnx.cursor()
	query = '''INSERT INTO compliments VALUES (%(client_id)s, %(request_time)s,%(point)s)'''
	cur.execute(query, values)
	cnx.commit()
	cnx.close()

'''{'client_id':	INT,
	'request_time':	DATETIME,
	'point':		None/
					baxi:
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
	query = '''INSERT INTO complaints VALUES (%(client_id)s, %(request_time)s,%(point)s)'''
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
	query = '''INSERT INTO company_deposits VALUES (%(amount)s, %(time)s,%(type)s, %(employee_personnel_code)s,%(driver_id)s)'''
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
