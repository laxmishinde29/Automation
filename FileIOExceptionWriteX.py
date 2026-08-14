def main():
    try:
        fobj = open("Hello.txt","w")            #fobj is handel
        print("File gets succesfully open")

        fobj.write("Jay Ganesh Marvellous...")

        fobj.close()

    except FileNotFoundError:
        print('Unable to open file as there is no such file')

    finally:
        print("End of application")

if __name__ == "__main__": 
    main()