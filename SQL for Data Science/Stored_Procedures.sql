CREATE DATABASE fun;

USE fun;

CREATE TABLE players
(
player_id INT,
player_name VARCHAR(25),
country VARCHAR(50),
goals INT
);

SELECT * FROM players;


INSERT INTO players VALUES (1,'Lionel Messi','Argentina',200);
INSERT INTO players VALUES (2,'Christiano Ronaldo','Portugal',100);
INSERT INTO players VALUES (3,'Lamine Yamal','Spain',50);
INSERT INTO players VALUES (4,'Mbappe','France',56);
INSERT INTO players VALUES (5,'Guvi','Spain',65);
INSERT INTO players VALUES (6,'Jude Bellingham','England',64);
INSERT INTO players VALUES (7,'Neimar','Brazil',170);
INSERT INTO players VALUES (8,'Halland','Norway',125);
INSERT INTO players VALUES (9,'Jindal','Iran',5);
INSERT INTO players VALUES (10,'Mohamed Salah','Egypt',8);


# Return the list of players that have scored greater than 50 goals in tour
SELECT * FROM players WHERE goals > 50;
SELECT player_name,country,goals FROM players WHERE goals > 50;

# Store Procedure for the above query
DELIMITER &&
CREATE PROCEDURE top_players()
BEGIN
SELECT player_name,country,goals FROM players WHERE goals > 50;
END &&
DELIMITER ;

CALL top_players();



# STORED PROCEDURES : IN & OUT (IN - Input , OUT : Output)

# STORED PROCEDURED USING IN
# Lets create a procedure which returns the top players based on goals :
# top(5) -->
SELECT player_name,goals FROM players ORDER BY goals DESC LIMIT 5;

# top(n) -->
DELIMITER //
CREATE PROCEDURE top_players_sort_by_goals(IN var INT)
BEGIN
SELECT player_name,country,goals FROM players ORDER BY goals DESC LIMIT var;
END //
DELIMITER ;

CALL top_players_sort_by_goals(3);
CALL top_players_sort_by_goals(5);


# UPDATE 
SET SQL_SAFE_UPDATES=0;
UPDATE players SET goals=15 WHERE player_name='Christiano Ronaldo';

# UPDATE AUTOMATICALLY STORED PROCEDURE
DELIMITER //
CREATE PROCEDURE update_players(IN num INT,IN player VARCHAR(25))
BEGIN
UPDATE players SET goals=num WHERE player_name=player;
END //
DELIMITER ;

CALL update_players(25,'Lionel Messi');
CALL update_players(5,'Lamine Yamal');
CALL update_players(6,'Mbappe');
CALL update_players(3,'Guvi');

SELECT * FROM players;


# STORED PROCEDURES USING OUT

SELECT COUNT(*) FROM players;

DELIMITER //
CREATE PROCEDURE player_count(OUT total_players INT)
BEGIN
SELECT COUNT(*) FROM players INTO total_players;
END //
DELIMITER ;

CALL player_count(@total_count);
SELECT @total_count AS Total_Count;


# Using IN
DELIMITER //
CREATE PROCEDURE player_count_in()
BEGIN
SELECT COUNT(*) FROM players;
END //
DELIMITER ;

CALL player_count_in();


# Using IN and OUT
DELIMITER //
CREATE PROCEDURE player_count_country(IN var VARCHAR(25), OUT total_players INT)
BEGIN
SELECT COUNT(*) FROM players WHERE country = var INTO total_players;
END //
DELIMITER ;


CALL player_count_country('Spain', @total_count);
SELECT @total_count AS Total_Count;

# Without OUT
DELIMITER //
CREATE PROCEDURE player_count_country_new(IN var VARCHAR(25))
BEGIN
SELECT COUNT(*) FROM players WHERE country = var;
END //
DELIMITER ;

CALL player_count_country_new('Spain');











