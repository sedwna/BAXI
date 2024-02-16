CREATE DATABASE baxi_staff;
CREATE DATABASE baxi_users;

-- use POINT for coordinates

USE baxi_staff;

CREATE TABLE	employees
				(
					personnel_code			INT							PRIMARY KEY		AUTO_INCREMENT,
					password				VARCHAR(50)									NOT NULL,
					first_name				VARCHAR(50)									NOT NULL,
					last_name				VARCHAR(50)									NOT NULL,
					shaba_number			CHAR(26)					UNIQUE			NOT NULL,
					birth_date				DATE										NOT NULL,
					proficiency				ENUM										NOT NULL,
											(
												'basic',
												'intermediate',
												'advanced',
												'proficient',
												'expert'
											)
					salary					INT											NOT NULL,
					education				ENUM										NOT NULL,
											(
												'none',
												'high school diploma',
												'associate degree',
												'bachelor''s degree',
												'master''s degree',
												'phd'
											)
					position				ENUM										NOT NULL,
											(
												'department manager',
												'basic employee',
												'programmer'
											)
					department				VARCHAR(50)									NOT NULL,
					profile_picture_path	VARCHAR(50)
				);

USE baxi_users;

CREATE TABLE	clients
				(
					client_id		INT				PRIMARY KEY		AUTO_INCREMENT,
					phone_number	CHAR(11)		UNIQUE			NOT NULL,
					first_name		VARCHAR(50)						NOT NULL,
					last_name		VARCHAR(50)						NOT NULL,
					sex				ENUM							NOT NULL,
									(
										'M',
										'F'
									)
					wallet_balance	INT				DEFAULT 0		NOT NULL,
					email			VARCHAR(50)
				);

CREATE TABLE	transactions
				(
					tracking_code		INT						PRIMARY KEY,
					amount				INT													NOT NULL,
					source_card			CHAR(16),
					destination_card	CHAR(16),
					time				DATETIME				DEFAULT CURRENT_TIMESTAMP	NOT NULL,
					state				ENUM												NOT NULL,
										(
											'failed',
											'declined',
											'pending',
											'cancelled',
											'completed',
											'returned'
										)
					type				ENUM												NOT NULL
										(
											-- verification needed
											'wallet-to-wallet',
											'card-to-wallet',
											'wallet-to-card',
											'cash'
										)
				);

CREATE TABLE	baxi_drivers
				(
					driver_id									INT										PRIMARY KEY		AUTO_INCREMENT,
					driver_phone_number							CHAR(11)								UNIQUE			NOT NULL,
					driver_first_name							VARCHAR(50)												NOT NULL,
					driver_last_name							VARCHAR(50)												NOT NULL,
					driver_birth_date							DATE													NOT NULL,
					driver_national_code						CHAR(10)												NOT NULL,
					driver_sex									ENUM													NOT NULL,
																(
																	'M',
																	'F'
																)
					driver_wallet_balance						INT										DEFAULT 0		NOT NULL,
					dirver_shaba_number							CHAR(26)								UNIQUE			NOT NULL,
					driver_referral_code						CHAR(10)								UNIQUE			NOT NULL,
					driver_disability							ENUM
																(
																	'alzheimer''s disease',
																	'epilepsy',
																	'hearing loss',
																	'paralysis',
																	'reduced limb or finger function',
																	'weakened muscles',
																	'parkinson''s disease',
																	'developmental disabilities',
																	'physical disabilities'
																),
					driver_profile_picture_path					VARCHAR(50),
					driver_license_photo_path					VARCHAR(50)												NOT NULL,
					driver_national_card_photo_path				VARCHAR(50)												NOT NULL,
					driver_license_verification_date			DATE													NOT NULL,
					driver_judicial_letter_path					VARCHAR(50)												NOT NULL,
					driver_judicial_letter_verification_date	DATE													NOT NULL,
					driver_final_verification_date				DATE													NOT NULL,
					vehicle_license_plate						CHAR(8)													NOT NULL,
					vehicle_capacity							INT														NOT NULL,
					vehicle_color								VARCHAR(50)												NOT NULL,
					vehicle_model								VARCHAR(50)												NOT NULL,
					vehicle_production_date						DATE													NOT NULL,
					vehicle_fuel_type							ENUM													NOT NULL,
																(
																	'gasoline',
																	'CNG',
																	'dual',
																	'electricity'
																)
					vehicle_card_photo							VARCHAR(50)												NOT NULL,
					verifier_personnel_code						INT														NOT NULL,
				);
