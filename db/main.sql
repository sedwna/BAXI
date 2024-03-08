CREATE DATABASE baxi_staff;
USE baxi_staff;

CREATE TABLE	employees
				(
					personnel_code			INT							PRIMARY KEY					AUTO_INCREMENT,
					shaba_number			CHAR(26)					UNIQUE						NOT NULL,
					signup_time				DATETIME					DEFAULT CURRENT_TIMESTAMP	NOT NULL,
					password				VARCHAR(50)												NOT NULL,
					first_name				VARCHAR(50)												NOT NULL,
					last_name				VARCHAR(50)												NOT NULL,
					birth_date				DATE													NOT NULL,
					salary					INT														NOT NULL,
					department				ENUM
											(
												'marketing',
												'accounting',
												'finance',
												'HR',
												'support',
												'development'
											)														NOT NULL,
					proficiency				ENUM
											(
												'basic',
												'intermediate',
												'advanced',
												'proficient',
												'expert'
											)														NOT NULL,
					education				ENUM
											(
												'none',
												'high school diploma',
												'associate degree',
												'bachelor''s degree',
												'master''s degree',
												'phd'
											)														NOT NULL,
					position				ENUM
											(
												'department manager',
												'basic employee',
												'programmer'
											)														NOT NULL,
					profile_picture_path	VARCHAR(50)
				);

CREATE VIEW managers AS	(
							SELECT	*
							FROM	employees
							WHERE	position = 'department manager'
						);

CREATE DATABASE baxi_users;
USE baxi_users;

CREATE TABLE	clients
				(
					id				INT				PRIMARY KEY					AUTO_INCREMENT,
					phone_number	CHAR(10)		UNIQUE						NOT NULL,
					wallet_balance	INT				DEFAULT 0					NOT NULL			CHECK (wallet_balance >= 0),
					signup_time		DATETIME		DEFAULT CURRENT_TIMESTAMP	NOT NULL,
					first_name		VARCHAR(50)									NOT NULL,
					last_name		VARCHAR(50)									NOT NULL,
					birth_date		DATE										NOT NULL,
					sex				ENUM
									(
										'M',
										'F'
									)				DEFAULT 'M'					NOT NULL,
					email			VARCHAR(50)
				);

CREATE TABLE	transactions
				(
					tracking_code		VARCHAR(20)				PRIMARY KEY,
					time				DATETIME				DEFAULT CURRENT_TIMESTAMP	NOT NULL,
					shaba_number		CHAR(26)											NOT NULL,
					amount				INT													NOT NULL,
					state				ENUM
										(
											'failed',
											'declined',
											'pending',
											'cancelled',
											'completed',
											'returned'
										)						DEFAULT 'pending'			NOT NULL,
					type				ENUM
										(
											'card-to-wallet',
											'wallet-to-card'
										)													NOT NULL
				);

CREATE TABLE	drivers
				(
					id									INT										PRIMARY KEY					AUTO_INCREMENT,
					phone_number						CHAR(10)								UNIQUE						NOT NULL,
					shaba_number						CHAR(26)								UNIQUE						NOT NULL,
					referral_code						CHAR(10)								UNIQUE						NOT NULL,
					wallet_balance						INT										DEFAULT 0					NOT NULL			CHECK (wallet_balance > -50),
					signup_time							DATETIME								DEFAULT CURRENT_TIMESTAMP	NOT NULL,
					disability							ENUM
														(
															'none',
															'alzheimer''s disease',
															'epilepsy',
															'hearing loss',
															'paralysis',
															'reduced limb or finger function',
															'weakened muscles',
															'parkinson''s disease',
															'developmental disabilities',
															'physical disabilities'
														)										DEFAULT 'none'				NOT NULL,
					first_name							VARCHAR(50)															NOT NULL,
					last_name							VARCHAR(50)															NOT NULL,
					birth_date							DATE																NOT NULL,
					national_code						CHAR(10)															NOT NULL,
					license_photo_path					VARCHAR(50)															NOT NULL,
					national_card_photo_path			VARCHAR(50)															NOT NULL,
					sex									ENUM
														(
															'M',
															'F'
														)										DEFAULT 'M'					NOT NULL,
					license_verification_date			DATE,
					judicial_letter_path				VARCHAR(50),
					judicial_letter_verification_date	DATE,
					final_verification_date				DATE,
					location							POINT,
					profile_picture_path				VARCHAR(50),
					verifier_personnel_code				INT,
					FOREIGN KEY(verifier_personnel_code)	REFERENCES baxi_staff.employees(personnel_code)	ON UPDATE CASCADE	ON DELETE RESTRICT
				);

