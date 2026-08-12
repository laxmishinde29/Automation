#Commandline input 1

import psutil
import sys

def main():
    Border = "-"*50
    print(Border)
    print("-----Marvellous Platform Surveillance Systems-----")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is use to : ")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : send mail with the logs")
            print("4 : store information about processes")
            print("5 : store information about CPU")
            print("6 : Store usage about RAM usage")
            print("7 : store infomation about secondary storage")

        elif(len(sys.argv) == 2):
            if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
                print("Use the automation script as")
                print("ScriptName.py TimeInterval DirectoryName")
                print("TimeInterval : The time in minutes for periodic scheduling")
                print("DirectoryName : Name of directory to create auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    #python Demo.py 5 Marvellous
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval :",sys.argv[1])
        print("Directory Name :",sys.argv[2])

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("----------Thank You For Using Our Script----------")
    print(Border)

if __name__ == "__main__":
    main()