#Commandline input 5

import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):
    Border = "-"*50
    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create Folder")
            return

    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("log file gets created with name :",FileName)

    fobj = open(FileName, "w")
    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Surveillance Systems-----\n")
    fobj.write("log created at :"+time.ctime()+"\n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    fobj.write(Border+"\n")
    fobj.write("--------------- End of log file ---------------\n")
    fobj.write(Border+"\n")

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
        
        #Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("Platform Surveillance Systems started successfully")
        print("Directory created with name :",sys.argv[2])
        print("Time interval in minutes:",sys.argv[1])
        print("Press ctrl + c to stop the execution")
        #wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("----------Thank You For Using Our Script----------")
    print(Border)

if __name__ == "__main__":
    main()