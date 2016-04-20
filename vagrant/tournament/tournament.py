#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


#  def connect():
    #  """Connect to the PostgreSQL database.  Returns a database connection."""
#      return psycopg2.connect("dbname=tournament")

def connect(databaseName = 'tournament'):
    """
    Connect to the PostgreSQL database. Return s a database connection and coursor

    Refactor connect function to make more code readable, maintainable and shorter.
    """
    try:
        db = psycopg2.connect('dbname={}'.format(databaseName))
        cursor = db.cursor()
        return db, cursor
    except:
        print 'failed to connect to database'


def deleteMatches():
    """Remove all the match records from the database."""
    db, c = connect()
    sql = 'TRUNCATE matches'
    c.execute(sql)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, c = connect()
    # table matches references players, so we need TRUNCATE matches here
    sql = 'TRUNCATE players, matches'
    c.execute(sql)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, c = connect()
    query = 'SELECT count(*) FROM players'
    c.execute(query)
    rows= c.fetchall()

    count = rows[0][0]

    db.close()

    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, c = connect()
    query = 'INSERT INTO players VALUES (%s)'
    param = (name,)
    c.execute(query, param)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, c = connect()
    query = 'SELECT id, name, wins, games FROM standings'
    c.execute(query)
    rows = c.fetchall()
    db.close()

    return [(row[0], row[1], row[2], row[3]) for row in rows]


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, c = connect()
    query = 'INSERT INTO matches VALUES (%s, %s)'
    params = (winner, loser,)
    c.execute(query, params)
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    if len(standings) % 2 != 0:
        print 'The number of players is not even'
        return

    return  map(lambda (x, y): (x[0], x[1], y[0], y[1]), zip(standings[0::2], standings[1::2]))

