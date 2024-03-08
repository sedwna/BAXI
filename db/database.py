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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
    cnx.close()


'''{'referrer_id':	INT,
	'referred_id':	INT}'''


def insert_referral(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO referrals VALUES (%(referrer_id)s, %(referred_id)s)'''
    cur.execute(query, values)
    cnx.commit()
    cur.close()
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
    cur.close()
    cnx.close()


'''{'tracking_code':	VARCHAR(20),
	'client_id':		INT}'''


def insert_deposit(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO deposits VALUES (%(tracking_code)s, %(client_id)s)'''
    cur.execute(query, values)
    cnx.commit()
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
    cnx.close()


'''{'tracking_code':	VARCHAR(20),
	'driver_id':		INT}'''


def insert_compensatory_deposit(values):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''INSERT INTO compensatory_deposits VALUES (%(tracking_code)s, %(driver_id)s)'''
    cur.execute(query, values)
    cnx.commit()
    cur.close()
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
    cur.close()
    cnx.close()

def pyramid_query(id):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''WITH RECURSIVE pyramid (referrer_id, referred_id, factor) AS	(
																				SELECT		referrer_id, referred_id, CAST(0.1 AS FLOAT)
																				FROM		referrals
																				WHERE		referred_id = %s
																				UNION ALL
																				SELECT		r.referrer_id, r.referred_id, factor / 2
																				FROM		referrals r JOIN pyramid ON r.referred_id = pyramid.referrer_id
																			)
																			select * from pyramid;'''
    cur.execute(query, (id,))
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result

def query1():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT       D.*
                FROM		drivers D, baxi B, baxi_baar BB
                WHERE		(D.id = B.driver_id AND B.vehicle_color  = 'blue' AND B.vehicle_name  LIKE '%pride%') OR 
			                (D.id = BB.driver_id AND B.vehicle_color = 'blue' AND BB.vehicle_name LIKE '%pride%'))'''
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
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
    cur.close()
    cnx.close()
    return result

def query3():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT 		first_name, last_name, license_verification_date, judicial_letter_verification_date, final_verification_date
                FROM		drivers JOIN baxi_baar ON id = driver_id
                WHERE		vehicle_name LIKE '%vanet%' AND final_verification_date IS NOT NULL'''
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
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
    cur.close()
    cnx.close()
    return result

def query5():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT       time
                FROM		
                (
	                SELECT 		DATE(request_time) time, COUNT(*) no
	                FROM		baxi_trips JOIN clients ON client_id = id
	                WHERE		round_trip = 'yes' AND TIMESTAMPDIFF(YEAR, birth_date,CURDATE()) BETWEEN 15 AND 18
	                GROUP BY	DATE(request_time)
                )
                HAVING		MIN(no) = no'''
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result

def query6():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT       first_name , last_name, wallet_balance
                FROM		service_acceptances JOIN drivers ON driver_id = id
                WHERE 		DATE(request_time) = '2024-01-01'
                GROUP BY	first_name, last_name, wallet_balance, driver_id
                HAVING 	COUNT(*) >= 2'''
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result

def query7():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT		C.first_name, C.last_name, SUM(cost)
                FROM		clients C,
                (
	                SELECT		client_id, request_time, cost
	                FROM		service_acceptances NATURAL JOIN baxi_trips
	                WHERE		YEARWEEK(request_time) = YEARWEEK(CURDATE()) AND TIMESTAMPDIFF(HOUR, end_time, request_time) > 2
                ) TARGET
                WHERE		TARGET.client_id = C.id
                GROUP BY	C.first_name, C.last_name, C.id'''
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result

def query8():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT		NV.first_name, NV.last_name, TIMESTAMPDIFF(YEAR, NV.birth_date,CURDATE()) Age
                FROM
                (
	                SELECT		D.*
                    FROM		drivers D, baxi_baar BB
                    WHERE		BB.vehicle_fuel_type = 'CNG' AND D.disability = 'hearing loss' AND BB.vehicle_name LIKE '%vanet%' AND D.id = BB.driver_id
                    HAVING		TIMESTAMPDIFF(YEAR, D.birth_date, CURDATE()) > (SELECT AVG(TIMESTAMPDIFF(YEAR, birth_date, CURDATE()))      FROM drivers)
                ) NV,
                (
                    SELECT		COUNT(*) no
                    FROM		service_acceptances NATRUAL JOIN baxi_trips
                    WHERE		vehicle_capacity >= 4
                ) Z4
                GROUP BY	NV.first_name, NV.last_name, NV.birth_date, NV.id
                HAVING		COUNT(*) > Z4'''
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result