CREATE TABLE	baxi
				(
					vehicle_license_plate		CHAR(9)			UNIQUE			NOT NULL	CHECK (vehicle_license_plate REGEXP '^[0-9]{2}[A-Z][0-9]{3}-[0-9]{2}$'),
					vehicle_capacity			INT								NOT NULL,
					vehicle_color				VARCHAR(50)						NOT NULL,
					vehicle_name				VARCHAR(50)						NOT NULL,
					vehicle_production_date		DATE							NOT NULL,
					vehicle_card_photo			VARCHAR(50)						NOT NULL,
					vehicle_fuel_type			ENUM
												(
													'gasoline',
													'CNG',
													'dual',
													'electricity'
												)								NOT NULL,
					driver_id					INT				PRIMARY KEY,
					FOREIGN KEY(driver_id)	REFERENCES drivers(id)	ON UPDATE CASCADE	ON DELETE CASCADE
				);

CREATE TABLE	baxi_baar
				(
					vehicle_license_plate		CHAR(9)			UNIQUE			NOT NULL	CHECK (vehicle_license_plate REGEXP '^[0-9]{2}[A-Z][0-9]{3}-[0-9]{2}$'),
					vehicle_capacity			INT								NOT NULL,
					vehicle_color				VARCHAR(50)						NOT NULL,
					vehicle_name				VARCHAR(50)						NOT NULL,
					vehicle_production_date		DATE							NOT NULL,
					vehicle_card_photo			VARCHAR(50)						NOT NULL,
					vehicle_fuel_type			ENUM
												(
													'gasoline',
													'CNG',
													'dual',
													'electricity'
												)								NOT NULL,
					driver_id					INT				PRIMARY KEY,	
					FOREIGN KEY(driver_id)	REFERENCES drivers(id)	ON UPDATE CASCADE	ON DELETE CASCADE
				);

CREATE TABLE	baxi_box
				(
					vehicle_license_plate		CHAR(9)				UNIQUE				NOT NULL	CHECK (vehicle_license_plate REGEXP '^[0-9]{2}[A-Z][0-9]{3}-[0-9]{2}$'),
					vehicle_capacity			INT										NOT NULL,
					vehicle_color				VARCHAR(50)								NOT NULL,
					vehicle_name				VARCHAR(50)								NOT NULL,
					vehicle_production_date		DATE									NOT NULL,
					vehicle_card_photo			VARCHAR(50)								NOT NULL,
					driver_id					INT					PRIMARY KEY,	
					FOREIGN KEY(driver_id)	REFERENCES drivers(id)	ON UPDATE CASCADE	ON DELETE CASCADE
				);

CREATE TABLE	service_requests
				(
					
					pickup_location		POINT			NOT NULL,
					pickup_province		VARCHAR(50)		NOT NULL,	
					pickup_city			VARCHAR(50)		NOT NULL,
					client_id			INT,
					request_time		DATETIME,
					PRIMARY KEY(client_id, request_time),
					FOREIGN KEY(client_id)	REFERENCES clients(id)	ON UPDATE CASCADE	ON DELETE RESTRICT
				);

CREATE TABLE	baxi_trips
				(
					cost			INT							NOT NULL,
					round_trip		ENUM
									(
										'no',
										'yes'
									)			DEFAULT 'no'	NOT NULL,
					client_id		INT,
					request_time	DATETIME,
					PRIMARY KEY(client_id, request_time),
					FOREIGN KEY(client_id, request_time)	REFERENCES service_requests(client_id, request_time)	ON UPDATE CASCADE	ON DELETE CASCADE
				);

CREATE TABLE	heavy_transports
				(
					cost				INT											NOT NULL,
					cargo_weight		INT											NOT NULL,
					cargo_value			INT											NOT NULL,
					dropoff_location	POINT										NOT NULL,
					dropoff_city		VARCHAR(50)									NOT NULL,
					cargo_type			ENUM
										(
											'unfragile',
											'fragile'
										)					DEFAULT 'unfragile'		NOT NULL,
					client_helped		ENUM
										(
											'no',
											'yes'
										)					DEFAULT 'no'			NOT NULL,
					client_id			INT,
					request_time		DATETIME,
					PRIMARY KEY(client_id, request_time),
					FOREIGN KEY(client_id, request_time)	REFERENCES service_requests(client_id, request_time)	ON UPDATE CASCADE	ON DELETE CASCADE
				);

