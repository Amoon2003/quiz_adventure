# An adventure game

Hp = 20
Cp = 3
rat1 = 6
boss1 = 80

from random import randint

def health_loss(n):
    global Hp, Cp

    Hp = Hp - n
    if Hp  <= 0:
        print("")
        game_over() 

def game_over():

    print("\n"*2) 
    print('GAME OVER!!')
    print('YOU DEAD')

def bossatk(n):
    global boss1

    print("You attack")
    boss1 = boss1 - n
    print("Boss health remaining:", boss1)
    if boss1 <= 0:
        print("You kill it and run for the door")
        escape()
    else:
        boss1_fight
    
        

      


def status():

    print("\n"*5)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("             Hp:", Hp, "                                   Cp:", Cp                                                                                                 )
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")



    


def room1():
    global Hp, Cp

    status()
    

     

    print("you wake up in a dark room")
    print("Do you ?")
    print("")
    print("A. leave the room")
    print("B. stay in the room")
    answer = input("What do you choose ")

    if answer.upper() == 'A':
        print("you leave the room")
        room2()
    elif answer.upper() == 'B':
        print("you take hunger damage")
        room3()

def room2():
    global Hp, Cp

    status()

    print("As you exit the room you see a window")
    print("Do you ?")
    print("")
    print("A. Jump through it")
    print("B. Look through it")
    answer = input("What do you choose ")

    if answer.upper() == 'A':
        print("You jump through the window and...")
        print("you relise its too high but its too late")
        game_over() 
    elif answer.upper() =='B':
        print("You look through the window and see that your in a...")
        print("Tower!!!!!")
        room4()

def room3():
    global Hp, Cp

    hunger = randint(1, 2)

    if hunger == 1:
        print ("you lose 1 Hp") 
        health_loss(hunger)
    elif hunger == 2:
        print ("you lose 2 Hp")
        health_loss(hunger)
    

    

def room4():
    global Hp, Cp

    status()

    print("You turn around and hear a squek")
    print("You then see a giant RAT")
    print("Do you ?")
    print("")
    print("A. Fight it")
    print("B. Run away")
    answer = input("What do you choose ")

    if answer.upper() == 'A':
        fight1()
    elif answer.upper() == 'B':
        print("You try to run but it still attacks")
        print("You loose 2 Hp")
        health_loss(2) 
        fight1()

    

def fight1():
    global rat1
    global Hp, Cp

    ratk = randint(1, 2)

    if ratk == 1:
        print ("The rat attacks") 
        print ("You loose:",  ratk, "Hp")
        health_loss(ratk) 
        attack1()

    elif ratk == 2:
        print ("The rat attacks")
        print ("You loose 2 Hp")
        health_loss(ratk) 
        attack1()

    

    print("Hp remaining:", Hp)

def attack1():
    global Hp
    global rat1
    global Cp

    atk = randint(1, Cp)

    if atk <= Cp:
        print("You attack it")
        print("It looses:", atk)
        rat1 = rat1 - atk
        print(rat1)
        if rat1 <= 0:
            room5()
        else:
              fight1()
            

    

def room5():
    global Hp, Cp

    status()

    print("You kill the rat")
    print("Do you ")
    print("")
    print("A. Eat it")
    print("B. Leave it")
    answer = input("What do you choose ")

    if answer.upper() == 'A':
        print ("You eat the rat and gain 1 Hp")
        Hp = Hp + 1
        room6()


    elif answer.upper() == 'B':
        print("You carry on")
        room6()

def room6():
    global Hp, Cp

    status()

    print("You go down the corridor and encounter")
    print("a door to each side of you")
    print("Do you ?")
    print("")
    print("A. go left")
    print("B. go right")
    print("C. Carry on")
    answer = input("What do you choose ")

    if answer.upper() == 'A':
        print("You go left")
        room7()
    elif answer.upper() == 'B':
        print("You go right")
        room7()
    elif answer.upper() == 'C':
        print ("You carry on")
        room8() 

def room7():

    status()
    

    print("You walk in the room")
    print("Do you ?")
    print("")
    print("A. Look around")
    print("B. Carry on up the corridor")
    answer = input("What do you choose ")

    if  answer.upper() == 'A':
        print("You start looking and Then...")
        find()
    elif answer.upper() == 'B':
        print ("You carry on up the cotrridor")
        room8()

def find():
    global Cp

    status() 

    f = randint(1, 2)

    if f == 1:
        print("You found a knife")
        print("and carry on up the corridor")
        Cp = Cp + 5
        room8()

    elif f == 2: 
        print("You found sledge hammer!")
        print("and carry on up the corridor")
        Cp = Cp + 20
        room8() 

def room8():
    global Hp, Cp
    status()

    print("You come to a door see a bottle with drink this on it")
    print("Do you ?")
    print("")
    print("A. Drink it and go through the door")
    print("B. Leave it and go through the door")
    answer = input("What do you choose ")

    if  answer.upper() == 'A':
        print("You drink and feel stronger you gain 3 Cp and 10 HP")
        Hp = Hp + 10
        Cp = Cp + 3
        boss1()
    elif  answer.upper() == 'B':
        print("You leave it and go through the door with a feeling of regret")
        boss1()

def boss1():
    global boss1

    status()

    print("You enter the room and see a statue and a door at the other side")
    print("You run for it but then")
    print("\n"*3)
    print("The statue turns into a gient monster")
    print ("Your only chance is to fight so you ready your self and take your first swing")
    print("but miss then it attacks back")
    boss1_fight

def boss1_fight():
    global Cp, Hp, boss1

    status()
    dodge = randint(1, 2)
    yatk = randint(5, Cp)
    batk = randint(5, 10)

    print("What do you do")
    print("A. dodge")
    print("B. Attack")

    if answer.upper() == 'A':
        if dodge == 1:
             print("it attacks You to dodge but it gets you")
             health_loss(batk) 
             print("Hp remaining:", Hp)
             boss1_fight
        elif dodge == 2:
                   print("You dodge it")
                   boss1_fight() 


    elif answer.upper() == 'B':
                   
                   bossatk(yatk)
                   boss_attack()

def boss_attack():
    global Hp

    batk = randint(5, 10)

    print("it attacks")
    print("You lose:", yatk)
    health_loss(yatk)
    boss1_fight() 
    
    



                   

            
                   

    
    
    

    

    

    
        


    

    
    
        
    
    
    
    
    
        
        

    
        
    

    
        

    








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()
