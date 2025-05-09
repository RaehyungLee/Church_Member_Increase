from math import floor as lower

class Church:
    def __init__(self, name):
        self.name = name
        self.numMembers = 0

class Evangelism(Church):

    def __init__(self, name):
        super().__init__(name)
        self.evMembers = 0
        

    def futureMember(self, period, grace ,evRatio=0.5, evanSprit=0.05): 
        #period: Per year evanSprit: Chance to make people evangelize
        #evRatio: newMembers/evMembers like ev success rate
        
        total_member = self.numMembers

        for year in range(1, period + 1):
            print(f"We have {total_member} people")
            newMember = lower(self.evMembers * evRatio)   # number of new brothers
            total_member += newMember
            
            print(f"Total member after {year} year is {total_member}, {newMember} people increased.")
            left_people = lower(newMember * grace)
            total_member = total_member - newMember + left_people


            print(f"However, God only chose {left_people} more people")
            evangelistic_hearts = lower(left_people * evanSprit) # holy spirit gives them hearts
            self.evMembers += evangelistic_hearts       # new ev team
        
        return total_member
    
EV_Team = Evangelism('MyChurch')

EV_Team.numMembers = 100
EV_Team.evMembers = 10

EV_Team.futureMember(10, 0.1, 10, 0) #With Holy Spirit
EV_Team.futureMember(10, 0.1, 10, 0.5) #Without Holy Spirit




            







    



