import sys

def main():
    Border = "-"*40
    print(Border)
    print("--------- Marvellous Automation ---------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):              #help
            print("This application used to perform ____")
            print("This is the automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):              #help
            print("Use the given script as")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1 : ___________")
            print("Argument2 : ___________")

        else:
            print("Use given flags as :")
            print("--u : Used to display a usage")
            print("--h : Used to display a help")

    else:
        print("Invalid number of command line arguments")
        print("Use given flags as :")
        print("--u : Used to display a usage")
        print("--h : Used to display a help")

    print(Border)
    print("------ Thank you for using script ------")
    print("-------- Marvellous Infosystems --------")
    print(Border)

if __name__ =="__main__":
    main()