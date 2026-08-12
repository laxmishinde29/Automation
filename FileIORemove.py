import os

def main():
    FileName = input("Enter the name of File:")

    if(os.path.exists(FileName)):
        os.remove(FileName)
        print("File gets deleted")
        
    else:
        print("Threr is no suh file")

if __name__ == "__main__": 
    main()