CREATE TABLE	light_transports
				(
					cost				INT											NOT NULL,
					cargo_weight		INT											NOT NULL,
					cargo_value			INT											NOT NULL,
					dropoff_location	POINT										NOT NULL,
					dropoff_city		VARCHAR(50)									NOT NULL,
					insurance_cost		INT											NOT NULL,
					cargo_type			ENUM
										(
											'unfragile',
											'fragile'
										)					DEFAULT 'unfragile'		NOT NULL,
					client_id			INT,
					request_time		DATETIME,
					PRIMARY KEY(client_id, request_time),
					FOREIGN KEY(client_id, request_time)	REFERENCES service_requests(client_id, request_time)	ON UPDATE CASCADE	ON DELETE CASCADE
				);

CREATE TABLE	referrals
				(
					referrer_id		INT		PRIMARY KEY,
					referred_id		INT		NOT NULL,
					FOREIGN KEY(referrer_id)	REFERENCES drivers(id)	ON UPDATE CASCADE	ON DELETE RESTRICT,
					FOREIGN KEY(referred_id)	REFERENCES drivers(id)	ON UPDATE CASCADE	ON DELETE RESTRICT
				);

CREATE TABLE	withdrawals
				(
					type			ENUM
									(
										'daily',
										'momentary'
									)				DEFAULT 'momentary'		NOT NULL,
					tracking_code	VARCHAR(20)		PRIMARY KEY,
					driver_id		INT										NOT NULL,
					FOREIGN KEY(tracking_code)	REFERENCES transactions(tracking_code)	ON UPDATE CASCADE	ON DELETE CASCADE,
					FOREIGN KEY(driver_id)		REFERENCES drivers(id)	ON UPDATE CASCADE	ON DELETE RESTRICT
				);

CREATE TABLE	deposits
				(
					tracking_code	VARCHAR(20)		PRIMARY KEY,
					client_id		INT				NOT NULL,
					FOREIGN KEY(tracking_code)	REFERENCES transactions(tracking_code)	ON UPDATE CASCADE	ON DELETE CASCADE,
					FOREIGN KEY(client_id)		REFERENCES clients(id)	ON UPDATE CASCADE	ON DELETE RESTRICT
				);

CREATE TABLE	service_acceptances
				(
					estimated_end_time	DATETIME											NOT NULL,
					end_time			DATETIME				DEFAULT CURRENT_TIMESTAMP	NOT NULL,
					driver_id			INT													NOT NULL,
					method_of_payment	ENUM
										(
											'direct',
											'cash',
											'wallet-to-wallet'
										)													NOT NULL,
					wait_time			ENUM
										(
											'0-to-5 minutes',
											'5-to-10 minutes',
											'10-to-30 minutes',
											'30-to-60 minutes'
										)						DEFAULT '0-to-5 minutes'	NOT NULL,
					driver_rating		ENUM
										(
											'0-star',
											'1-star',
											'2-star',
											'3-star',
											'4-star',
											'5-star'
										)						DEFAULT NULL,
					client_rating		ENUM
										(
											'0-star',
											'1-star',
											'2-star',
											'3-star',
											'4-star',
											'5-star'
										)						DEFAULT NULL,
					tracking_code		VARCHAR(20),
					client_id			INT,
					request_time		DATETIME,
					PRIMARY KEY(client_id, request_time),
					FOREIGN KEY(client_id, request_time)	REFERENCES service_requests(client_id, request_time)	ON UPDATE CASCADE	ON DELETE CASCADE,
					FOREIGN KEY(tracking_code)	REFERENCES transactions(tracking_code)	ON UPDATE CASCADE	ON DELETE RESTRICT,
					FOREIGN KEY(driver_id)		REFERENCES drivers(id)	ON UPDATE CASCADE	ON DELETE RESTRICT
				);

CREATE TABLE	reports
				(
					description		VARCHAR(100)												NOT NULL,
					state			ENUM
									(
										'pending',
										'under investigation',
										'dismissed',
										'driver''s account deactivated',
										'client''s account deactivated'
									)										DEFAULT 'pending'	NOT NULL,
					client_id		INT,
					driver_id		INT,
					PRIMARY KEY(client_id, driver_id),
					FOREIGN KEY(client_id)	REFERENCES clients(id)	ON UPDATE CASCADE	ON DELETE RESTRICT,
					FOREIGN KEY(driver_id)	REFERENCES drivers(id)	ON UPDATE CASCADE	ON DELETE RESTRICT
				);

