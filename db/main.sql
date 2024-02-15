CREATE DATABASE baxi;

USE baxi;

CREATE TABLE	logs
				(
					user_id		INT				NOT NULL,
					log_time	DATETIME		NOT NULL	DEFAULT CURRENT_TIMESTAMP,
					operation	ENUM
								(
									'sign-up',
									'sign-in'
									--todo
								),
					PRIMARY KEY(user_id, log_time)
				);

CREATE TABLE	employees
				(
					personnel_code	INT				NOT NULL	PRIMARY KEY,
					first_name		VARCHAR(50),
					last_name		VARCHAR(50),
					shaba_number	CHAR(26),
					birth_date		DATETIME,
					proficiency		ENUM
									(
										'basic',
										'intermediate',
										'advanced',
										'proficient',
										'expert'
									),
					salary			INT,
					education		VARCHAR(50),
					position		ENUM
									(
										'department manager',
										'basic employee',
										'programmer'
									),
					department		VARCHAR(50),
					profile_picture	VARCHAR(50),
					password		VARCHAR(50)
				);

CREATE TABLE	clients
				(
					user_id			INT				NOT NULL	PRIMARY KEY,
					first_name		VARCHAR(50),
					last_name		VARCHAR(50),
					sex				ENUM
									(
										'M',
										'F'
									),
					wallet_balance	INT,
					phone_number	CHAR(11),
					e-mail			VARCHAR(50)
				);

CREATE TABLE	transactions
				(
					tracking_code		INT				NOT NULL	PRIMARY KEY,
					amount				INT,			NOT NULL,
					source_card			CHAR(16),
					destination_card	CHAR(16),
					time				DATETIME,
					state				ENUM
										(
											'failed',
											'declined',
											'pending',
											'cancelled',
											'completed',
											'returned'
										),
					type				ENUM
										(
											'wallet-to-wallet',
											''
										)
				);

CREATE TABLE	baxi_drivers
				(
					driver_code									INT				NOT NULL	PRIMARY KEY,
					vehicle_license_plate						CHAR(8),
					vehicle_capacity							INT,
					vehicle_color								VARCHAR(50),
					vehicle_model								VARCHAR(50),
					vehicle_production_date						DATE,
					vehicle_fuel_type							ENUM
																(
																	'gasoline',
																	'CNG',
																	'dual',
																	'electricity'
																),
					vehicle_card_photo							VARCHAR(50),
					driver_first_name							VARCHAR(50),
					driver_last_name							VARCHAR(50),
					driver_birth_date							DATE,
					driver_national_code						CHAR(10),
					driver_sex									ENUM
																(
																	'M',
																	'F'
																),
					driver_wallet_balance						INT,
					dirver_shaba_number							CHAR(26),
					driver_phone_number							CHAR(11),
					driver_referral_code						CHAR(10),
					driver_disability							--todo,
					driver_profile_picture						VARCHAR(50),
					driver_license_photo						VARCHAR(50),
					driver_national_card_photo					VARCHAR(50),
					verifier_personnel code						INT,
					driver_license_verification_date			DATE,
					driver_judicial_letter						VARCHAR(50),
					driver_judicial_letter_verification_date	DATE,
					final_verification_date						DATE
				);
