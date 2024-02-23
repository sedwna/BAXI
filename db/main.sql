CREATE DATABASE baxi_staff;
USE baxi_staff;

CREATE TABLE	employees
				(
					personnel_code			INT							PRIMARY KEY		AUTO_INCREMENT,
					shaba_number			CHAR(26)					UNIQUE			NOT NULL,
					password				VARCHAR(50)									NOT NULL,
					first_name				VARCHAR(50)									NOT NULL,
					last_name				VARCHAR(50)									NOT NULL,
					birth_date				DATE										NOT NULL,
					salary					INT											NOT NULL,
					department				VARCHAR(50)									NOT NULL,
					signup_time				DATETIME									NOT NULL,
					proficiency				ENUM
											(
												'basic',
												'intermediate',
												'advanced',
												'proficient',
												'expert'
											)											NOT NULL,
					education				ENUM
											(
												'none',
												'high school diploma',
												'associate degree',
												'bachelor''s degree',
												'master''s degree',
												'phd'
											)											NOT NULL,
					position				ENUM
											(
												'department manager',
												'basic employee',
												'programmer'
											)											NOT NULL,
					profile_picture_path	VARCHAR(50)
				);

CREATE DATABASE baxi_users;
USE baxi_users;

CREATE TABLE	clients
				(
					client_id		INT				PRIMARY KEY		AUTO_INCREMENT,
					phone_number	CHAR(11)		UNIQUE			NOT NULL,
					wallet_balance	INT				DEFAULT 0		NOT NULL,
					first_name		VARCHAR(50)						NOT NULL,
					last_name		VARCHAR(50)						NOT NULL,
					signup_time		DATETIME						NOT NULL,
					sex				ENUM
									(
										'M',
										'F'
									)								NOT NULL,
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
					id									INT										PRIMARY KEY		AUTO_INCREMENT,
					phone_number						CHAR(11)								UNIQUE			NOT NULL,
					shaba_number						CHAR(26)								UNIQUE			NOT NULL,
					referral_code						CHAR(10)								UNIQUE			NOT NULL,
					wallet_balance						INT										DEFAULT 0		NOT NULL,
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
														)										DEFAULT 'none'	NOT NULL,
					first_name							VARCHAR(50)												NOT NULL,
					last_name							VARCHAR(50)												NOT NULL,
					birth_date							DATE													NOT NULL,
					national_code						CHAR(10)												NOT NULL,
					license_photo_path					VARCHAR(50)												NOT NULL,
					national_card_photo_path			VARCHAR(50)												NOT NULL,
					license_verification_date			DATE													NOT NULL,
					judicial_letter_path				VARCHAR(50)												NOT NULL,
					judicial_letter_verification_date	DATE													NOT NULL,
					final_verification_date				DATE													NOT NULL,
					signup_time							DATETIME												NOT NULL,
					sex									ENUM
														(
															'M',
															'F'
														)														NOT NULL,
					profile_picture_path				VARCHAR(50),
					verifier_personnel_code				INT														NOT NULL,
					FOREIGN KEY(verifier_personnel_code)	REFERENCES employees(personnel_code)
				);

CREATE TABLE	baxi
				(
					vehicle_license_plate		CHAR(8)			UNIQUE			NOT NULL,
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
					FOREIGN KEY(driver_id)	REFERENCES drivers(driver_id)
				);

CREATE TABLE	baxi_baar
				(
					vehicle_license_plate		CHAR(8)			UNIQUE			NOT NULL,
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
					FOREIGN KEY(driver_id)	REFERENCES drivers(driver_id)
				);

CREATE TABLE	baxi_box
				(
					vehicle_license_plate		CHAR(8)				UNIQUE				NOT NULL,
					vehicle_capacity			INT										NOT NULL,
					vehicle_color				VARCHAR(50)								NOT NULL,
					vehicle_name				VARCHAR(50)								NOT NULL,
					vehicle_production_date		DATE									NOT NULL,
					vehicle_card_photo			VARCHAR(50)								NOT NULL,
					vehicle_fuel_type			ENUM
												(
													'gasoline',
													'CNG',
													'dual',
													'electricity'
												)					DEFAULT 'gasoline'	NOT NULL,
					driver_id					INT					PRIMARY KEY,	
					FOREIGN KEY(driver_id)	REFERENCES drivers(driver_id)
				);

CREATE TABLE	service_requests
				(
					pickup_location		POINT,
					client_id			INT,
					request_time		DATETIME,
					PRIMARY KEY(client_id, request_time),
					FOREIGN KEY(client_id)	REFERENCES clients(client_id)
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
					FOREIGN KEY(client_id)		REFERENCES service_requests(client_id),
					FOREIGN KEY(request_time)	REFERENCES service_requests(request_time)
				);

