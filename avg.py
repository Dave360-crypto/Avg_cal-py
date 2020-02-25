#This progam was developed by Malvern Shaurwa

#This is basically a python script that calculates the average height of ten people in a class

def main():
    sum = 0
    count = 0

    while count < 10:
        try:
            h = input("height %d : " % (count + 1) )
            sum+=float(h)
            count+=1

        except:
           print("invalid input please enter a interger")

    print("\n average %.2f" % (sum/10))

main()
