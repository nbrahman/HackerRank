'''
Meereen is famous for its fighting pits where fighters fight each other to the death.

Initially, there are n fighters and each fighter has a strength value. The n fighters are divided into k teams, and each fighter belongs exactly one team. For each fight, the Great Masters of Meereen choose two teams, x and y, that must fight each other to the death. The teams attack each other in alternating turns, with team x always launching the first attack. The fight ends when all the fighters on one of the teams are dead.

Assume each team always attacks optimally. Each attack is performed as follows:

    The attacking team chooses a fighter from their team with strength s.
    The chosen fighter chooses at most s fighters from other team and kills all of them.

The Great Masters don't want to see their favorite fighters fall in battle, so they want to build their teams carefully and know who will win different team matchups. They want you to perform two type of queries:

    1 p x Add a new fighter with strength p to team x. It is guaranteed that this new fighter's strength value will not be less than any current member of team x.
    2 x y Print the name of the team that would win a matchup between teams x and y in their current state (recall that team x always starts first). It is guaranteed that x != y.

Given the initial configuration of the teams and queries, perform each query so the Great Masters can plan the next fight.

Note: You are determining the team that would be the winner if the two teams fought. No fighters are actually dying in these matchups so, once added to a team, a fighter is available for all future potential matchups.

Input Format

The first line contains three space-separated integers describing the respective values of n (the number of fighters), k (the number of teams), and q (the number of queries).
Each line i of the n subsequent lines contains two space-separated integers describing the respective values of fighter i's strength, s[i], and team number, t[i].
Each of the q subsequent lines contains a space-separated query in one of the two formats defined in the Problem Statement above (i.e., 1 p x or 2 x y).

Constraints
1<=n,q<=2*10^5
2<=k<=2*10^5
1<=x,y,t[i]<=k
1<=s[i],p<=2*10^5
It is guaranteed that both teams in a query matchup will always have at least one fighter.

Scoring
This challange has binary scoring. This means you will get a full score if your solution passes all test cases; otherwise, you will get 0 points.

Output Format

After each type 2 query, print the name of the winning team on a new line. For example, if x=1 and y=2 are matched up and x wins, you would print 1.

Sample Input

7 2 6
1 1
2 1
1 1
1 2
1 2
1 2
2 2
2 1 2
2 2 1
1 2 1
1 2 1
2 1 2
2 2 1

Sample Output

1
2
1
1

Explanation

Team 1 has three fighters with the following strength levels: s1={1,1,2}.
Team 2 has four fighters with the following strength levels: s2={1,1,1,2}.

The first query matching up team x=1 and y=2 would play out as follows:

    1. Team x=1 attacks -> The fighter with strength 2 can kill one fighter with strength 2 and one fighter with strength 1. Now, s1={1,1,2}, and s2={1,1}.
    2. Team x=2 attacks -> The fighter with strength 1 can kill one fighter with strength 1. Now, s1={1,1}, and s2={1,1}.
    3. Team x=1 attacks -> The fighter with strength 1 can kill one fighter with strength 1. Now, s1={1,1}, and s2={1}.
    4. Team x=2 attacks -> The fighter with strength 1 can kill one fighter with strength 1. Now, s1={1}, and s2={1}.
    5. Team x=1 attacks -> The fighter with strength 1 can kill one fighter with strength 1. Now, s1={1}, and s2={}.

After this last attack, all of Team 2's fighters would be dead. Thus, we print as team would win that fight.
'''

import sys
#all_input = sys.stdin.readlines()

class FightingPits:
    def __init__(self):
        self.numPlayers, self.numTeams, self.numQueries = input().strip().split(' ')
        self.numPlayers, self.numTeams, self.numQueries = [int(self.numPlayers), int(self.numTeams), int(self.numQueries)]
        self.allPlayers = []
        self.allQueries = []

    def prepare(self):
        for i in range (0,self.numPlayers):
            t = input().strip().split(' ')
            self.allPlayers.append ([int (t[0]),int(t[1])])
        print (self.allPlayers)
        for i in range (0,self.numQueries):
            t = input().strip().split(' ')
            self.allQueries.append ([int (t[0]),int(t[1]),int(t[2])])
        print (self.allQueries)
        if self.numPlayers != len(self.allPlayers):
            print("Problem with the number of players")
            print(self.numPlayers, "numPlayers ;", self.allPlayers, " all Players" )
        elif self.numQueries != len(self.allQueries):
            print("Problem with the number of queries")
        #else:
            #print("the game has initialized successfully")
            #pass

    def fight(self):
        self.teams = self.prepareTeams(self.allPlayers, self.numTeams)
        self.executeQueries(self.allQueries, self.numQueries)


    def executeQueries(self, allQueries, numQueries):
        if numQueries != len(allQueries):
            print("Problem with the number of queries")
        else:
            for query in allQueries:
                if query[0] == 1:
                    self.executeAddPlayerQuery(query)
                elif query[0] == 2:
                    self.executeFightMatchQuery(query)
                else:
                    "could not match query"

    def executeFightMatchQuery(self, query):
        teamXnum = query[1]
        teamYnum = query[2]
        teamX = sorted(self.teams[teamXnum])
        teamY = sorted(self.teams[teamYnum])
        if (len(teamX) < 1) or (len(teamY) < 1):
            print("one of the teams doesn't exist", query)
        else:
            isMatchFinished = False
            while not isMatchFinished:
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

    def executeAddPlayerQuery(self, query):
        self.teams[query[2]].append(query[1])

    def prepareTeams(self, allPlayers, numTeams):
        teams = [[] for i in range(numTeams+1)]
        len(teams)
        for player in allPlayers:
            teams[player[1]].append(player[0])
        return teams



if __name__ == "__main__":
    #all_input= '''7 2 6
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
    fight = FightingPits()
    fight.prepare()
    fight.fight()