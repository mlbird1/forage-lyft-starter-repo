import random

fl = random.randint(0,1)
fr = random.randint(0,1)
rl = random.randint(0,1)
rr = random.randint(0,1)


def check_Ctyres(FL, FR, RR, RL):
   
    if FL >= 0.9 or FR >= 0.9 or RL >= 0.9 or RR >= 0.9:
        print("Tyres needs servicing")
    else:
        print("You're front-left tyre value is " ,FL, ", you're Front-right tyre value is " ,FR, ", you're rear-left tyre value is " ,RL, ", you're rear-right tyre value is " ,RR, ". This is for the Carrigan tyre.")


def check_Otyres(FL, FR, RR, RL):
    
    if FL + FR + RR + RL >= 3:
        print("Tyres needs servicing")
    else:
        print("You're front-left tyre value is " ,FL, ", you're Front-right tyre value is " ,FR, ", you're rear-left tyre value is " ,RL, ", you're rear-right tyre value is " ,RR, ". This is for the Octoprime tyre.")


check_Ctyres(fr,fl,rr,rl)
check_Otyres(fr,fr,rr,rl)
