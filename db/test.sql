CREATE DATABASE	test;
USE test;
CREATE TABLE	test.tab
				(
					id		INT			NOT NULL	PRIMARY KEY,
                    name	VARCHAR(50)	DEFAULT	'dummy'
                );
ALTER TABLE tab MODIFY COLUMN id INT AUTO_INCREMENT;
-- INSERT INTO tab(name)
-- VALUES	('arishiamio'),
--		('sijid'),
--		('navidio.h');
-- to delete the database uncomment the following
-- DROP DATABASE test;
