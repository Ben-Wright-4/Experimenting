import math
import sqlite3 as sql
from flask import render_template

teams = ["Team1", "Team2","Team3", "Team4","Team5", "Team6","Team7", "Team8", "Team9", "Team10","Team11", "Team12","Team13", "Team14","Team15", "Team16"]
def createTable():
    try:
        connection = sql.connect("data.db")
        connection.execute('''
                            create table tournament (
                                tournamentID integer primary key autoincrement,
                                tournamentName text not null,
                                active text,
                                rounds text
                        )''')
    except Exception as e:
        print(e)
    finally:
        connection.close()


def showTouraments():
    try:
        connection = sql.connect("data.db")
        cursor = connection.cursor()
        results = cursor.execute("""select * from tournament""").fetchall()
    except Exception as e:
        print(e)
        results = []
    finally:
        return results

def createTournament(name, brackets):
    try:
        connection = sql.connect("data.db")
        connection.execute("""insert into tournament (tournamentName, active, rounds) values (?,false,?)""",(name,brackets))
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

def generateBrackets(numTeams):
    global teamsList
    teamsList = teams
    numberOfTeams = numTeams
    numRounds = int(math.log2(numTeams))
    bracket = {}

    for i in range(numRounds):
        round = {}
        bracket[i+1]= round
        numMatches = numberOfTeams // 2
        for i in range(numMatches):
            round[i+1] = {"T1":None, "T2":None}

        numberOfTeams = numberOfTeams // 2

    for i in range (numTeams//2):
        team1 = teams.pop(0)
        team2 = teams.pop(0)
        bracket[1][i+1]["T1"] = team1
        bracket[1][i+1]["T2"] = team2

    return bracket


# createTable()

tournament = generateBrackets(16)
print(tournament)
createTournament("test",str(tournament))
results = showTouraments()
brackets = (results[0][3])
brackets = eval(brackets)
print(brackets[1][1]["T1"])

