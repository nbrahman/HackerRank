#!/usr/bin/python
import sys
#let's play a game
user_input = sys.stdin.readlines()

class Game:
    def __init__(self, user_input):
        self.user_input = user_input

    def setup(self):
#            self.user_input = self.user_input.splitlines()
            for i, x in enumerate(self.user_input):
                self.user_input[i] = list(map(int, x.strip().split()))

            self.numPlayers = self.user_input[0][0]
            self.numTeams = self.user_input[0][1]
            self.numQueries = self.user_input[0][2]

            self.allPlayers = self.user_input[1:self.numPlayers+1]
            print (self.allPlayers)
            self.allQueries = self.user_input[self.numPlayers+1:self.numPlayers+1+self.numQueries]
            print (self.allQueries)
            if self.numPlayers != len(self.allPlayers):
                print("error, problem with the number of players")
                print(self.numPlayers, "numPlayers ;", self.allPlayers, " all Players" )
            elif self.numQueries != len(self.allQueries):
                print("error, problem with the number of queries")
            else:
                #print("the game has initialized successfully")
                pass

    def run(self):
        self.teams = self.makeTeams(self.allPlayers, self.numTeams)
        #print(self.teams)
        self.runQueries(self.allQueries, self.numQueries)


    def runQueries(self, allQueries, numQueries):
        if numQueries != len(allQueries):
            print("error, problem with the number of queries")
        else:
            for query in allQueries:
                if query[0] == 1:
                    self.addPlayer(query)
                elif query[0] == 2:
                    self.runMatch(query)
                else:
                    "could not match query"

    def runMatch(self, query):
        teamXnum = query[1]
        teamYnum = query[2]
        teamX = sorted(self.teams[teamXnum])
        teamY = sorted(self.teams[teamYnum])
        if (len(teamX) < 1) or (len(teamY) < 1):
            print("one of the teams doesn't exist", query)
        else:
            isMatchFinished = False
            while not isMatchFinished:
#                print("teamY", teamY, "teamX", teamX)
                ##team x attack
                xStrength = teamX[-1]
                if xStrength < len(teamY):
                    teamY = teamY[0:-xStrength]
                else:
                    teamY = []
                if len(teamY) < 1:
                    print(teamXnum)
                    isMatchFinished = True
                    break
                ##team y attack
                yStrength = teamY[-1]
                if yStrength < len(teamX):
                    teamX = teamX[0:-yStrength]
                else:
                    teamX = []
                if len(teamX) < 1:
                    print(teamYnum)
                    isMatchFinished = True
                    break
                if (len(teamX) < 1) or (len(teamY) < 1):
                    isMatchFinished = True
                    break

    def addPlayer(self, query):
#        print("adding Player")
#        print(self.teams[query[2]])
        self.teams[query[2]].append(query[1])
#        print(self.teams[query[2]])

    def makeTeams(self, allPlayers, numTeams):
        teams = [[] for i in range(numTeams+1)]
        len(teams)
        for player in allPlayers:
            teams[player[1]].append(player[0])
#        print(teams)
        return teams



if __name__ == "__main__":
    #user_input= '''7 2 6
    #    1 1
    #    2 1
    #    1 1
    #    1 2
    #    1 2
    #    1 2
    #    2 2
    #    2 1 2
    #    2 2 1
    #    1 2 1
    #    1 2 1
    #    2 1 2
    #    2 2 1'''
    game = Game(user_input)
    game.setup()
    game.run()