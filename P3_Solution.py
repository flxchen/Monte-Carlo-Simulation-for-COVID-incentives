#example of monte carlo simulation to estimate pi value
import random
import csv
from statistics import *
def findPi(numPoints,details,times):
    numPoints = numPoints
    numHits = 0
    average = 0; total = 0
    times = times
    details=details #Set to true to print all the random points.
    for j in range(times):
        numHits = 0        
        total = 0
        for i in range(1,numPoints+1):
            x = random.random()
            y = random.random()    
            f = x**2 + y**2
                        
            if f < 1:
                numHits +=1             
            if details:
                print ('Random point number', i,' :',f,' numHits:',numHits,' numPoints:',numPoints)
        total += 4*numHits/numPoints
        average += total
        #print('Pi value',j+1,',',total)
    average /= times    
    #print ('the average Pi value over ',times,' times','with ',numPoints,' points is: ', average,'.')
    return average
    

#COVID vaccine Monte Carlo simulation to estimate average profit
#Vaccine 1 requires two shots
#Vaccine 2 and 3 needs one shot
#1/3 of students receiving vaccine get Incentive 1, Incentive 1 gives out three game1 tickets
#1/3 of students receiving vaccine get Incentive 2, Incentive 2 gives out three game2 tickets
#Every 200 students receive Incentive 3 
#Game 1: 10% to win 100 dollars
#Game 2: 5% to win 300 dollars
#Incentive 3: Every 200 stduents win a paid round trip to Hawaii plus 300 cash 
def findAvgProfit():
    Total = 0
    TotalStudent = 600
    #Vaccine = 0 #vaccine is 1,2,or 3
    Vaccine1Num = 0
    Vaccine2Num = 0
    Vaccine3Num = 0
    Game1Num = 0 #number of times winning game1
    Game2Num = 0 #number of times winning game2
    Inecentive3Num = 0 #number of times winning incentive3
    times = 0 #total eligibility of play game1 and 2
    Game = 0 #game is 1 or 2
    ticket = 3 # a student gets three tickets for incentive 1 and 2
    Incentive1Probability = 1/3 #probability of getting incentive 1
    Incentive2Probability = 2/3 #probability of getting incentive 2
    Game1Probability = 1/10 #probability of winning game1
    Game2Probability = 1/20 #probability of winning game2
    totalTimes = 0 #total times of receiving vaccines
    details = False 
    eligible = False # whether a student are eligible for lottery games   
    for student in range(TotalStudent+Vaccine1Num):
        probVac = random.random() # prob of which Vaccine a student receives
        eligible = False
        if probVac < Incentive1Probability:                                  
            Vaccine1Num += 1
            eligible = True          
        if probVac > Incentive1Probability and probVac < Incentive2Probability:              
            Vaccine2Num += 1
            eligible = True
        if student <= TotalStudent:
            if probVac > Incentive2Probability:
                Vaccine3Num += 1
                eligible = False
            if student % 200 == 0:            
                Total += 300
                Inecentive3Num += 1
                eligible = False            
        else:
            eligible = False
        
        if eligible:
            probGame = random.random() # prob of which game a student is elgible to play 
            if probGame < Incentive1Probability:
                Game = 1     
            if probGame > Incentive1Probability and probGame < Incentive2Probability:
                Game = 2
            for num in range(ticket):
                probInc = random.random() # prob of which incentive a student gets
                if Game == 1 and probInc < Game1Probability:
                    Total += 100
                    Game1Num += 1
                if Game == 2 and probInc < Game2Probability:
                    Total += 300
                    Game2Num += 1
    totalTimes = 2*Vaccine1Num+Vaccine2Num+Vaccine3Num 
    times = 2*Vaccine1Num+Vaccine2Num             
    if details:        
        print('money: ',Total,'\nvaccine1 student: ',Vaccine1Num,'\nvaccine2 student: ',Vaccine2Num,'\nvaccine3 student:',Vaccine3Num,
        '\ntotal times: ',totalTimes,'\ntotal times of play game1 and 2: ',times 
        ,'\nGame1 win: ',Game1Num, ' Game1 win probability: ',Game1Num/times,'\nGame2 win: ',Game2Num,' Game2 winprobability: ',Game2Num/times,
        '\nincentive3 win: ',Inecentive3Num)
    #print('\naverage money ',TotalStudent,' students can make: ',Total/TotalStudent)
    result = []   
    result.append(Total);result.append(Total/TotalStudent);result.append(Vaccine1Num);result.append(Vaccine2Num);result.append(Vaccine3Num)
    result.append(Game1Num/times);result.append(Game2Num/times)
    return result
#repeat findAvgProfit num times
def Repeat(num):
    Total = 0; average = 0; vaccine1 = 0; vaccine2 = 0; vaccine3 = 0; Game1 = 0; Game2 = 0
    result = []
    for i in range(num):
        l = findAvgProfit()
        length = len(l)
        for j in range(length):
            if j == 0:
                Total += l[j] 
            elif j == 1:
                average += l[j]
            elif j == 2:
                vaccine1 += l[j] 
            elif j == 3:
                vaccine2 += l[j]
            elif j == 4:
                vaccine3 += l[j] 
            elif j == 5:
                Game1 += l[j] 
            elif j == 6:    
                Game2 += l[j] 
    Total /= num; average /= num; vaccine1 /= num; vaccine2 /= num; vaccine3 /= num; Game1 /= num; Game2 /= num
    result.append(Total);result.append(average);result.append(vaccine1);result.append(vaccine2);result.append(vaccine3);result.append(Game1);result.append(Game2)
    return result
#test uniform distribution
def testRandom(times):
    n = 0
    for i in range(times):    
        n = random.random()    
    #print('average over ',times,' times is ', n)
    return n

def printResult():
    l = Repeat(1000)
    length = len(l)
    s = ''
    print('Total ',' average ',' vaccine1 ',' vaccine2 ',' vaccine3 ',' Game1 win probability ','Game2 win probability')
    for i in range(length):    
        s += f'{l[i]:.2f}'+'\t'
    print (s)

#write to a data.csv
def writeCSV(lines):
    filename = 'D:/document/college/UWB/2021 Spring/STMATH 381 Discrete Math Modeling/hw/Project 3/COVID.csv'
    # Open the file in write mode and store the content in file_object
    with open(filename, 'w',newline='') as file_object:
        writer = csv.writer(file_object)
        #writer.writerow(['x','y'])
        writer.writerow(['Total','average','vaccine1 ','vaccine2','vaccine3','Game1','Game2'])
        for i in range(lines):
            l = Repeat(1000)
            writer.writerow([l[0],l[1],l[2],l[3],l[4],l[5],l[6]])            
            #writer.writerow([findPi(10000,False,10),findPi(10000,False,10),findPi(10000,False,10),findPi(10000,False,10),findPi(10000,False,10)])
            #writer.writerow([testRandom(lines)])

#find standard deviation and arithmetic mean of average money 600 student can make
def findData(num):
    result = []    
    for i in range(num):
        l = Repeat(1000)
        result.append(l[1])        
    print ('mean: ',mean(result))
    print('stdev: ',stdev(result))    

#writeCSV(100)
for i in range(10):
    print(i,': ')
    findData(100)