import math
import sqlite3 as sql

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

def generateBrakets(numberOfPlayers):
    rounds = int(math.log2(numberOfPlayers)) #--> 16 : 4
    bracket = {}

    for i in range(rounds):
        round = {}
        bracket[i+1] = round
        numberOfMatches = numberOfPlayers // 2
        for i in range(numberOfMatches):
            team1 = teams.pop(0)
            team2 = teams.pop(0)
            round[i+1] = {"T1":team1, "T2":team2}
        numberOfPlayers = numberOfPlayers // 2
       
        # for i in range(numberOfPlayers * 2)


    return bracket


createTable()

tournament = generateBrakets(16)
print(tournament)
createTournament("test",str(tournament))
results = showTouraments()
brackets = (results[0][3])
brackets = eval(brackets)
print(brackets[1]["p1"])

