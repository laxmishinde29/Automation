import sys
import os
import time
import schedule

def DirectoryScanner(DirName = "Marvellous"):
    Border = "-"*50
    timestamp = time.ctime()

    Logfilename = "Marvellous%s.log" %(timestamp)
    Logfilename = Logfilename.replace(" ","_")
    Logfilename = Logfilename.replace(":","_")
    
    fobj = open(Logfilename,"w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a Directory cleaner Script\n")
    fobj.write(Border+"\n")

    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It s not a directory")
        return

    FileCount = 0
    EmptyFileCount = 0
    for FolderName,SubFolder,FileName in os.walk(DirName):
        

        for fname in FileName:
            FileCount = FileCount+1

            fname = os.path.join(FolderName,fname)
            

            if(os.path.getsize(fname)==0):      #emptyfile
                EmptyFileCount = EmptyFileCount+1
                os.remove(fname)

    fobj.write("Total file scanned:"+str(FileCount)+"\n")
    fobj.write("Total empty file found:"+str(EmptyFileCount)+"\n")
    fobj.write("This log file is ceated at:"+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():
    Border = "-"*50
    print(Border)
    print("---------Marvellous Directory Automation-----")
    print(Border)

    if(len(sys.argv)!=2):
        print("Invalid numer of arguments")
        print("Please specify the name of directory")
        return

    #DirectoryScanner(sys.argv[1])

    schedule.every(1).minute.do(DirectoryScanner)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print(Border)
    print("---------Marvellous Directory Automation-----")
    print(Border)

if __name__ == "__main__":
    main()