import math as m
import shutup
import sigfig
from sigfig import round as rnd


# function to compute x_bar; aka the mean/average
def average(lst) -> float:
    return sum(lst) / len(lst)
 
 
# function to compute standard deviation of a sample
def stdevAverage(lst) -> float:
    avg = average(lst)
    numerator = 0 
    denominator = (len(lst) - 1)

    for i in range(len(lst)):
        numerator += (lst[i] - avg) ** 2
    
    return rnd(m.sqrt(numerator / denominator), 1)


# function to prompt the user until a valid input is put in
def ask(prompt) -> bool:
    while True:
        attempt = str(input(prompt)).lower().strip()
        if attempt == "n":
            return False
    
        elif attempt == "Y":
            return True
        
        else:
            print("\nInvalid input. Please try again.")
            
    
# driver code
try:
    while True:
        termsList = []
        n_terms = int(input("Enter the number of terms: "))
    
        if n_terms > 1:
            for i in range(n_terms):
                term = float(input("Enter the term itself: "))
                termsList.append(term)
    
            avg = average(termsList)
            strAvg = str(avg)
            avgSigFig = int(strAvg[strAvg.find('.') + 1])
    
            dev = stdevAverage(termsList)
    
            print(f"The average is {rnd(avg, sigfigs=avgSigFig, warn=False)}; which is rounded to {avgSigFig} significant figure(s).")
            print(f"The standard deviation (stdev) is {dev}; which is rounded to 1 significant figure.")
            print(f"The final answer is: x_bar = {avg} +- {dev} units.")
        
        else:
            raise ZeroDivisionError
    
        attempt = ask("Try again? (Y/N): ")
        if attempt == False:
            break
   
 
except (ValueError, KeyboardInterrupt, TypeError):
    print("Exiting code.\n")
    
except ZeroDivisionError:
    print("Cannot have 1 term only! Exiting code.\n")
    
shutup.please()
shutup.jk()