CREATE TABLE	addresses
				(
					location		POINT			NOT NULL,
					client_id		INT,
					address_name	VARCHAR(50),
					PRIMARY KEY(client_id, address_name),
					FOREIGN KEY(client_id)	REFERENCES clients(id)	ON UPDATE CASCADE	ON DELETE CASCADE
				);

CREATE TABLE	destinations
				(
					city			VARCHAR(50)		NOT NULL,
					client_id		INT				NOT NULL,
					request_time	DATETIME		NOT NULL,
					latitude		FLOAT			NOT NULL,
					longitude		FLOAT			NOT NULL,
					PRIMARY KEY(client_id, request_time, latitude, longitude),
					FOREIGN KEY(client_id, request_time)	REFERENCES service_requests(client_id, request_time)	ON UPDATE CASCADE	ON DELETE CASCADE
				);

CREATE TABLE	compliments
				(
					client_id		INT,
					request_time	DATETIME,
					point			ENUM
									(
										-- baxi
										'safe driving',
										'enjoyable music',
										-- box and baar
										'safe shipment',
										-- all
										'neat vehicle',
										'respectful behavior',
										'punctuality',
										'proper routing',
										'moderate temperature'
									)							NOT NULL,
					PRIMARY KEY(client_id, request_time, point),
					FOREIGN KEY(client_id, request_time)	REFERENCES service_requests(client_id, request_time)	ON UPDATE CASCADE	ON DELETE CASCADE
				);

CREATE TABLE	complaints
				(
					client_id		INT,
					request_time	DATETIME,
					point			ENUM
									(
										-- baxi
										'dangerous driving',
										'immoderate temperature',
										-- box and baar
										'unsafe shipment',
										-- all
										'improper routing',
										'demand for extra money',
										'demand for cash payment',
										'discrepancy in description',
										'disrespectful behavior',
										'poor vehicle condition',
										'unpunctuality'
									)									NOT NULL,
					PRIMARY KEY(client_id, request_time, point),
					FOREIGN KEY(client_id, request_time)	REFERENCES service_requests(client_id, request_time)	ON UPDATE CASCADE	ON DELETE CASCADE
				);

CREATE TABLE	company_deposits
				(
					amount						INT			NOT NULL,
					time						DATETIME	NOT NULL,
					type	ENUM
							(
								'reward',
								'fuel quota'
							)								NOT NULL,
					employee_personnel_code		INT,
					driver_id					INT,
					PRIMARY KEY(employee_personnel_code, driver_id),
					FOREIGN KEY(employee_personnel_code)	REFERENCES baxi_staff.employees(personnel_code)	ON UPDATE CASCADE	ON DELETE RESTRICT,
					FOREIGN KEY(driver_id)					REFERENCES drivers(id)	ON UPDATE CASCADE	ON DELETE RESTRICT
				);

CREATE TABLE	compensatory_deposits
				(
					tracking_code	VARCHAR(20)		PRIMARY KEY,
					driver_id		INT				NOT NULL,
					FOREIGN KEY(tracking_code)	REFERENCES transactions(tracking_code)	ON UPDATE CASCADE	ON DELETE CASCADE,
					FOREIGN KEY(driver_id)		REFERENCES drivers(id)	ON UPDATE CASCADE	ON DELETE RESTRICT
				);

CREATE TABLE	monthly_incomes
				(
					income		INT		NOT NULL,
					driver_id	INT,
					date		DATE,
					PRIMARY KEY(driver_id, date),
					FOREIGN KEY(driver_id)	REFERENCES drivers(id)
				);

DELIMITER //

CREATE TRIGGER	update_wallets	AFTER INSERT ON service_acceptances	FOR EACH ROW
BEGIN
	DECLARE cost	INT;
	DECLARE state	ENUM ('failed', 'declined', 'pending', 'cancelled', 'completed', 'returned');
	SELECT state INTO state	FROM service_acceptances JOIN transactions USING (tracking_code);
	IF ((NEW.method_of_payment = 'direct' AND state = 'completed') OR NEW.method_of_payment = 'wallet_to_wallet') THEN
		SELECT cost INTO cost	FROM baxi_trips b	WHERE NEW.client_id = b.client_id AND NEW.request_time = b.request_time;
		UPDATE clients	SET wallet_balance = wallet_balance - cost	WHERE id = NEW.client_id;
		UPDATE drivers	SET wallet_balance = wallet_balance + cost * 0.8	WHERE id = NEW.driver_id;
	ELSEIF (NEW.method_of_payment = 'cash')	THEN
		UPDATE drivers	SET wallet_balance = wallet_balance - cost * 0.2	WHERE id = NEW.driver_id;
	END IF;
