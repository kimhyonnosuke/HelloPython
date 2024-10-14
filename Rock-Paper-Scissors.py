import random

def RockPaperScissors():

    a = random.randint(0,2)
    b = random.randint(0,2)

    if a == 0 :
        resulta = 'グー'
    
    if b == 0 :
        resultb = 'グー'
    
    if a == 1:
        resulta = 'チョキ'

    if b == 1:
        resultb = 'チョキ'

    if a == 2:
        resulta = 'パー'

    if b == 2:
        resultb = 'パー'        

    if (a == 0 and b == 0) or (a == 1 and b == 1) or (a == 2 and b == 2):
         result = "引き分け"
    
    if (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
        result = "Aの勝ち"

    if (b == 0 and a == 1) or (b == 1 and a == 2) or (b == 2 and a == 0):
        result = "Bの勝ち"
    
    print ("Aの手 : " + resulta + "v.s. Bの手 :" + resultb + "->" + result) 


RockPaperScissors()