def query9():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT		vehicle_license_plate, first_name, last_name
                FROM		((heavy_transports NATRUAL JOIN service_acceptances) NATURAL JOIN baxi_baar) JOIN drivers ON driver_id = id
                WHERE		cargo_value <= 50000000 AND cargo_type = 'fragile'''
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result

def query10():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT		C.last_name, C.phone_number, C.email
                FROM		clients C, 
                (
                    SELECT		C2.id, DATE(A.request_time), COUNT(*) no
                    FROM		clients C2 JOIN service_acceptances A ON C2.id = A.client_id
                    WHERE		DATE(A.request_time) BETWEEN '2024-02-21' AND '2024-01-01'	
                    GROUP BY	DATE(A.request_time)		
                ) BETDAT
                WHERE		(C.first_name LIKE '%Piotr%' OR C.last_name LIKE '%Piotr%') AND C.sex = 'M' AND C.id IN 
                            (
                                SELECT		BDT.id
                                FROM		BETDAT BDT,
                                (
                                    SELECT 		COUNT(*) no
                                    FROM		destinations D	
                                    WHERE		DATE(D.request_time) BETWEEN '2024-02-21' AND '2024-01-01'
                                    GROUP BY	D.client_id, DATE(D.request_time)
                                    HAVING		COUNT(*) >= 2
                                ) MULTID
                                HAVING		MAX(BDT.no) > MAX(MULTID.no)
                            )'''
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result

def query11():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT		C.*
                FROM		clients C JOIN accepteances A on C.id = A.client_id,
                (
                    SELECT		client_id
                    FROM		(clients JOIN deposits ON id = client_id) NATRUAL JOIN transactoins
                    GROUP BY	client_id
                    HAVING		SUM(amount) > 100000
                )MONEY
                WHERE		C.id IN MONEY AND TIMESTAMPDIFF(HOUR, request_time, A.end_time) >= 1
                GROUP BY	C.id
                HAVING 		COUNT(*) <= 2'''
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result

def query12():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT		P/COUNT(T.*)
                FROM		reports T,
                (
                    SELECT		COUTN(*) * 100
                    FROM		reports
                    WHERE		state = 'driver''s account deactivated' OR state = 'client''s account deactivated' OR state = 'dismissed'
                ) P'''
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result

def query13():
    cnx = create_connection('baxi_staff')
    cur = cnx.cursor()
    query = '''SELECT		COUNT(*) No
                FROM		employees
                WHERE		positoin <> 'department manager' AND salary > 5000000 AND education >= 'bachelor''s degree'
                            AND TIMESTAMPDIFF(YEAR, signup_time, CURDATE()) >= 1'''
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result

def query14():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT		SUM(cost), first_name, last_name, vehicle_name
                FROM	
                (
                    SELECT      driver_id, cost, vehicle_name
                    FROM
                    (
                        SELECT	    driver_id, cost, vehicle_name, COUNT(*) no
                        FROM		(service_acceptances NATURAL JOIN baxi_trips) NATURAL  JOIN baxi
                        WHERE		vehicle_production_date < '2009-00-00' AND method_of_payment = 'cash'
                    )
                    ORDER BY	no
                    LIMIT		3
                ) JOIN drivers ON driver_id = id
                GROUP BY	driver_id'''
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result

