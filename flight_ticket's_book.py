class fly:
    def __init__ (self, country,company):
        self.country=country
        self.company=company

    global mytic
    mytic=[]
    myticlist=mytic
    global qty0
    qty0=[]
    user_name=input("First Enter Your Name: ")
    
    def listcountry(self):
        count=1
        print("           LIST ALL COUNTRY'S ")
        for i in (self.country):
            print(f"{count}.{i}")
            count+=1  

    def bookticket(self):
        q=1
        if q<4:
            while  q<3:
                self.listcountry()
                global place
                place=int(input(("\nsir please select your country choice: ")))
                if place == 1:
                    place=self.country[0]
                    break
                elif place == 2:
                    place=self.country[1]
                    break
                elif place == 3:
                    place=self.country[2]
                    break
                elif place == 4:
                    place=self.country[3]
                    break
                elif place == 5:
                    place=self.country[4] 
                    break
                if place != (1,6):
                    print("Please enter correct number 🙂")
                continue
        qty=int(input("How many tickets want to you sir? (enter only number): "))
        if qty<1:
            qty=1
        mytic.append(place)
        qty0.append(qty)
        print(f"\nTake your ticket for going : {str(place).upper()} x {qty}")
        print("Successfully Booking Your Ticket's 😃!!!")

    def addticket(self):   
        self.bookticket()
        print("Add More Ticket's 😃!!!")

    def cancelticket(self):
        global mytic
        if mytic!=[]:
            mytic=[]
            print("Cancel All Ticket's 😞...")
        else:
            print("\nPlease Sir Frist Book Your Ticket... (✿◠‿◠)")

    def deletetic(self):
        num=0
        for i in (mytic):
            print(f"{num}.{i}")
            num+=1 
        while mytic!=[]:     
            userinput1=int(input("Choice Your Ticket: "))
            if  userinput1 <0:
                print("please enter correct number")
                continue
            elif userinput1 > num-1 :
                print("please enter correct number")
                continue
            elif userinput1 == 0:
                del mytic[0]
            elif userinput1 == 1:
                del mytic[1]
            elif userinput1 == 2:
                del mytic[2]
            elif userinput1 == 3:
                del mytic[3]
            elif userinput1 == 4:
                del mytic[4] 
            print("Delete Your Ticket 😑")
            break
        if mytic==[]:
            print("\nPlease Sir First Book Your Ticket... (✿◠‿◠)")

    def mytickets(self): 
        print(f"        🔥🔥🔥  {str(self.user_name).capitalize()} Profile  🔥🔥🔥\n")
        if mytic !=[]:
            print(f"Enjoy {self.user_name} 😁😁😁!\nYou Have:")
            for mytic1,qty2 in zip(mytic,qty0):
                print(f"         {mytic1} x {qty2} ticket's")
        if mytic == []:
            print(f"No Ticket's in Your Account {self.user_name} 😥😥😥")
        
if __name__== "__main__":
    countrys=fly(["England", "China", "London", "Canada", "Australia"],"JET GHOST👻" )
    
    print(f"        ****  WELCOME {str(fly.user_name).upper()} OUR {countrys.company} Flight    ****")
    while True:
        z=0
        i=1
        while i <2:
            z=z+1
            print(f"""\n{(fly.user_name).capitalize()} select option in this below.
        
            1.list country's (place)
            2.booking your ticket
            3.add more ticket's
            4.delete your ticket's
            5.cancel all ticket's
            6.my profile
            """)

            userinput=int(input("Enter your number: "))
            if userinput == 1:
                countrys.listcountry()
            elif userinput == 2:
                countrys.bookticket()
            elif userinput == 3:
                countrys.addticket()
            elif userinput == 4:
                countrys.deletetic()
            elif userinput == 5:
                countrys.cancelticket()
            elif userinput == 6:
                countrys.mytickets()
            elif i<2:
                if userinput != range(1,7):
                    if z==1:
                        print("Please enter correct number 🙂")
                if userinput != range(1,7):
                    if z==2:
                        print("Please enter correct number 😠😠")
                if userinput != range(1,7):
                    if z==3:
                        print("Please enter correct number 😤😤😤")
                if userinput != range(1,7):
                    if z==4:
                        print("Please enter correct number 😡😡😡😡")                
                if userinput != range(1,7):
                    if z>4:
                        print("Please enter correct number 🤬🤬🤬🤬🤬 fun")
                continue
            none=input("------------------------  Enter c to continue or q to exist  ------------------------: ")
            if none == "q":
                print("\nThank You Sir Using Our JET GHOST Service 🥰!!!")
                exit()
            elif none=="c":
                continue
            
