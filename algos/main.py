
from algos import algorithms

##Proste menu wyboru funkcji do wykonania
# Wersja 1.0
version = "1.0"
# projekt_sinwo
# Mateusz Liber & Mateusz Latkowski & Antoni Goszcz

def main():
    'Function contains simple selection menu'
    task_list = [algorithms.Euclidean(), algorithms.LCM(), algorithms.Fibonacci(), algorithms.Quadratic_formula(), algorithms.Hanoi(), algorithms.FermatFactorization(), algorithms.BubbleSort()]
    
    print("\nSelect the algorithm to perform:\n")
    
    for i in range(len(task_list)):
        print(str(i+1)+". "+str(task_list[i]))
    
    print("")
    print('Pick Algorithm: \n')
    task_tmp = input("Alghoritm: ")
     
    if(int(task_tmp) <= len(task_list)):
        acctual_algorithm = task_list[(int(task_tmp)-1)]
        print("Output: ", acctual_algorithm.start())
        print()
    else:
        print("Ivaild Algortihm Number")
        print()
main()





