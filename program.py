import sys

seats2pm = ["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9",
            "B0","B1","B2","B3","B4","B5","B6","B7","B8","B9",
            "C0","C1","C2","C3","C4","C5","C6","C7","C8","C9",
            "D0","D1","D2","D3","D4","D5","D6","D7","D8","D9",
            "E0","E1","E2","E3","E4","E5","E6","E7","E8","E9",
            "F0","F1","F2","F3","F4","F5","F6","F7","F8","F9",
            "G0","G1","G2","G3","G4","G5","G6","G7","G8","G9",
            "H0","H1","H2","H3","H4","H5","H6","H7","H8","H9"]
seats5pm = ["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9",
            "B0","B1","B2","B3","B4","B5","B6","B7","B8","B9",
            "C0","C1","C2","C3","C4","C5","C6","C7","C8","C9",
            "D0","D1","D2","D3","D4","D5","D6","D7","D8","D9",
            "E0","E1","E2","E3","E4","E5","E6","E7","E8","E9",
            "F0","F1","F2","F3","F4","F5","F6","F7","F8","F9",
            "G0","G1","G2","G3","G4","G5","G6","G7","G8","G9",
            "H0","H1","H2","H3","H4","H5","H6","H7","H8","H9"]
seats8pm = ["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9",
            "B0","B1","B2","B3","B4","B5","B6","B7","B8","B9",
            "C0","C1","C2","C3","C4","C5","C6","C7","C8","C9",
            "D0","D1","D2","D3","D4","D5","D6","D7","D8","D9",
            "E0","E1","E2","E3","E4","E5","E6","E7","E8","E9",
            "F0","F1","F2","F3","F4","F5","F6","F7","F8","F9",
            "G0","G1","G2","G3","G4","G5","G6","G7","G8","G9",
            "H0","H1","H2","H3","H4","H5","H6","H7","H8","H9"]
               #All the seats for each show numbered for conveneince

booked2index = []    #index of all the booked seats
booked5index = []
booked8index = []
    
def seats2():
    print("2pm seats:")
    count = 1
    for i in seats2pm:
        print(i, end=" ")
        if(count == 10 or count ==20 or count == 30 or count ==40 or count == 50 or count ==60 or count ==70 or count ==80):
            print(" ")       #to separate rows to simulate the seating pattern of a cinema 
        count = count +1
        
def seats5():
    print("5pm seats:")
    count = 1
    for i in seats5pm:
        print(i, end=" ")
        if(count == 10 or count ==20 or count == 30 or count ==40 or count == 50 or count ==60 or count ==70 or count ==80):
            print(" ")       #to separate rows to simulate the seating pattern of a cinema 
        count = count +1
    
def seats8():
    print("8pm seats:")
    count = 1
    for i in seats8pm:
        print(i, end=" ")
        if(count == 10 or count ==20 or count == 30 or count ==40 or count == 50 or count ==60 or count ==70 or count ==80):
            print(" ")       #to separate rows to simulate the seating pattern of a cinema 
        count = count +1
        
        
def report():
    
    print()
    print("An 'x' replacing the seat number represents a booked seat")
    print()
    seats2()
    print()
    sold = 0
    for i in seats2pm:
        if i == "x":
            sold = sold+1
            
    print("Total number of sold seats for 2pm slot:", sold)
    print("Total number of empty seats for 2pm slot:", 80 -sold)
    
    print()
    seats5()
    print()
    sold = 0
    for i in seats5pm:
        if i == "x":
            sold = sold+1
            
    print("Total number of sold seats for 5pm slot:", sold)
    print("Total number of empty seats for 2pm slot:", 80 -sold)
        
    print()
    seats8()
    print()
    sold = 0
    for i in seats8pm:
        if i == "x":
            sold = sold+1
            
    print("Total number of sold seats for 8pm slot:", sold)
    print("Total number of empty seats for 2pm slot:", 80 -sold)
    
    opt = input("Enter '0' to return to main menu: ")
    if opt == "0":
        print()
        menu()
    
