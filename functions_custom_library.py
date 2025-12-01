# check number is even or not
def is_even(n):
    if type(n)!=int:
         return "Not allowed other than integer"
        
    
    return  n % 2==0

# check flexibility 
def flexi(*number):
     product=1
     for i in number:
          product*=i
     
     return product
           