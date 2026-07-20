class HotelManagement:

    def __init__(self):
        
        self.roomDict = {
            101 : None,
            102 : None,
            103 : None,
            104 : None,
            201 : None,
            202 : None,
            203 : None,
            204 : None,
            301 : None,
            302 : None,
            303 : None,
            304 : None
        }
        self.action = None

        while self.action != 15:

            self.showMenu()

            if self.action == 1:

                self.bookRoom()

            elif self.action == 2:

                self.cancelBooking()

            elif self.action == 3:

                self.showAvailableRooms()
            
            elif self.action == 4:

                self.displayCustomerDetails()

            elif self.action == 5:

                self.bill()

            elif self.action == 6:

                self.differentRoomTypes()

            elif self.action == 7:

                self.checkInDate()

            elif self.action == 8:

                self.checkOutDate()

            elif self.action == 9:

                self.searchCustomer()

            elif self.action == 10:

                self.displayAllBookings()

            elif self.action == 11:

                self.foodCharges()

            elif self.action == 12:

                self.otherServices()

            elif self.action == 13:

                self.saveDataToFile()

            elif self.action == 14:

                self.loadFromFile()

            elif self.action == 15:

                self.terminate()
    
    def showMenu(self):

        print('''
            ========== Hotel Management ==========
              
            1. Book Room
            2. Cancel Booking
            3. Check Available Rooms
            4. Display Customer Details
            5. Generate Bill
            6. Different Room Types
            7. Check-In Date
            8. Check-Out Date
            9. Search Customer
            10. Display All Bookings
            11. Add Food Charges
            12. Add Extra Services
            13. Save Data
            14. Load Data
            15. Exit
              
             ====================================== 
              ''')
        
        choice = input("Enter the choice : ").strip()

        if not choice:

            print("---> Please select a option first.")
            return
        
        if not choice.isnumeric():

            print("---> Invalid Option entered.")
            return
        
        self.action = int(choice)

        if not 1 <= self.action <= 15:

            print("---> Option must be between 1 to 15.")
            self.action = None
            return
        
    def bookRoom(self):

        name = input("Enter customer Name : ").strip().title()

        if not name:

            print("---> Please enter the customer name first.")
            return
        
        roomNumber = input("Enter Room number : ").strip()

        if not roomNumber:

            print("---> Please enter the room number first.")
            return
        
        if not roomNumber.isnumeric():

            print("---> Invalid room number entered.")
            return
        
        roomNumber = int(roomNumber)

        if roomNumber not in self.roomDict:

            print("---> Sorry, We don't have any room with this number.")
            return
        
        if self.roomDict[roomNumber] is not None:

            print("---> Sorry, Room already booked.")
            return

        days = input("Enter the number of days : ").strip()

        if not days:

            print("---> Please enter the days you want to stay.")
            return
        
        if not days.isnumeric():

            print("---> Invalid days entered.")
            return
        
        days = int(days)

        if days <= 0:

            print("---> Days must be greater than 0.")
            return

        temp = {
            "name" : name,
            "days" : days,
            "check_In" : None,
            "check_Out" : None,
            "food_charge" : 0,
            "other_services" : 0
        }

        self.roomDict[roomNumber] = temp

        print("---> Room booked successfully.")

    def cancelBooking(self):

        roomNumber = input("Enter Room Number : ").strip()

        if not roomNumber:

            print("---> Please enter the room number first.")
            return
        
        if not roomNumber.isnumeric():

            print("---> Invalid room number entered.")
            return
        
        roomNumber = int(roomNumber)

        if roomNumber not in self.roomDict:

            print("---> Sorry, We don't have any room with this number.")
            return
        
        if self.roomDict[roomNumber] is None:

            print("---> Room is already vacant.")
            return
        
        self.roomDict[roomNumber] = None

        print("---> Booking cancelled successfully.")

    def showAvailableRooms(self):

        print('''
            ------ Available Rooms ------
              ''')
        
        isAvailable = False

        for room in self.roomDict:

            if self.roomDict[room] is None:

                print(f'''
                    {room}''')
                isAvailable = True

        if not isAvailable:

            print('''
                No rooms available.
                  ''')

        print('''
            -----------------------------
              ''')
        
    def displayCustomerDetails(self):

        roomNumber = input("Enter Room Number : ").strip()

        if not roomNumber:

            print("---> Please enter the room number first.")
            return
        
        if not roomNumber.isnumeric():

            print("---> Invalid room number entered.")
            return
        
        roomNumber = int(roomNumber)

        if roomNumber not in self.roomDict:

            print("---> Sorry, We don't have any room with this number.")
            return
        
        if self.roomDict[roomNumber] is None:

            print("---> No customer found.")
            return
        
        print(f'''
            ------ Customer Details ------

            Name           : {self.roomDict[roomNumber]["name"]}
            Room           : {roomNumber}
            Days           : {self.roomDict[roomNumber]["days"]}
            Check-In Date  : {self.roomDict[roomNumber]["check_In"]} 
            Check-Out Date : {self.roomDict[roomNumber]["check_Out"]} 
            Food Charges   : {self.roomDict[roomNumber]["food_charge"]}
            Other Services : {self.roomDict[roomNumber]["other_services"]}

            ------------------------------
              ''')
        
    def bill(self):

        roomNumber = input("Enter Room Number : ").strip()

        if not roomNumber:

            print("---> Please enter the room number first.")
            return
        
        if not roomNumber.isnumeric():

            print("---> Invalid room number entered.")
            return
        
        roomNumber = int(roomNumber)

        if roomNumber not in self.roomDict:

            print("---> Sorry, We don't have any room with this number.")
            return
        
        if self.roomDict[roomNumber] is None:

            print("---> No customer found.")
            return
        
        if roomNumber <= 104:

            rate = 2000

        elif roomNumber <= 204:

            rate = 4000

        else:

            rate = 8000

        roomInfo = self.roomDict[roomNumber]

        print(f'''
            ------ Bill ------

            Customer      : {roomInfo["name"]}
            Room          : {roomNumber}
            Days          : {roomInfo["days"]}
            Rate          : ₹{rate}/day
            Food Charges  : ₹{roomInfo["food_charge"]}
            Other Service : ₹{roomInfo["other_services"]}

            Total         : ₹{(rate * roomInfo["days"]) + roomInfo["food_charge"] + roomInfo["other_services"]}

            ------------------
              ''')
        
    def differentRoomTypes(self):

        print('''
            Room Types
            101 to 104 → Standard → ₹2000/day
              
            201 to 204 → Deluxe → ₹4000/day
              
            301 to 304 → Suite → ₹8000/day
              ''')
        
    def checkInDate(self):

        roomNumber = input("Enter Room Number : ").strip()

        if not roomNumber:

            print("---> Please enter the room number first.")
            return
        
        if not roomNumber.isnumeric():

            print("---> Invalid room number entered.")
            return
        
        roomNumber = int(roomNumber)

        if roomNumber not in self.roomDict:

            print("---> Sorry, We don't have any room with this number.")
            return
        
        if self.roomDict[roomNumber] is None:

            print("---> No customer found.")
            return

        date = input("Enter the Check-In Date (DD-MM-YYYY) : ").strip()

        if not date:

            print("---> Please enter the Date first.")
            return
        
        if len(date) != 10:

            print("---> Invalid format.")
            return
        
        if not (date[:2].isnumeric() and date[2] == "-" and date[3 : 5].isnumeric() and date[5] == "-" and date[6:10].isnumeric()):

            print("---> Invalid format of Date.")
            return
        
        day = int(date[:2])
        month = int(date[3 : 5])
        year = int(date[6:10])

        if not (1 <= day <= 31 and 1 <= month <= 12 and year >= 2026):

            print("---> Invalid Date")
            return
        
        self.roomDict[roomNumber]["check_In"] = date

        print("---> Check In successfull.")

    def checkOutDate(self):

        roomNumber = input("Enter Room Number : ").strip()

        if not roomNumber:

            print("---> Please enter the room number first.")
            return
        
        if not roomNumber.isnumeric():

            print("---> Invalid room number entered.")
            return
        
        roomNumber = int(roomNumber)

        if roomNumber not in self.roomDict:

            print("---> Sorry, We don't have any room with this number.")
            return
        
        if self.roomDict[roomNumber] is None:

            print("---> No customer found.")
            return
        
        if self.roomDict[roomNumber]["check_In"] is None:

            print(f"---> No Check-In found in Room Number {roomNumber}")
            return

        date = input("Enter the Check-Out Date (DD-MM-YYYY) : ").strip()

        if not date:

            print("---> Please enter the Date first.")
            return
        
        if len(date) != 10:

            print("---> Invalid format.")
            return
        
        if not (date[:2].isnumeric() and date[2] == "-" and date[3 : 5].isnumeric() and date[5] == "-" and date[6:10].isnumeric()):

            print("---> Invalid format of Date.")
            return
        
        day = int(date[:2])
        month = int(date[3 : 5])
        year = int(date[6:10])

        if not (1 <= day <= 31 and 1 <= month <= 12 and year >= 2026):

            print("---> Invalid Date")
            return
        
        self.roomDict[roomNumber]["check_Out"] = date

        print("---> Check Out was successfull, Thank you for Visiting.")

    def searchCustomer(self):

        name = input("Enter Customer name : ").strip().title()

        if not name:

            print("---> Please enter the name first.")
            return
        
        isFound = False
        
        for room in self.roomDict:

            roomInfo = self.roomDict[room]

            if roomInfo is not None and roomInfo["name"] == name:
                
                isFound = True

                print(f'''
                Customer Found

                Name        : {roomInfo["name"]}
                Room Number : {room}
                Days        : {roomInfo["days"]}
                Check-In Date  : {roomInfo["check_In"]} 
                Check-Out Date : {roomInfo["check_Out"]}
                  ''')

        if not isFound:

            print("---> No customer found.")

    def displayAllBookings(self):

        print('''
              All Bookings
              ''')
            
        isFound = False

        for room in self.roomDict:

            roomInfo = self.roomDict[room]

            if roomInfo is not None:

                isFound = True

                print(f'''
            Name        : {roomInfo["name"]}
            Room Number : {room}
            Days        : {roomInfo["days"]}
            Check-In Date  : {roomInfo["check_In"]} 
            Check-Out Date : {roomInfo["check_Out"]}
                ''')

        if not isFound:

            print("---> No Bookings Found.")

    def foodCharges(self):

        print('''
            Food Menu
            ================
              
            Breakfast → ₹200

            Lunch → ₹400

            Dinner → ₹500
              ''')
        
        roomNumber = input("Enter your Room Number : ").strip()

        if not roomNumber:

            print("---> Please enter the room number first.")
            return
        
        if not roomNumber.isnumeric():

            print("---> Invalid room number entered.")
            return
        
        roomNumber = int(roomNumber)

        if roomNumber not in self.roomDict:

            print("---> Sorry, We don't have any room with this number.")
            return
        
        if self.roomDict[roomNumber] is None:

            print("---> No customer found.")
            return
        
        choice = input("Enter the meal you want to order : ").strip().title()

        if not choice:

            print("---> No meal was selected.")
            return
        
        roomInfo = self.roomDict[roomNumber]

        if choice == "Breakfast":

            roomInfo["food_charge"] += 200
            print("---> Order successfull.")

        elif choice == "Lunch":

            roomInfo["food_charge"] += 400
            print("---> Order successfull.")

        elif choice == "Dinner":

            roomInfo["food_charge"] += 500
            print("---> Order successfull.")

        else:

            print("---> Please select the meal from the above menu.")

    def otherServices(self):

        print('''
            Other Services We Provide
            =========================
            
            Laundry → ₹200

            Swimming Pool → ₹300

            Spa → ₹450

            Gym → ₹200
              ''')
        
        roomNumber = input("Enter your Room Number : ").strip()

        if not roomNumber:

            print("---> Please enter the room number first.")
            return
        
        if not roomNumber.isnumeric():

            print("---> Invalid room number entered.")
            return
        
        roomNumber = int(roomNumber)

        if roomNumber not in self.roomDict:

            print("---> Sorry, We don't have any room with this number.")
            return
        
        if self.roomDict[roomNumber] is None:

            print("---> No customer found.")
            return
        
        choice = input("Enter the service you want : ").strip().title()

        if not choice:

            print("---> No service was selected.")
            return
        
        roomInfo = self.roomDict[roomNumber]
        
        if choice == "Laundry":

            roomInfo["other_services"] += 200
            print(f"---> Thank you {roomInfo['name']}, Have a nice Day")

        elif choice == "Swimming Pool":

            roomInfo["other_services"] += 300
            print(f"---> Thank you {roomInfo['name']}, Have a nice Day")
        
        elif choice == "Spa":

            roomInfo["other_services"] += 450
            print(f"---> Thank you {roomInfo['name']}, Have a nice Day")

        elif choice == "Gym":

            roomInfo["other_services"] += 200
            print(f"---> Thank you {roomInfo['name']}, Have a nice Day")

        else:

            print("---> Please select the service from the above Menu.")

    def saveDataToFile(self):

        try:
        
            with open("Booking.txt" , "w") as file:

                for room in self.roomDict:

                    roomInfo = self.roomDict[room]

                    if roomInfo is None:

                        file.write(
                            f'None\n'
                        )

                    else:

                        file.write(
                            f'{room}|{roomInfo["name"]}|{roomInfo["days"]}|{roomInfo["check_In"]}|{roomInfo["check_Out"]}|{roomInfo["food_charge"]}|{roomInfo["other_services"]}\n'
                        )
        
                print("---> Booking saved successfully.")

        
        except FileNotFoundError:

            print("---> Error in finding file.")

    def loadFromFile(self):

        try:

            with open("Booking.txt" , "r") as file:

                data = file.readlines()

                if not data:

                    print("---> No Booking have been saved to the database.")
                    return

                self.roomDict = {
                    101 : None,
                    102 : None,
                    103 : None,
                    104 : None,
                    201 : None,
                    202 : None,
                    203 : None,
                    204 : None,
                    301 : None,
                    302 : None,
                    303 : None,
                    304 : None
                }

                for line in data:

                    line = line.strip()

                    if not line:

                        continue

                    parts = line.split("|")

                    if len(parts) != 7:

                        continue

                    self.roomDict[int(parts[0])] = {
                        "name" : parts[1],
                        "days" : int(parts[2]),
                        "check_In" : parts[3],
                        "check_Out" : parts[4],
                        "food_charge" : int(parts[5]),
                        "other_services" : int(parts[6])
                    }

                print("---> All the Booking have been loaded successfully.")

        except FileNotFoundError:

            print("---> Booking file does not exist.")

    def terminate(self):

        print("---> Program terminated successfully.")



hotel = HotelManagement()



