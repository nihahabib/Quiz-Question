print("Niha Habib")
print("18B-032-Cs")
print("Quiz Of Question")
def room_reservation():
    Left = 0
    print("Thankyou for choosing our hotel Sir , Please follow through the following procedure for reservation Details")
    print("\n")
    Number_of_persons= int(input("How many persons with you have,Sir..?: "))
    room_type= (input("Enter the Room,Single or Deluxe..?: "))
    if room_type== "Single" or room_type == "single" or room_type == "SINGLE":
        print("You can Book ",Number_of_persons," Single rooms")#if customer chooses single room then total number of rooms would be equal to total numberOfPersons
    elif   Number_of_persons%2 == 0:
           Number = (Number_of_persons/2)
           x= int(Number)
           print("You would have ",int(Number)," Deluxe rooms for your stay") 
    elif   Number_of_persons%2 != 0:
           Number = (Number_of_persons/2)
           x= int(Number)
           print("You would have ",int(Number)," Deluxe rooms and 1 single room for your stay")
    else:
        print("exit")
    if room_type == "Single" or room_type == "single" or room_type == "SINGLE":
        Ball = 0 #Initialize the variables first with 0 so in case the user doesn't want to use a particular sevice , then 0 would be added in the bill
        Bell = 0
        Bull = 0
        Days= int(input("Enter the period,how many days would you stay,Sir...?: "))
        Iron=(input("Would you like to give your clothes for Iron..?: "))
        if Iron== "Yes"or Iron == "yes" or Iron == "YES":
             print("Iron charges for 1 day is: 100 per cloth")            
             Irio= int(input("How many cloths you have given for iron in one day..?: "))
             Iries=int(input("For How many days you have given your cloths for Iron...?: "))
             Bull= Irio*Iries*100
        else:
             print("As you Wish Sir..")
        wash=input("Would you like to give your clothes for Laundary..?: ")
        if wash == "Yes" or wash == "yes" or wash == "YES":
            print("Wash charges for 1 day is: 300 per cloth") 
            washio= int(input("How many cloths you have given for Laundry in one day..?: "))
            washies= int(input("For How many days you have given your cloths for Laundry...?: "))
            Ball= washio*washies*300
        else:
            print("Ok,Sir") 
        Taxi= (input("Sir would you like to use our service of Taxi..?: "))
        if Taxi == "Yes"or Taxi== "yes" or Taxi== "YES":
            print("Taxi Charges for 1km will be: 40/km ")#Taxi charges for 1km is 40   
            taxio= int(input("How many kilo meters(Km) you have travelled through our service of taxi in one day..?: "))
            taxies= int(input("For how many days you have used our service..?: "))
            Bell= taxio*taxies*40
        else :
            print("Ok")
        bill1 = 1500*Number_of_persons*Days #total room charges of "*" number of people for "*" days
        Bill= (Bull+Ball+Bell)#total charges for the services used by the customer
        bill2 = Bill+bill1 #the total bill (services + all the rooms)
        print("\n")
        print("Following are the charges of the room category you choose")
        print("\n")
        print("Plese Verify before leaving and confirm the charges")
        print("Single Room(1 Person)= 1500")
        print("Iron per cloths = 100")
        print("Wash(per cloth) takes 1day= 300")
        print("taxi(per km) = 40")
        print("\n")
        print("\t\tHere Is your Bill: ",bill2,"PKR")
    elif room_type == "Deluxe" or room_type == "DELUXE" or room_type == "deluxe":
        Ball = 0 
        Bell = 0
        Bull = 0
        Days= int(input("Enter the period,how many days would you stay,Sir...?: "))
        Iron=(input("Would you like to give your clothes for Iron..?: "))
        if Iron== "Yes"or Iron == "yes" or Iron == "YES":
             print("Iron charges for 1 day is: 100 per cloth")
             Irio= int(input("How many cloths you have given for iron in one day..?: "))
             Iries=int(input("For How many days you have given your cloths for Iron...?: "))
             Bull= Irio*Iries*100
        else:
             print("As you wish Sir..")
        wash=input("Would you like to give your clothes for laundary..?: ")
        if wash == "Yes" or wash == "yes" or wash == "YES":
            print("Wash charges for 1 day is: 300 per cloth")
            washio= int(input("How many cloths you have given for laundry in day..?: "))
            washies= int(input("For How many days you have given your cloths for Laundry...?: "))
            Ball= washio*washies*300
        else:
            print("Ok,Sir") 
        Taxi= (input("Would you like to use our service of Taxi..?: "))
        if Taxi == "Yes"or Taxi== "yes" or Taxi== "YES":
            print("Taxi Charges for 1km will be: 40")
            taxio= int(input("How many kilo meters(Km) you have travelled through our service of taxi in one day..?: "))
            taxies= int(input("For how many days you have used our service..?: "))
            Bell= taxio*taxies*40
        else :
            print("Ok")        
        bill1 =2500*x*Days #total room charges of "*" number of people for "*" days
        Bill= (Bull+Ball+Bell)#total charges for the services used by the customer
        bill2 = Bill+bill1 #the total bill (services + all the rooms)
        print("\n")
        print("Following are the charges of the room category you choose")
        print("\n")
        print("Plese Verify before leaving and confirm the charges")
        print("Deluxe Room(2 Persons)= 2500")
        print("Iron per cloths = 100")
        print("Wash(per cloth) takes 1day= 300")
        print("taxi(per km) = 40")
        print("\n")
        print("\t\tHere Is your Bill: ",bill2,"PKR")


    print("\tAllah Hafiz Sir..,Enjoy and come back soon..")
