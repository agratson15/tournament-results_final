#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()
    c.execute("DELETE FROM Matches;")
    conn.commit()
    conn.close()   

def deletePlayers():
    """Remove all the player records from the database."""
    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()
    c.execute("DELETE FROM Players;")
    conn.commit()
    conn.close()    

def countPlayers():
    """Returns the number of players currently registered.

        The for loop is counting every row in the cursor (that just counted all players in the Players table).
        Found this snippet on the udacity forums.
    """
    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM Players;")
    for row in c:
        return row[0]
    conn.commit()
    conn.close()

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()
    c.execute("INSERT INTO Players (id, name) VALUES (DEFAULT, %s) returning id", (name,))
    player_id = c.fetchone()[0]
    conn.commit()
    conn.close()

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

    Found the 'row for row' in the udacity forums to help fill the gap.
    """
    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()
    c.execute("SELECT * FROM playerStandings;")
    standings = c.fetchall()
    standingList = [row for row in standings if row[0] != 0]
    conn.commit()
    conn.close()
    return standingList

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()
    c.execute("INSERT INTO Matches(winner, loser) VALUES (%s,%s)", (winner, loser, ))
    conn.commit()
    conn.close() 
 
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

    The for loop below is looping through the standings table and taking every second
    row and placing it in a tuple list of (id1, name1, id2, name2) and goes through all the 
    players in the tournament - only taking account for even amount of players.
    """
    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()

    Pairings = []

    c.execute("SELECT * FROM playerStandings;")
    standings = c.fetchall()
    
    for index, row in enumerate(standings):
        if index % 2 == 0:
            Pairings.append([standings[index][0],standings[index][1],standings[index+1][0],standings[index+1][1]])

    conn.commit()
    conn.close()
    return Pairings
