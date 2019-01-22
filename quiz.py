print("------------------------Likhit Parikshya Game------------------------")
life = 3
score = 0

print("What is the work of Dynamo in Vehicle?")
print("A.To connect the engine and gear.\nB.To start the engine.\nC.To charge the battery.\nD.None of the above.\n")
choice = input("Enter your choice: ")

if choice.upper() == 'C':
    score = score + 1
    print("\nCorrect! Your score is",score,"\n")
else:
    life = life - 1
    print("\nIncorrect! Your life is",life,"\n")
    print("The correct answer is: C.To charge the battery.")

print("When do you have to pay vehicle tax according to Nepalese Transport Act ?")
print("A.Within Ashar Month.\nB.Within Shrawan Month.\nC.Within Chaitra Month.\nD.Within Baishak Month.\n")
choice = input("Enter your choice: ")
if choice.upper() == 'A':
    score = score + 1
    print("\nCorrect! Your score is",score,"\n")
else:
    life = life - 1
    print("\nIncorrect! Your life is",life,"\n")
    print("The correct answer is: A.Within Ashar Month.\n")
    

print("If there is no lane marked on the road, you should drive ;")
print("A.Along the middle of the road.\nB.To the left of the road.\nC.to the right of the road.\nD.to the right of the road.\n")
choice = input("Enter your choice: ")
if choice.upper() == 'B':
    score = score + 1
    print("\nCorrect! Your score is",score,"\n")
else:
    life = life - 1
    print("\nIncorrect! Your life is",life,"\n")
    print("The correct answer is: B.To the left of the road.\n")
    

if life <= 0:
    print("Game Over! Your score is: ",score)