def query15():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = """SELECT		cancelled / successful AS ratio
				FROM		(
								SELECT		COUNT(*) AS successful
								FROM		service_requests JOIN service_acceptances USING (client_id, request_time)
								WHERE		pickup_province = 'tehran' AND pickup_city = 'rey'
							),
							(
								SELECT		COUNT(*) AS cancelled
								FROM		(
												SELECT		client_id, request_time
												FROM		service_requests
												WHERE		pickup_province = 'tehran' AND pickup_city = 'rey'
											)
											EXCEPT
											(
												SELECT		sr.client_id, sr.request_time
												FROM		service_requests sr JOIN service_acceptances USING (client_id, request_time)
												WHERE		pickup_province = 'tehran' AND pickup_city = 'rey'
											)
							)"""
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result

def query16():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT			D.*
                FROM
                (
                    SELECT		driver_id, 
                                MAX(TIMEDIFF(estimated_end_time, end_time)) T
                    FROM		service_acceptances NATRUAL JOIN baxi_box
                    GROUP BY	driver_id
                ) JOIN drivers D ON driver_id = id
                GROUP BY	driver_id 
                ORDER BY	T DESC
                LIMIT		10'''
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cnx.commit()
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
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
    cur.close()
    cnx.close()
    return result


def get_unverified_drivers():
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''SELECT	*
				FROM	drivers
				WHERE	final_verification_date IS NULL'''
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result


def set_license_verification_date(id, date):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	drivers
				SET		license_verification_date = %s
				WHERE	id = %s'''
    cur.execute(query, (date, id))
    cnx.commit()
    cur.close()
    cnx.close()


def set_judicial_letter_path(id, path):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	drivers
				SET		judicial_letter_path = %s
				WHERE	id = %s'''
    cur.execute(query, (path, id))
    cnx.commit()
    cur.close()
    cnx.close()

def set_judicial_letter_verification_date(id, date):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	drivers
				SET		judicial_letter_verification_date = %s
				WHERE	id = %s'''
    cur.execute(query, (date, id))
    cnx.commit()
    cur.close()
    cnx.close()


def set_final_verification_date(id, date):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	drivers
				SET		final_verification_date = %s
				WHERE	id = %s'''
    cur.execute(query, (date, id))
    cnx.commit()
    cur.close()
    cnx.close()


def set_verifier_personnel_code(id, code):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	drivers
				SET		verifier_personnel_code = %s
				WHERE	id = %s'''
    cur.execute(query, (code, id))
    cnx.commit()
    cur.close()
    cnx.close()


def set_employee_pppath(pcode, path):
    cnx = create_connection('baxi_staff')
    cur = cnx.cursor()
    query = '''UPDATE	employees
				SET		profile_picture_path = %s
				WHERE	personnel_code = %s'''
    cur.execute(query, (path, pcode))
    cnx.commit()
    cur.close()
    cnx.close()


def set_driver_pppath(id, path):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	drivers
				SET		profile_picture_path = %s
				WHERE	id = %s'''
    cur.execute(query, (path, id))
    cnx.commit()
    cur.close()
    cnx.close()


def set_email(id, path):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = '''UPDATE	clients
				SET		email = %s
				WHERE	id = %s'''
    cur.execute(query, (path, id))
    cnx.commit()
    cur.close()
    cnx.close()


def is_female(id):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = """SELECT	id
				FROM	drivers
				WHERE	id = %s AND sex = 'F'"""
    cur.execute(query, (id,))
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result


def is_driver_account_inactive(id):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = """SELECT	id
				FROM	drivers LEFT JOIN reports ON id = driver_id
				WHERE	id = %s AND (final_verification_date IS NULL OR state = 'driver''s account deactivated)'"""
    cur.execute(query, (id,))
    result = cur.fetchall()
    cur.close()
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
    cur.close()
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
    cur.close()
    cnx.close()
    return result


def requests_within_range(lat, lon):
    cnx = create_connection('baxi_users')
    cur = cnx.cursor()
    query = """SELECT	first_name, last_name, pickup_location, pickup_province, pickup_city, city, latitude, longitude
				FROM	(service_requests JOIN clients ON client_id = id) JOIN destinations USING (client_id, request_time)
				WHERE	ST_Distance_Sphere(POINT(%s, %s), pickup_location) <= 5000"""
    cur.execute(query, (lat, lon))
    result = cur.fetchall()
    cur.close()
    cnx.close()
    return result
