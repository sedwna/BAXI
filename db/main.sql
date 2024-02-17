CREATE DATABASE baxi_staff;
CREATE DATABASE baxi_users;

-- use POINT for coordinates

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
					signup_time				DATETIME									NOT NULL
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
					profile_picture_path	VARCHAR(50),
				);

USE baxi_users;

CREATE TABLE	clients
				(
					client_id		INT				PRIMARY KEY		AUTO_INCREMENT,
					phone_number	CHAR(11)		UNIQUE			NOT NULL,
					wallet_balance	INT				DEFAULT 0		NOT NULL,
					first_name		VARCHAR(50)						NOT NULL,
					last_name		VARCHAR(50)						NOT NULL,
					signup_time		DATETIME						NOT NULL
					sex				ENUM
									(
										'M',
										'F'
									)								NOT NULL,
					email			VARCHAR(50),
				);

CREATE TABLE	transactions
				(
					tracking_code		INT						PRIMARY KEY,
					time				DATETIME				DEFAULT CURRENT_TIMESTAMP	NOT NULL,
					amount				INT													NOT NULL,
					state				ENUM
										(
											'failed',
											'declined',
											'pending',
											'cancelled',
											'completed',
											'returned'
										)													NOT NULL,
					type				ENUM
										(
											-- verification needed
											'wallet-to-wallet',
											'card-to-wallet',
											'wallet-to-card',
											'cash'
										)													NOT NULL
					source_card			CHAR(16),
					destination_card	CHAR(16),
				);

CREATE TABLE	baxi_drivers
				(
					driver_id									INT										PRIMARY KEY		AUTO_INCREMENT,
					driver_phone_number							CHAR(11)								UNIQUE			NOT NULL,
					dirver_shaba_number							CHAR(26)								UNIQUE			NOT NULL,
					driver_referral_code						CHAR(10)								UNIQUE			NOT NULL,
					driver_wallet_balance						INT										DEFAULT 0		NOT NULL,
					driver_disability							ENUM
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
					driver_first_name							VARCHAR(50)												NOT NULL,
					driver_last_name							VARCHAR(50)												NOT NULL,
					driver_birth_date							DATE													NOT NULL,
					driver_national_code						CHAR(10)												NOT NULL,
					driver_license_photo_path					VARCHAR(50)												NOT NULL,
					driver_national_card_photo_path				VARCHAR(50)												NOT NULL,
					driver_license_verification_date			DATE													NOT NULL,
					driver_judicial_letter_path					VARCHAR(50)												NOT NULL,
					driver_judicial_letter_verification_date	DATE													NOT NULL,
					driver_final_verification_date				DATE													NOT NULL,
					driver_signup_time							DATETIME												NOT NULL,
					vehicle_license_plate						CHAR(8)													NOT NULL,
					vehicle_capacity							INT														NOT NULL,
					vehicle_color								VARCHAR(50)												NOT NULL,
					vehicle_name								VARCHAR(50)												NOT NULL,
					vehicle_production_date						DATE													NOT NULL,
					vehicle_card_photo							VARCHAR(50)												NOT NULL,
					vehicle_fuel_type							ENUM
																(
																	'gasoline',
																	'CNG',
																	'dual',
																	'electricity'
																)														NOT NULL,
					driver_sex									ENUM
																(
																	'M',
																	'F'
																)														NOT NULL,
					driver_profile_picture_path					VARCHAR(50),
					verifier_personnel_code						INT														NOT NULL,
					FOREIGN KEY(verifier_personnel_code) REFERENCES employees(personnel_code)
				);

CREATE TABLE	baxi_baar_drivers
				(
					driver_id									INT										PRIMARY KEY		AUTO_INCREMENT,
					driver_phone_number							CHAR(11)								UNIQUE			NOT NULL,
					dirver_shaba_number							CHAR(26)								UNIQUE			NOT NULL,
					driver_referral_code						CHAR(10)								UNIQUE			NOT NULL,
					driver_wallet_balance						INT										DEFAULT 0		NOT NULL,
					driver_disability							ENUM
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
					driver_first_name							VARCHAR(50)												NOT NULL,
					driver_last_name							VARCHAR(50)												NOT NULL,
					driver_birth_date							DATE													NOT NULL,
					driver_national_code						CHAR(10)												NOT NULL,
					driver_license_photo_path					VARCHAR(50)												NOT NULL,
					driver_national_card_photo_path				VARCHAR(50)												NOT NULL,
					driver_license_verification_date			DATE													NOT NULL,
					driver_judicial_letter_path					VARCHAR(50)												NOT NULL,
					driver_judicial_letter_verification_date	DATE													NOT NULL,
					driver_final_verification_date				DATE													NOT NULL,
					driver_signup_time							DATETIME												NOT NULL,
					vehicle_license_plate						CHAR(8)													NOT NULL,
					vehicle_capacity							INT														NOT NULL,
					vehicle_color								VARCHAR(50)												NOT NULL,
					vehicle_name								VARCHAR(50)												NOT NULL,
					vehicle_production_date						DATE													NOT NULL,
					vehicle_card_photo							VARCHAR(50)												NOT NULL,
					vehicle_fuel_type							ENUM
																(
																	'gasoline',
																	'CNG',
																	'dual',
																	'electricity'
																)														NOT NULL,
					driver_sex									ENUM
																(
																	'M',
																	'F'
																)														NOT NULL,
					driver_profile_picture_path					VARCHAR(50),
					verifier_personnel_code						INT														NOT NULL,
					FOREIGN KEY(verifier_personnel_code) REFERENCES employees(personnel_code)
				);

CREATE TABLE	baxi_box_drivers
				(
					driver_id									INT										PRIMARY KEY		AUTO_INCREMENT,
					driver_phone_number							CHAR(11)								UNIQUE			NOT NULL,
					dirver_shaba_number							CHAR(26)								UNIQUE			NOT NULL,
					driver_referral_code						CHAR(10)								UNIQUE			NOT NULL,
					driver_wallet_balance						INT										DEFAULT 0		NOT NULL,
					driver_disability							ENUM
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
					driver_first_name							VARCHAR(50)												NOT NULL,
					driver_last_name							VARCHAR(50)												NOT NULL,
					driver_birth_date							DATE													NOT NULL,
					driver_national_code						CHAR(10)												NOT NULL,
					driver_license_photo_path					VARCHAR(50)												NOT NULL,
					driver_national_card_photo_path				VARCHAR(50)												NOT NULL,
					driver_license_verification_date			DATE													NOT NULL,
					driver_judicial_letter_path					VARCHAR(50)												NOT NULL,
					driver_judicial_letter_verification_date	DATE													NOT NULL,
					driver_final_verification_date				DATE													NOT NULL,
					driver_signup_time							DATETIME												NOT NULL,
					vehicle_license_plate						CHAR(8)													NOT NULL,
					vehicle_capacity							INT														NOT NULL,
					vehicle_name								VARCHAR(50)												NOT NULL,
					vehicle_production_date						DATE													NOT NULL,
					vehicle_card_photo							VARCHAR(50)												NOT NULL,
					vehicle_fuel_type							ENUM
																(
																	'gasoline',
																	'CNG',
																	'dual',
																	'electricity'
																)														NOT NULL,
					driver_sex									ENUM
																(
																	'M',
																	'F'
																)														NOT NULL,
					driver_profile_picture_path					VARCHAR(50),
					verifier_personnel_code						INT														NOT NULL,
					FOREIGN KEY(verifier_personnel_code) REFERENCES employees(personnel_code)
				);
