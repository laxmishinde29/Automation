import os

def main():
    FileName = input("Enter the name of File:")

    if(os.path.exists(FileName)):
        Ret = os.path.isabs(FileName)       #abs=absolute

        if(Ret == True):
            print("It is absolute path")

        else:
            print("It is relative path")
            NewPath = os.path.abspath(FileName)
            print("Updated path:",NewPath)

    else:
        print("Threr is no suh file")

if __name__ == "__main__": 
    main()