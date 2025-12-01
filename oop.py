# Example ATM demo 
'''
Example output below

1. Create Pin 
2. Deposit Amount
3.Withdraw Amount
4.Check Amount
5.Exit?
Option ? : 1
Enter your Pin 123
Pin Create Successfully
1. Create Pin
2. Deposit Amount
3.Withdraw Amount
4.Check Amount
5.Exit?
Option ? : 4
Enter your pin : 123
Balance is :  0
1. Create Pin
2. Deposit Amount
3.Withdraw Amount
4.Check Amount
5.Exit?
Option ? : 2
Enter your pin : 123
Enter your deposit amount : 50000
Deposit Amount Successfully
1. Create Pin
2. Deposit Amount
3.Withdraw Amount
4.Check Amount
5.Exit?
Option ? : 4
Enter your pin : 123
Balance is :  50000
1. Create Pin
2. Deposit Amount
3.Withdraw Amount
4.Check Amount
5.Exit?
Option ? : 3
Enter your pin : 123
Enter your withdraw amount : 20000
Deposit Amount Successfully
1. Create Pin
2. Deposit Amount
3.Withdraw Amount
4.Check Amount
5.Exit?
Option ? : 4
Enter your pin : 123
Balance is :  30000
1. Create Pin
2. Deposit Amount
3.Withdraw Amount
4.Check Amount
5.Exit?
Option ? :
'''



class ATM:

    # in some cases we need a variables which  is same for all objects like static variables 
    counter=1
    # constructor 

    def __init__(self):
        #encapsulate  data variables (but in python its not 100% private as java or others because this pythons is for adults hahaha so be mature )
        # instance variables which is different for each object like his pin or his balance below
        self.__pin=""
        self.__balance=0
        self.serial_number=ATM.counter
        ATM.counter+=1

        # self.menuATM()

# getter , setter pin

    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        self.__pin=new_pin

    def menuATM(self):
        print("1. Create Pin \n2. Deposit Amount \n3.Withdraw Amount \n4.Check Amount\n5.Exit? ")
        choice=int(input("Option ? : "))
        while(choice!=5):
            
            if(choice==1):
                self.createPin()
            elif(choice==2):
                self.depositAmount()
            elif(choice==3):
                self.withdrawAmount()
            elif(choice==4):
                self.checkAmount()
            elif(choice==5):
                print("Exit!")
            print("1. Create Pin \n2. Deposit Amount \n3.Withdraw Amount \n4.Check Amount\n5.Exit? ")
            choice=int(input("Option ? : "))
       
        


    def createPin(self):
        self.__pin=input("Enter your Pin ")
        print("Pin Create Successfully")

    def depositAmount(self):
        pin=input("Enter your pin : ")
        if(pin==self.__pin):
            self.__balance += int(input("Enter your deposit amount : "))
            print("Deposit Amount Successfully")

    def withdrawAmount(self):
        pin=input("Enter your pin : ")
        if(pin==self.__pin):
            am= int(input("Enter your withdraw amount : "))
            if(am>self.__balance):
                print("Insufficient blance")
            else:
                self.__balance -= am
                print("Deposit Amount Successfully")

    def checkAmount(self):
        pin=input("Enter your pin : ")
        if(pin==self.__pin):
            print("Balance is : " , self.__balance)
    


# client=ATM()


'''
Example on static variables which is shareable 
here is the output for below code 
```
1
2
3
4 
```
'''
c1=ATM()
c2=ATM()
c3=ATM()

print(c1.serial_number)
print(c2.serial_number)
print(c3.serial_number)


print(ATM.counter)


