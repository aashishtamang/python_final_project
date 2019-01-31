import random
print("------------------------Likhit Parikshya Game------------------------")
life = 3
score = 0

questions = { 1 : {"question" : "What is the work of Dynamo in Vehicle?","answer" : "To charge the batter.","options" : {"A" : "To connect the engine and gear." , "B" : "To start the engine." , "C" : "To charge the battery." , "D" : "None of the above."}},
            2 : {"question" : "When do you have to pay vehicle tax according to Nepalese Transport Act?","answer" : "Within Ashar Month.","options" : {"A" : "Within Ashar Month.","B" : "Within Shrawan Month." , "C" : "Within Chaitra Month.", "D" : "Within Baishak Month."}},
            3 : {"question" : "If there is no lane marked on the road, you should drive:","answer" : "To the left of the road.","options" : {"A" : "Along the middle of the road.","B" : "To the left of the road." , "C" : "to the right of the road.", "D" : "Shouldnt drive"}},
            4 : {"question" : "What can happen if pillion passenger on bike sit keeping gap from rider?","answer" : "Bike can crash due to imbalance of load.","options" : {"A" : "Bike can crash due to imbalance of load.","B" : "Bike can slow down." , "C" : "Bike can move smoothly.", "D" : "All is futile - we may ride as we wish."}},
            5 : {"question" : "You are driving bike with a child in the front of you, what issues should you be aware of?","answer" : "All of the above.","options" : {"A" : "Your child may twist accelerator and can cause accident.","B" : "Your child may sway handle." , "C" : "Your child may stretch out legs and collide with another vehicle.", "D" : "All of the above."}},
            6 : {"question" : "What does flashing red light mean in traffic signal?","answer" : "Stop Completely and Proceed with caution." , "options" : {"A" : "Continue in the same speed with horn and flashlight.","B" : "Stop Completely and Proceed with caution." , "C" : "Wait until green light signal.", "D" : "Assume that none are coming and proceed in the same speed."}},
            7 : {"question" : "What is blue book or what information does bluebook contain ?","answer" : "A & B.", "options" :{ "A" : "A small book containing vehicle ownership details like name , surname, race and address etc.","B" : "A small book containing vehicle details i.e. Model, Color, Engine no. etc." , "C" : "A & B.", "D" : "A small book containing driving tips for new drivers."}},
            8 : {"question" : "What distance is called short distance journey in Nepal?","answer" : "25 KM to 100 KM Journey." , "options" : {"A" : "25 KM to 80 KM Journey.","B" : "25 KM to 50 KM Journey." , "C" : "25 KM to 100 KM Journey.", "D" : "25 KM to 200 KM Journey."}},
            9 : {"question" : "You have to renew your license after: ","answer" : "5 Years","options" : {"A" : "3 Years.","B" : "10 Years." , "C" : "20 Years", "D" : "5 Years"}},
            10 : {"question" : "What type of vehicle are prone to have more fatalities during accident ?","answer" : "Two wheelers","options" : {"A" : "Two wheelers.","B" : "Car and Light vehicles." , "C" : "Trucks.", "D" : "Busses."}}
            }

while life > 0:
    acb = random.choice(list(questions))
    print("\n",questions[acb]["question"],"\n",questions[acb]["options"])
    choice = input("Enter your choice: ")
    choice = choice.upper()

    if questions[acb]["answer"] == questions[acb]["options"][choice]:
        print("Correct!")
        score = score + 1
        print("Your score is: ", score)
    else:
        print("Incorrect! The correct answer is ", questions[acb]["answer"])
        life = life - 1
        print("Your life is: ", life)
        
print("Your final score is: ",score)