else:
    print("What can happen if pillion passenger on bike sit keeping gap from rider ?")
    print("A.Bike can crash due to imbalance of load.\nB.Bike can slow down.\nC.Bike can move smoothly.\nD.All is futile - we may ride as we wish.\n")
    choice = input("Enter your choice: ")
    if choice.upper() == 'A':
        score = score + 1
        print("\nCorrect! Your score is",score,"\n")
    else:
        life = life - 1
        print("\nIncorrect! Your life is",life,"\n")
        print("The correct answer is: A.Bike can crash due to imbalance of load.\n")

    if life <= 0:
        print("Game Over! Your score is: ",score)
    else:
        print("You are driving bike with a child in the front of you, what issues should you be aware of?")
        print("A.Your child may twist accelerator and can cause accident.\nB.Your child may sway handle.\nC.Your child may stretch out legs and collide with another vehicle.\nD.All of the above.\n")
        choice = input("Enter your choice: ")
        if choice.upper() == 'D':
            score = score + 1
            print("\nCorrect! Your score is",score,"\n")
        else:
            life = life - 1
            print("\nIncorrect! Your life is",life,"\n")
            print("The correct answer is: D.All of the above.\n")

        if life <= 0:
            print("Game Over! Your score is: ",score)

        else:
            print("What does flashing red light mean in traffic signal?")
            print("A.Continue in the same speed with horn and flashlight.\nB.Stop Completely and Proceed with caution.\nC.Wait until green light signal.\nD.Assume that none are coming and proceed in the same speed.\n")
            choice = input("Enter your choice: ")
            if choice.upper() == 'B':
                score = score + 1
                print("\nCorrect! Your score is",score,"\n")
            else:
                life = life - 1
                print("\nIncorrect! Your life is",life,"\n")
                print("The correct answer is: B.Stop Completely and Proceed with caution.\n")

            if life <= 0:
                print("Game Over! Your score is: ",score)
            else:
                print("What is blue book or what information does bluebook contain ?")
                print("A.A small book containing vehicle ownership details like name , surname, race and address etc.\nB.A small book containing vehicle details i.e. Model, Color, Engine no. etc.\nC.A & B.\nD.A small book containing driving tips for new drivers.\n")
                choice = input("Enter your choice: ")
                if choice.upper() == 'C':
                    score = score + 1
                    print("\nCorrect! Your score is",score,"\n")
                else:
                    life = life - 1
                    print("\nIncorrect! Your life is",life,"\n")
                    print("The correct answer is: C.A & B.\n")

                if life <= 0:
                    print("Game Over! Your score is: ",score)
                else:
                    print("What distance is called short distance journey in Nepal?")
                    print("A.25 KM to 80 KM Journey.\nB.25 KM to 50 KM Journey.\nC.25 KM to 100 KM Journey.\nD.25 KM to 200 KM Journey.\n")
                    choice = input("Enter your choice: ")
                    if choice.upper() == 'C':
                        score = score + 1
                        print("\nCorrect! Your score is",score,"\n")
                    else:
                        life = life - 1
                        print("\nIncorrect! Your life is",life,"\n")
                        print("The correct answer is: C.25 KM to 100 KM Journey.\n")

                    if life <= 0:
                        print("Game Over! Your score is: ",score)
                    else:
                        print("What are different parts on bike to control ?")
                        print("A.Hand brake, Foot brake, Clutch, Accelerator.\nB.Hand brake, Handle, Footbrake, Clutch, Accelerator.\nC.Hand brake, foot brake , Gear, Handle.\nD.Hand brake, Foot brake, Gear, Accelerator.\n")
                        choice = input("Enter your choice: ")
                        if choice.upper() == 'A':
                            score = score + 1
                            print("\nCorrect! Your score is",score,"\n")
                        else:
                            life = life - 1
                            print("\nIncorrect! Your life is",life,"\n")
                            print("The correct answer is: A.Hand brake, Foot brake, Clutch, Accelerator.\n")

                        if life <= 0:
                            print("Game Over! Your score is: ",score)
                        else:        
                            print("What can happen if you increase speed of your two-wheelers just after you passed through muddy road ?")
                            print("A.Bike/ Scooty becomes smooth due to mud on wheels.\nB.Bike/ Scooty can slip away due to stuck mud on the wheels.\nC.Bike/ Scooty's engine and wheels get stuck and needs immediate washing.\nD.Nothing happens , we need to be careful only on muddy roads.\n")
                            choice = input("Enter your choice: ")
                            if choice.upper() == 'B':
                                score = score + 1
                                print("\nCorrect! Your score is",score,"\n")
                            else:
                                life = life - 1
                                print("\nIncorrect! Your life is",life,"\n")
                                print("The correct answer is: B.Bike/ Scooty can slip away due to stuck mud on the wheels.")
                            
                            if life <= 0:
                                print("Game Over! Your score is: ",score)
                            else:                           
                                print("What type of braking can cause bike to somersault ?")
                                print("A.Handbrake only in high speed.\nB.Footbrake only in high speed.\nC.Both Brakes in hight speed.\nD.All of the above.\n")
                                choice = input("Enter your choice: ")
                                if choice.upper() == 'A':
                                    score = score + 1
                                    print("\nCorrect! Your score is",score,"\n")
                                else:
                                    life = life - 1
                                    print("\nIncorrect! Your life is",life,"\n")
                                    print("The correct answer is: A.Handbrake only in high speed.")
                                
                                if life <= 0:
                                    print("Game Over! Your score is: ",score)
                                else:
                                    print("You have to renew your license after: ")
                                    print("A.3 Years.\nB.10 Years.\nC.20 Years\nD.5 Years\n")
                                    choice = input("Enter your choice: ")
                                    if choice.upper() == 'D':
                                        score = score + 1
                                        print("\nCorrect! Your score is",score,"\n")
                                    else:
                                        life = life - 1
                                        print("\nIncorrect! Your life is",life,"\n")
                                        print("The correct answer is: D.5 Years")
                                    
                                    if life <= 0:
                                        print("Game Over! Your score is: ",score)
                                    else:
                                        print("Why broken lights are avoided in vehicles?")
                                        print("A.Because Traffic police will catch you and fine you.\nB.Because You vehicle does not look nice and new\nC.Because it saves from having collision as it let back drivers know about your driving move.\nD.Because it will damage your battery and engine.\n")
                                        choice = input("Enter your choice: ")
                                        if choice.upper() == 'C':
                                            score = score + 1
                                            print("\nCorrect! Your score is",score,"\n")
                                        else:
                                            life = life - 1
                                            print("\nIncorrect! Your life is",life,"\n")
                                            print("The correct answer is: C.Because it saves from having collision as it let back drivers know about your driving move.")
                                        
                                        if life <= 0:
                                            print("Game Over! Your score is: ",score)
                                        else:
                                            print("What type of vehicle are prone to have more fatalities during accident ?")
                                            print("A.Two wheelers.\nB.Car and Light vehicles.\nC.Trucks.\nD.Busses.\n")
                                            choice = input("Enter your choice: ")
                                            if choice.upper() == 'A':
                                                score = score + 1
                                                print("\nCorrect! Your score is",score,"\n")
                                            else:
                                                life = life - 1
                                                print("\nIncorrect! Your life is",life,"\n")
                                                print("The correct answer is: A.Two wheelers.")

                                            if life <= 0:
                                                print("Game Over! Your score is: ",score)
                                            else:
                                                print("Congratulations! You won the game.")
                                                print("your score is ",score)
                                                print("your life is ",life)
                                                print("Final score is ",score,"+",life,"=",score+life)


                            