END//

CREATE TRIGGER	commit_withdrawal	AFTER INSERT ON withdrawals	FOR EACH ROW
BEGIN
	DECLARE amount	INT;
	DECLARE state	ENUM ('failed', 'declined', 'pending', 'cancelled', 'completed', 'returned');
	SELECT state, amount INTO state, amount	FROM transactions	WHERE tracking_code = NEW.tracking_code;
	IF (state = 'completed') THEN
		UPDATE clients	SET wallet_balance = wallet_balance - amount	WHERE id = NEW.driver_id;
	END IF;
END//

CREATE TRIGGER	commit_deposit	AFTER INSERT ON deposits	FOR EACH ROW
BEGIN
	DECLARE amount	INT;
	DECLARE state	ENUM ('failed', 'declined', 'pending', 'cancelled', 'completed', 'returned');
	SELECT state, amount INTO state, amount	FROM transactions	WHERE tracking_code = NEW.tracking_code;
	IF (state = 'completed') THEN
		UPDATE clients	SET wallet_balance = wallet_balance + amount	WHERE id = NEW.client_id;
	END IF;
END//

CREATE TRIGGER	commit_company_deposit	AFTER INSERT ON company_deposits	FOR EACH ROW
BEGIN
	UPDATE drivers	SET wallet_balance = wallet_balance + NEW.amount	WHERE id = NEW.driver_id;
END//

CREATE TRIGGER	commit_referral_bonus	AFTER INSERT ON referrals	FOR EACH ROW
BEGIN
	UPDATE drivers	SET wallet_balance = wallet_balance + 50000	WHERE id = NEW.referred_id;
END//

CREATE TRIGGER	commit_compensatory_deposit	AFTER INSERT ON compensatory_deposits	FOR EACH ROW
BEGIN
	DECLARE amount	INT;
	SELECT amount INTO amount	FROM transactions	WHERE tracking_code = NEW.tracking_code;
	UPDATE drivers	SET wallet_balance = wallet_balance + amount	WHERE id = NEW.driver_id;
END//

DELIMITER ;

SET GLOBAL event_scheduler = ON;
CREATE EVENT monthly_income_event
ON SCHEDULE
	EVERY 1 MONTH STARTS
	CURRENT_DATE + INTERVAL 1 MONTH
	ON COMPLETION PRESERVE
DO
	INSERT	INTO monthly_incomes
	SELECT	income, driver_id, LAST_DAY(DATE_SUB(CURDATE(), INTERVAL 1 MONTH))
	FROM	(
				SELECT		driver_id, SUM(cost) AS income
				FROM		(
								(SELECT	driver_id, cost
								FROM	service_acceptance JOIN baxi_trips USING (client_id, request_time)
								WHERE	YEAR(end_time) = YEAR(CURRENT_DATE - INTERVAL 1 MONTH)
										AND MONTH(end_time) = MONTH(CURRENT_DATE - INTERVAL 1 MONTH))
								UNION
								(SELECT	driver_id, cost
								FROM	service_acceptance JOIN heavy_transports USING (client_id, request_time)
								WHERE	YEAR(end_time) = YEAR(CURRENT_DATE - INTERVAL 1 MONTH)
										AND MONTH(end_time) = MONTH(CURRENT_DATE - INTERVAL 1 MONTH))
								UNION
								(SELECT	driver_id, cost
								FROM	service_acceptance JOIN light_transports USING (client_id, request_time)
								WHERE	YEAR(end_time) = YEAR(CURRENT_DATE - INTERVAL 1 MONTH)
										AND MONTH(end_time) = MONTH(CURRENT_DATE - INTERVAL 1 MONTH))
							) AS sub0
				GROUP BY	driver_id
			) AS sub1;

CREATE VIEW	female_drivers AS	(
									SELECT	*
									FROM	drivers JOIN baxi ON id = driver_id
									WHERE	sex = 'F'
								);

CREATE VIEW	male_drivers AS	(
								SELECT	*
								FROM	drivers JOIN baxi ON id = driver_id
								WHERE	sex = 'M'
							);

CREATE VIEW	baar_drivers AS	(
								SELECT	*
								FROM	driver JOIN baxi_baar ON id = driver_id
							);

CREATE VIEW	box_drivers AS	(
								SELECT	*
								FROM	driver JOIN baxi_box ON id = driver_id
							);
