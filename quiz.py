# Our quiz!


score = 0
name = ""


def quiz():
    global score
    global name

    name =input("Enter your name:")

    q1()
    q2()
    q3()
    q4()
    q5()
    q6() 
    



def q1():
    global score
    global name

    print("Here is question 1", name)
    

    print("what is the capital of the USA")
    print("A. Washington DC")
    print("B. New York")
    print("C. Houstan")
    answer = input ("select an option ")

    if answer.upper() == "A":
        score = score + 100
    elif answer.upper() == "B":
        score = score + 50
    elif answer.upper() == "C":
        score = score + 25

    print(score)

def q2():
    global score
    global name

    print("Here is question 2", name)

    print ("what is the capital of England")
    print ("A. Leeds")
    print ("B. York")
    print ("C. London")
    print ("D. Washington")
    answer = input ("select an option ")

    if answer.upper() == "A":
        score = score + 50
    elif answer.upper() == "B":
        score = score + 0
    elif answer.upper() == "C":
        score = score + 100
    elif answer.upper() == "D":
        score = score + 25

    print (score)

def q3():
    global score
    global name

    print("Here is question 3", name)

    print ("what is the capital of Japan")
    print ("A.Toyko")
    print ("B.Yokohama") 
    print ("C.Kanagawa")
    print ("D.Osaka")
    answer = input ("select an option ")

    if answer.upper() == "A":
        score = score + 100
    elif answer.upper() == "B":
        score = score + 50
    elif answer.upper() == "C":
        score = score + 0
    elif answer.upper() == "D":
        score = score + 25

    print (score)

def q4():
    global score
    global name

    print("Here is question 4", name)

    print ("what is the capital of China")
    print ("A. Shanghai")
    print ("B. Hong Kong") 
    print ("C. Tianjin")
    print ("D. Beijing")
    answer = input ("select an option ")

    if answer.upper() == "A":
        score = score + 25
    elif answer.upper() == "B":
        score = score + 50
    elif answer.upper() == "C":
        score = score + 0
    elif answer.upper() == "D":
        score = score + 100

    print (score)

def q5():
    global score
    global name

    print("Here is question 5", name)

    print ("what is the capital of Spain")
    print ("A. Barcelona")
    print ("B. Madrid") 
    print ("C. Granada")
    print ("D. Bilboa")
    answer = input ("select an option ")

    if answer.upper() == "A":
        score = score + 50
    elif answer.upper() == "B":
        score = score + 100
    elif answer.upper() == "C":
        score = score + 25
    elif answer.upper() == "D":
        score = score + 0

    print (score)

def q6():
    global score
    global name

    print("Here is question 6", name)

    print ("what is the capital of Frnace")
    print ("A. Paris")
    print ("B. Lyon") 
    print ("C.Nantes")
    print ("D. Lille")
    answer = input ("select an option ")

    if answer.upper() == "A":
        score = score + 100
    elif answer.upper() == "B":
        score = score + 50
    elif answer.upper() == "C":
        score = score + 25
    elif answer.upper() == "D":
        score = score + 0
    
    
     

    

    

    





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
