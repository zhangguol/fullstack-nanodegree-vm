-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Drop tournament database if it exists
DROP DATABASE IF EXISTS tournament;

-- Create database
CREATE DATABASE tournament;

-- Connect to tournament
\c tournament;

-- Create player table with structure
--
-- Column   |   Type    |   Modifiers
-- ---------+-----------+-----------------
-- id       |   SERIAL  | primary key
-- ---------+-----------+-----------------
-- name     |   text    |   
-- ---------------------------------------
CREATE TABLE players (
    name text,
    id SERIAL PRIMARY KEY
);

-- Create matches table with structure
-- Column   |   Type    |   Modifiers
-- ---------+-----------+------------------------
-- id       |   SERIAL  | primary key
-- ---------+-----------+------------------------
-- winner   |   integer | reference id in player
-- ----------------------------------------------
-- loser    |   integer | reference id in player
-- ----------------------------------------------
CREATE TABLE matches (
    winner integer REFERENCES players,
    loser integer REFERENCES players,
    id SERIAL PRIMARY KEY
);

-- Create a view named stangdings with structure
--   Column   |  Type   | Modifiers
--  ----------+---------+-----------
--  player_id | integer |
--  name      | text    |
--  wins      | integer |
--  played    | integer |
CREATE VIEW standings AS
SELECT players.id,
    players.name,
    (SELECT count(*) FROM matches WHERE winner = players.id) as wins,
    (SELECT count(*) FROM matches WHERE winner = players.id or loser = players.id) as games
FROM players
GROUP BY players.id
ORDER BY wins DESC;