def allbookings():

    seats2()
    seats5()
    seats8()

    
    
def book():
    print("Please select a timeslot:")
    print()
    print("0. 2pm")
    print("1. 5pm")
    print("2. 8pm")
    time = input()
    
    if time == "0": 
        seats2() #display all available seats for timeslot
        
        seat = input("Enter a seat number: ") #pick a seat
        seat = seat.upper()
        if seat in seats2pm:
            index = seats2pm.index(seat)
            seats2pm[index] = "x"
            booked2index.append(seat) #add the seat number to list
            booked2index.append(index) #add the index of the booked seat to a list
            print("Seat booked")
        else:
            print("Seat is unavailable, please enter a valid seat number")
        inp = input("Would you like to book another seat? (Y/N) ")
        if inp.lower() == "y":
            book()
        else:
            print()
            menu()
           
        
        
    if time == "1":
        seats5() #display all available seats for timeslot
        
        seat = input("Enter a seat number: ") #pick a seat
        seat = seat.upper()
        if seat in seats5pm:
            index = seats5pm.index(seat)
            seats5pm[index] = "x"
            booked5index.append(seat) #add the seat number to list
            booked5index.append(index) #add the index of the booked seat to a list
            print("Seat booked")
        else:
            print("Seat is unavailable, please enter a valid seat number")
        inp = input("Would you like to book another seat? (Y/N) ")
        if inp.lower() == "y":
            book()
        else:
            print()
            menu()

    if time == "2":
        seats8() #display all available seats for timeslot
        
        seat = input("Enter a seat number: ") #pick a seat
        seat = seat.upper()
        if seat in seats8pm:
            index = seats8pm.index(seat)
            seats8pm[index] = "x"
            booked8index.append(seat) #add the seat number to list
            booked8index.append(index) #add the index of the booked seat to a list
            print("Seat booked")
        else:
            print("Seat is unavailable, please enter a valid seat number")
        inp = input("Would you like to book another seat? (Y/N) ")
        if inp.lower() == "y":
            book()
        else:
            print()
            menu()
    
    
def cancel():
    print("Please select your show's timeslot: ")
    print("0. 2pm")
    print("1. 5pm")
    print("2. 8pm")
    time = input()
    if time == "0":
        print("An 'x' represents a booked seat")
        seats2()
        
        seat = input("Please enter your seat number: ")
        seat = seat.upper()
        if seat in booked2index:
            seatnum = booked2index.index(seat)
            seatindex = booked2index[seatnum+1]
            
            seats2pm[seatindex] = seat 
            print("Seat booking canceled")
            
            print()
            menu()
        else:
            print("Seat not booked or invalid seat number entered.")
            print()
            menu()
            
    
    if time == "1":
        print("An 'x' represents a booked seat")
        seats5()
        
        seat = input("Please enter your seat number: ")
        seat = seat.upper()
        if seat in booked5index:
            seatnum = booked5index.index(seat)
            seatindex = booked5index[seatnum+1]
            
            seats5pm[seatindex] = seat 
            print("Seat booking canceled")
            
            print()
            menu()
        else:
            print("Seat not booked or invalid seat number entered.")
            print()
            menu()
        
    if time == "2":
        print("An 'x' represents a booked seat")
        seats8()
        
        seat = input("Please enter your seat number: ")
        seat = seat.upper()
        if seat in booked8index:
            seatnum = booked8index.index(seat)
            seatindex = booked8index[seatnum+1]
            
            seats8pm[seatindex] = seat 
            print("Seat booking canceled")
            
            print()
            menu()
        else:
            print("Seat not booked or invalid seat number entered.")
            print()
            menu()    
    
    
    
    
    
def menu():
    print("Welcome, Please select an option:")
    print("0. Make a booking")
    print("1. Cancel a booking")
    print("2. Report")
    opt = input()
    print()

    if opt == "0":
        book()
    if opt == "1":
        cancel()
    if opt == "2":
        report()

    
    
    
    