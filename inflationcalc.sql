/*SQL Script to Create inflationcalc relational database */ 
/*Created using HeidiSQL via Laragon*/
/* Delimiter changed to ; */
/* Connecting to 127.0.0.1 via MariaDB or MySQL (TCP/IP), username root, using password: No ... */
SELECT CONNECTION_ID();
SHOW VARIABLES;
/* Changing character set from latin1 to utf8mb4 */
/* Characterset: utf8mb4 */
SHOW /*!50002 GLOBAL */ STATUS;
SELECT NOW();
/* Connected. Thread-ID: 8 */
/* Reading function definitions from C:\laragon\bin\heidisql\functions-mysql.ini */
SHOW TABLES FROM `information_schema`;
SHOW DATABASES;
/* Entering session "Laragon.MySQL" */
/* Scaling controls to screen DPI: 125% */
USE `performance_schema`;
SELECT `DEFAULT_COLLATION_NAME` FROM `information_schema`.`SCHEMATA` WHERE `SCHEMA_NAME`='performance_schema';
SHOW TABLE STATUS FROM `performance_schema`;
SHOW FUNCTION STATUS WHERE `Db`='performance_schema';
SHOW PROCEDURE STATUS WHERE `Db`='performance_schema';
SHOW TRIGGERS FROM `performance_schema`;
SELECT *, EVENT_SCHEMA AS `Db`, EVENT_NAME AS `Name` FROM information_schema.`EVENTS` WHERE `EVENT_SCHEMA`='performance_schema';
USE `mysql`;
SELECT `DEFAULT_COLLATION_NAME` FROM `information_schema`.`SCHEMATA` WHERE `SCHEMA_NAME`='mysql';
SHOW TABLE STATUS FROM `mysql`;
SHOW FUNCTION STATUS WHERE `Db`='mysql';
SHOW PROCEDURE STATUS WHERE `Db`='mysql';
SHOW TRIGGERS FROM `mysql`;
SELECT *, EVENT_SCHEMA AS `Db`, EVENT_NAME AS `Name` FROM information_schema.`EVENTS` WHERE `EVENT_SCHEMA`='mysql';
USE `information_schema`;
SELECT `DEFAULT_COLLATION_NAME` FROM `information_schema`.`SCHEMATA` WHERE `SCHEMA_NAME`='information_schema';
SHOW TABLE STATUS FROM `information_schema`;
SHOW FUNCTION STATUS WHERE `Db`='information_schema';
SHOW PROCEDURE STATUS WHERE `Db`='information_schema';
SHOW TRIGGERS FROM `information_schema`;
SELECT *, EVENT_SCHEMA AS `Db`, EVENT_NAME AS `Name` FROM information_schema.`EVENTS` WHERE `EVENT_SCHEMA`='information_schema';
USE `sys`;
SELECT `DEFAULT_COLLATION_NAME` FROM `information_schema`.`SCHEMATA` WHERE `SCHEMA_NAME`='sys';
SHOW TABLE STATUS FROM `sys`;
SHOW FUNCTION STATUS WHERE `Db`='sys';
SHOW PROCEDURE STATUS WHERE `Db`='sys';
SHOW TRIGGERS FROM `sys`;
SELECT *, EVENT_SCHEMA AS `Db`, EVENT_NAME AS `Name` FROM information_schema.`EVENTS` WHERE `EVENT_SCHEMA`='sys';
USE `performance_schema`;
USE `information_schema`;
USE `performance_schema`;
USE `mysql`;
USE `information_schema`;
SHOW COLLATION;
SHOW VARIABLES;
CREATE DATABASE `inflationCalc` /*!40100 COLLATE 'utf8mb4_0900_ai_ci' */;
SHOW DATABASES;
/* Entering session "Laragon.MySQL" */
USE `inflationcalc`;
SELECT `DEFAULT_COLLATION_NAME` FROM `information_schema`.`SCHEMATA` WHERE `SCHEMA_NAME`='inflationcalc';
SHOW TABLE STATUS FROM `inflationcalc`;
SHOW FUNCTION STATUS WHERE `Db`='inflationcalc';
SHOW PROCEDURE STATUS WHERE `Db`='inflationcalc';
SHOW TRIGGERS FROM `inflationcalc`;
SELECT *, EVENT_SCHEMA AS `Db`, EVENT_NAME AS `Name` FROM information_schema.`EVENTS` WHERE `EVENT_SCHEMA`='inflationcalc';
SHOW VARIABLES;
SHOW CREATE DATABASE `inflationcalc`;
ALTER DATABASE `inflationcalc` COLLATE 'utf8mb4_0900_ai_ci';
SHOW DATABASES;
/* Entering session "Laragon.MySQL" */
SELECT `DEFAULT_COLLATION_NAME` FROM `information_schema`.`SCHEMATA` WHERE `SCHEMA_NAME`='inflationcalc';
SHOW TABLE STATUS FROM `inflationcalc`;
SHOW FUNCTION STATUS WHERE `Db`='inflationcalc';
SHOW PROCEDURE STATUS WHERE `Db`='inflationcalc';
SHOW TRIGGERS FROM `inflationcalc`;
SELECT *, EVENT_SCHEMA AS `Db`, EVENT_NAME AS `Name` FROM information_schema.`EVENTS` WHERE `EVENT_SCHEMA`='inflationcalc';
SHOW ENGINES;
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
/* #40: Abstract Error Message CharCode:0 Msg:514 */
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
CREATE TABLE `Products` (
	`ProductID` INT NULL,
	`Name` VARCHAR(50) NULL DEFAULT NULL,
	`SKU` VARCHAR(50) NULL DEFAULT NULL,
	`Description` VARCHAR(50) NULL DEFAULT NULL,
	`Brand name` VARCHAR(50) NULL DEFAULT NULL,
	`URL` VARCHAR(100) NULL DEFAULT NULL
)
COLLATE='utf8mb4_0900_ai_ci'
;
SELECT `DEFAULT_COLLATION_NAME` FROM `information_schema`.`SCHEMATA` WHERE `SCHEMA_NAME`='inflationcalc';
SHOW TABLE STATUS FROM `inflationcalc`;
SHOW FUNCTION STATUS WHERE `Db`='inflationcalc';
SHOW PROCEDURE STATUS WHERE `Db`='inflationcalc';
SHOW TRIGGERS FROM `inflationcalc`;
SELECT *, EVENT_SCHEMA AS `Db`, EVENT_NAME AS `Name` FROM information_schema.`EVENTS` WHERE `EVENT_SCHEMA`='inflationcalc';
SELECT * FROM `information_schema`.`COLUMNS` WHERE TABLE_SCHEMA='inflationcalc' AND TABLE_NAME='products' ORDER BY ORDINAL_POSITION;
SHOW INDEXES FROM `products` FROM `inflationcalc`;
SELECT * FROM information_schema.REFERENTIAL_CONSTRAINTS WHERE   CONSTRAINT_SCHEMA='inflationcalc'   AND TABLE_NAME='products'   AND REFERENCED_TABLE_NAME IS NOT NULL;
SELECT * FROM information_schema.KEY_COLUMN_USAGE WHERE   TABLE_SCHEMA='inflationcalc'   AND TABLE_NAME='products'   AND REFERENCED_TABLE_NAME IS NOT NULL;
/* Entering session "Laragon.MySQL" */
SHOW CREATE TABLE `inflationcalc`.`products`;
SELECT tc.CONSTRAINT_NAME, cc.CHECK_CLAUSE FROM `information_schema`.`CHECK_CONSTRAINTS` AS cc, `information_schema`.`TABLE_CONSTRAINTS` AS tc WHERE tc.CONSTRAINT_SCHEMA='inflationcalc' AND tc.TABLE_NAME='products' AND tc.CONSTRAINT_TYPE='CHECK' AND tc.CONSTRAINT_SCHEMA=cc.CONSTRAINT_SCHEMA AND tc.CONSTRAINT_NAME=cc.CONSTRAINT_NAME;
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
CREATE TABLE `prices` (
	`PriceID` INT NULL,
	`ProductID` INT NULL,
	`OldTS` INT NULL,
	`NewTS` INT NULL,
	`OldPrice` INT NULL,
	`NewPrice` INT NULL
)
COLLATE='utf8mb4_0900_ai_ci'
;
SELECT `DEFAULT_COLLATION_NAME` FROM `information_schema`.`SCHEMATA` WHERE `SCHEMA_NAME`='inflationcalc';
SHOW TABLE STATUS FROM `inflationcalc`;
SHOW FUNCTION STATUS WHERE `Db`='inflationcalc';
SHOW PROCEDURE STATUS WHERE `Db`='inflationcalc';
SHOW TRIGGERS FROM `inflationcalc`;
SELECT *, EVENT_SCHEMA AS `Db`, EVENT_NAME AS `Name` FROM information_schema.`EVENTS` WHERE `EVENT_SCHEMA`='inflationcalc';
SELECT * FROM `information_schema`.`COLUMNS` WHERE TABLE_SCHEMA='inflationcalc' AND TABLE_NAME='prices' ORDER BY ORDINAL_POSITION;
SHOW INDEXES FROM `prices` FROM `inflationcalc`;
SELECT * FROM information_schema.REFERENTIAL_CONSTRAINTS WHERE   CONSTRAINT_SCHEMA='inflationcalc'   AND TABLE_NAME='prices'   AND REFERENCED_TABLE_NAME IS NOT NULL;
SELECT * FROM information_schema.KEY_COLUMN_USAGE WHERE   TABLE_SCHEMA='inflationcalc'   AND TABLE_NAME='prices'   AND REFERENCED_TABLE_NAME IS NOT NULL;
/* Entering session "Laragon.MySQL" */
SHOW CREATE TABLE `inflationcalc`.`prices`;
SELECT tc.CONSTRAINT_NAME, cc.CHECK_CLAUSE FROM `information_schema`.`CHECK_CONSTRAINTS` AS cc, `information_schema`.`TABLE_CONSTRAINTS` AS tc WHERE tc.CONSTRAINT_SCHEMA='inflationcalc' AND tc.TABLE_NAME='prices' AND tc.CONSTRAINT_TYPE='CHECK' AND tc.CONSTRAINT_SCHEMA=cc.CONSTRAINT_SCHEMA AND tc.CONSTRAINT_NAME=cc.CONSTRAINT_NAME;
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
/* #1634496361: Access violation at address 00000000005DE1FB in module 'heidisql.exe'. Read of address 0000000000000000 Message CharCode:13 Msg:256 */
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
CREATE TABLE `Results` (
	`ResultID` INT NULL,
	`Basket1` INT NULL,
	`Basket2` INT NULL,
	`Basket3` INT NULL,
	`CPI Old ` INT NULL,
	`CPI New` INT NULL,
	`predictionInf` INT NULL,
	`measFreq` INT NULL
)
COLLATE='utf8mb4_0900_ai_ci'
;
/* SQL Error (1166): Incorrect column name 'CPI Old ' */
/* #1634496361: Access violation at address 00000056C1800000 in module 'heidisql.exe'. Execution of address 00000056C1800000 Message CharCode:13 Msg:256 */
/* #1634496361: Access violation at address 00000000005DE1FB in module 'heidisql.exe'. Read of address 0000000000000000 Message CharCode:13 Msg:256 */
CREATE TABLE `Results` (
	`ResultID` INT NULL,
	`Basket1` INT NULL,
	`Basket2` INT NULL,
	`Basket3` INT NULL,
	`oldCPI` INT NULL,
	`newCPI` INT NULL,
	`predictionInf` INT NULL,
	`measFreq` INT NULL
)
COLLATE='utf8mb4_0900_ai_ci'
;
SELECT `DEFAULT_COLLATION_NAME` FROM `information_schema`.`SCHEMATA` WHERE `SCHEMA_NAME`='inflationcalc';
SHOW TABLE STATUS FROM `inflationcalc`;
SHOW FUNCTION STATUS WHERE `Db`='inflationcalc';
SHOW PROCEDURE STATUS WHERE `Db`='inflationcalc';
SHOW TRIGGERS FROM `inflationcalc`;
SELECT *, EVENT_SCHEMA AS `Db`, EVENT_NAME AS `Name` FROM information_schema.`EVENTS` WHERE `EVENT_SCHEMA`='inflationcalc';
SELECT * FROM `information_schema`.`COLUMNS` WHERE TABLE_SCHEMA='inflationcalc' AND TABLE_NAME='results' ORDER BY ORDINAL_POSITION;
SHOW INDEXES FROM `results` FROM `inflationcalc`;
SELECT * FROM information_schema.REFERENTIAL_CONSTRAINTS WHERE   CONSTRAINT_SCHEMA='inflationcalc'   AND TABLE_NAME='results'   AND REFERENCED_TABLE_NAME IS NOT NULL;
SELECT * FROM information_schema.KEY_COLUMN_USAGE WHERE   TABLE_SCHEMA='inflationcalc'   AND TABLE_NAME='results'   AND REFERENCED_TABLE_NAME IS NOT NULL;
/* Entering session "Laragon.MySQL" */
SHOW CREATE TABLE `inflationcalc`.`results`;
SELECT tc.CONSTRAINT_NAME, cc.CHECK_CLAUSE FROM `information_schema`.`CHECK_CONSTRAINTS` AS cc, `information_schema`.`TABLE_CONSTRAINTS` AS tc WHERE tc.CONSTRAINT_SCHEMA='inflationcalc' AND tc.TABLE_NAME='results' AND tc.CONSTRAINT_TYPE='CHECK' AND tc.CONSTRAINT_SCHEMA=cc.CONSTRAINT_SCHEMA AND tc.CONSTRAINT_NAME=cc.CONSTRAINT_NAME;
SELECT * FROM `information_schema`.`COLUMNS` WHERE TABLE_SCHEMA='inflationcalc' AND TABLE_NAME='products' ORDER BY ORDINAL_POSITION;
SHOW INDEXES FROM `products` FROM `inflationcalc`;
SELECT * FROM information_schema.REFERENTIAL_CONSTRAINTS WHERE   CONSTRAINT_SCHEMA='inflationcalc'   AND TABLE_NAME='products'   AND REFERENCED_TABLE_NAME IS NOT NULL;
SELECT * FROM information_schema.KEY_COLUMN_USAGE WHERE   TABLE_SCHEMA='inflationcalc'   AND TABLE_NAME='products'   AND REFERENCED_TABLE_NAME IS NOT NULL;
SHOW CREATE TABLE `inflationcalc`.`products`;
SELECT tc.CONSTRAINT_NAME, cc.CHECK_CLAUSE FROM `information_schema`.`CHECK_CONSTRAINTS` AS cc, `information_schema`.`TABLE_CONSTRAINTS` AS tc WHERE tc.CONSTRAINT_SCHEMA='inflationcalc' AND tc.TABLE_NAME='products' AND tc.CONSTRAINT_TYPE='CHECK' AND tc.CONSTRAINT_SCHEMA=cc.CONSTRAINT_SCHEMA AND tc.CONSTRAINT_NAME=cc.CONSTRAINT_NAME;
SHOW CREATE TABLE `inflationcalc`.`results`;
