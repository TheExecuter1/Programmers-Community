def factorial(n):

    if ( n == 0 ):
         print ("0")
				 
    elif (n<0):
        print ("enter a positive value")
				
    else :    
        fact = 1 
        for a in range (1 , n+1):
            fact = fact * a
        return(fact)
