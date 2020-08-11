def panprimo(n):
    pandigital = True
    primo = True
    #comprueba si es pandigital
    for x in range(10):
        texto1=str(x)
        texto2=str(n)
        if texto1 not in texto2:
            pandigital = False 
            return False   
    #comprueba si es primo
    ud=n%1000
    if ud%2 == 0 or ud%3 == 0 or ud%5 == 0 or ud%7 == 0 or ud%9 == 0 or ud%11 == 0:
        primo=False
        return False
    for y in range(2, ud):
        if ud%y == 0:
            primo=False
    #revisa que ambas condiciones se cumplan      
    if pandigital == True and primo == True:
        return True
    else:
        return False
      


print(panprimo(1234567890121))
             
        
        