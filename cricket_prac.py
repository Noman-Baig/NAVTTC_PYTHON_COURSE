total_players = 10

total_balls_a = 26
total_balls_b = 26

runsA = 0
runsB = 0

wicketsA = 0
wicketsB = 0

print("\n===== Match Start (TEAM A) ======\n")
for i in range(total_balls_a):
    shot = input(f"\nBall > {total_balls_a} | Runs {runsA}/ Outs {wicketsA} Player{wicketsA+1} : ")
    
    if not shot:
        print("Press O/Out for out || 1-6 for Runs")
    elif(shot.lower() == "out" or shot.lower() == "o"):
        total_balls_a-=1
        wicketsA+=1
        if(wicketsA == total_players):
            print(f"\nAll Players out | Total Score {runsA}\n")
            wicketsA = 0
            break
    else:
        if(int(shot)>6 or int(shot)<0):
            print("Only 0-6 Runs Allowed")
        else:    
            total_balls_a-=1
            runsA += int(shot)
            # print(f"total runs {runsA} total out {wicketsA}")   
      
print("\n===== Match Start (TEAM B) ======\n")
for i in range(total_balls_b):
    shot = input(f"\nBall > {total_balls_b} | Runs {runsB}/ Outs {wicketsB} Player{wicketsB+1} : ")
    
    if not shot:
        print("Press O/Out for out || 1-6 for Runs")
    elif(shot.lower() == "out" or shot.lower() == "o"):
        total_balls_b-=1
        wicketsB+=1
        if(wicketsB == total_players):
            print(f"\nAll Players out | Total Score {runsB}\n")
            wicketsB = 0
            break
    else:
        if(int(shot)>6 or int(shot)<0):
            print("Only 0-6 Runs Allowed")
        else:    
            total_balls_b-=1
            runsB += int(shot)
            # print(f"total runs {runsB} total out {wicketsB}")   
      
    
if (runsA > runsB):
 print(f"\nTeam A Win the Match || Total Runs {runsA}!")
elif (runsB > runsA):
 print(f"\nTeam B Win the Match || Total Runs {runsB}!")
else:
 print("\nDraw hogaya bhai !")     