CREATE TABLE	heavy_transports
				(
					cost			INT											NOT NULL,
					cargo_weight	INT											NOT NULL,
					cargo_value		INT											NOT NULL,
					cargo_type		ENUM
									(
										'unfragile',
										'fragile'
									)					DEFAULT 'unfragile'		NOT NULL,
					client_helped	ENUM
									(
										'no',
										'yes'
									)					DEFAULT 'no'			NOT NULL,
					client_id		INT,
					request_time	DATETIME,
					PRIMARY KEY(client_id, request_time),
					FOREIGN KEY(client_id)		REFERENCES service_requests(client_id),
					FOREIGN KEY(request_time)	REFERENCES service_requests(request_time)
				);

CREATE TABLE	light_transports
				(
					cost			INT											NOT NULL,
					cargo_weight	INT											NOT NULL,
					cargo_value		INT											NOT NULL,
					insurance_cost	INT											NOT NULL,
					cargo_type		ENUM
									(
										'unfragile',
										'fragile'
									)					DEFAULT 'unfragile'		NOT NULL,
					client_id		INT,
					request_time	DATETIME,
					PRIMARY KEY(client_id, request_time),
					FOREIGN KEY(client_id)		REFERENCES service_requests(client_id),
					FOREIGN KEY(request_time)	REFERENCES service_requests(request_time)
				);

CREATE TABLE	referrals
				(
					referrer_id		INT		PRIMARY KEY,
					referred_id		INT,
					FOREIGN KEY(referrer_id)	REFERENCES drivers(driver_id),
					FOREIGN KEY(referred_id)	REFERENCES drivers(driver_id)
				);

CREATE TABLE	withdrawals
				(
					type			ENUM
									(
										'daily',
										'momentary'
									)				DEFAULT 'daily'		NOT NULL,
					tracking_code	VARCHAR(20)		PRIMARY KEY,
					driver_id		INT									NOT NULL,
					FOREIGN KEY(tracking_code)	REFERENCES transactions(tracking_code),
					FOREIGN KEY(driver_id)		REFERENCES drivers(driver_id)
				);

CREATE TABLE	deposits
				(
					tracking_code	VARCHAR(20)		PRIMARY KEY,
					client_id		INT				NOT NULL,
					FOREIGN KEY(tracking_code)	REFERENCES transactions(tracking_code),
					FOREIGN KEY(client_id)		REFERENCES clients(client_id)
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
					wait_time			ENUM
										(
											'0-to-5 minutes',
											'5-to-10 minutes',
											'10-to-30 minutes',
											'30-to-60 minutes'
										)						DEFAULT '0-to-5 minutes'	NOT NULL,
					client_id			INT,
					request_time		DATETIME,
					tracking_code		VARCHAR(20),
					PRIMARY KEY(client_id, request_time, tracking_code),
					FOREIGN KEY(client_id)		REFERENCES service_requests(client_id),
					FOREIGN KEY(request_time)	REFERENCES service_requests(request_time),
					FOREIGN KEY(tracking_code)	REFERENCES transactions(tracking_code),
					FOREIGN KEY(driver_id)		REFERENCES drivers(driver_id)
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
					FOREIGN KEY(client_id)	REFERENCES clients(client_id),
					FOREIGN KEY(driver_id)	REFERENCES drivers(driver_id)
				);

CREATE TABLE	addresses
				(
					location		POINT			NOT NULL,
					client_id		INT,
					address_name	VARCHAR(50),
					PRIMARY KEY(client_id, address_name),
					FOREIGN KEY(client_id)	REFERENCES clients(client_id)
				);

CREATE TABLE	destinations
				(
					client_id		INT,
					request_time	DATETIME,
					location		POINT,
					PRIMARY KEY(client_id, request_time, location),
					FOREIGN KEY(client_id)		REFERENCES service_requests(client_id),
					FOREIGN KEY(request_time)	REFERENCES service_requests(request_time)
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
									),
					PRIMARY KEY(client_id, request_time, point),
					FOREIGN KEY(client_id)		REFERENCES service_requests(client_id),
					FOREIGN KEY(request_time)	REFERENCES service_requests(request_time)
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
									),
					PRIMARY KEY(client_id, request_time, point),
					FOREIGN KEY(client_id)		REFERENCES service_requests(client_id),
					FOREIGN KEY(request_time)	REFERENCES service_requests(request_time)
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
					FOREIGN KEY(employee_personnel_code)	REFERENCES employees(personnel_code),
					FOREIGN KEY(driver_id)					REFERENCES drivers(driver_id)
				);

CREATE TABLE	compensatory_deposits
				(
					tracking_code	VARCHAR(20)		PRIMARY KEY,
					driver_id		INT				NOT NULL,
					FOREIGN KEY(tracking_code)	REFERENCES transactions(tracking_code),
					FOREIGN KEY(driver_id)		REFERENCES drivers(driver_id)
				);
