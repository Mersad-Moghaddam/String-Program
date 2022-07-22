# START
import os
from MyClass import Mystring
# |------------------------------------------------------------------------------------|
# |delete Digit // delete sppaces // Add to star & end // Sum of Digit //Delete Comaa  |
# |------------------------------------------------------------------------------------|
os.system('clear')
print("Welcom To 'TEST STRING Programm'\n")
wait=input("Press Enter to continue...")
os.system('clear')
key=1
inputstring=Mystring(input("Enter Your STRING : "))
lenstring=int(inputstring.getlen())
StringFile=open("String Class/StringFile/String.txt",'w')
StringFile.write(inputstring.__str__()+f"\tLen {lenstring}")
StringFile.close()
os.system('clear')
while key!=0 :
    print(f"""Your Base : {inputstring}\nLen = {lenstring}\n
1.Delete Digit\n
2.Delete Spaces\n
3.ADD To Start & End\n
4.Cal Sum Of Digit in STRING\n
5.Delete Comma\n
6.New STRING\n
7.Show History\n
8.Exit\n""")
    order=int(input("Enter your order : "))
    os.system('clear')
    match order:
        #delete Digit 
        case 1:
            print(f"Your Base String : {inputstring}\t\t Len = {lenstring}")
            txt=Mystring(str(inputstring))
            txt.deletedigit()
            print(f"Resualt : {txt}\n")
            wait=input("Press Enter to continue...")
            ch=input("Save changes ? y/n : : ")
            if ch=='y':
                inputstring=Mystring(str(txt))
                StringFile=open("String Class/StringFile/String.txt",'a')
                StringFile.write("\nDelete Digit :\t"+txt.__str__()+f"\tLen {txt.getlen()}")
                StringFile.close()
                print("TASK DONE!! ")
                os.system('clear')
            elif ch=='n':
                os.system('clear')
        #delete spaces 
        case 2:
            print(f"Your Base : {inputstring}\n")
            txt=Mystring(str(inputstring))
            txt.deleteSpaces()
            print(f"Resualt : {txt}\n")
            wait=input("Press Enter to continue...")
            ch=input("Save changes ? y/n :")
            if ch=='y':
                inputstring=Mystring(str(txt))
                StringFile=open("String Class/StringFile/String.txt",'a')
                StringFile.write("\nDelete spaces  :\t"+txt.__str__()+f"\tLen {txt.getlen()}")
                StringFile.close()
                print("TASK DONE!! ")
                os.system('clear')
            elif ch=='n':
                os.system('clear')
        # Add to start & end
        # Add To start   Add To end  
        case 3:
            print(f"Your Base : {inputstring}\n")
            txt=Mystring(str(inputstring))
            print("1.Add TO Start\n\n2.ADD TO End\n\n3.Add To Start & End\n\n")
            order2=int(input("Enter your order : "))
            match order2:
                # Add To Start
                case 1:
                    start=input("Start :")
                    txt.start(start)
                    print(f"Resualt : {txt}\n")
                    wait=input("Press Enter to continue...")
                    ch=input("Save changes ? y/n :")
                    if ch=='y':
                        inputstring=Mystring(str(txt))
                        StringFile=open("String Class/StringFile/String.txt",'a')
                        StringFile.write("\nAdd To Start  :\t"+txt.__str__()+f"\tLen {txt.getlen()}")
                        StringFile.close()
                        print("TASK DONE!! ")
                        os.system('clear')
                    elif ch=='n':
                        os.system('clear')
                    os.system('clear')
                # Add To End
                case 2:
                    end=input("End :")
                    txt.end(end)
                    print(f"Resualt : {txt}\n")
                    wait=input("Press Enter to continue...")
                    ch=input("Save changes ? y/n :")
                    if ch=='y':
                        inputstring=Mystring(str(txt))
                        StringFile=open("String Class/StringFile/String.txt",'a')
                        StringFile.write("\nAdd To End  :\t"+txt.__str__()+f"\tLen {txt.getlen()}")
                        StringFile.close()
                        print("TASK DONE!! ")
                        os.system('clear')
                    elif ch=='n':
                        os.system('clear')
                    os.system('clear')
                # Add To Start & End
                case 3:
                    start=input("Start :")
                    end=input("End :")
                    txt.startend(start,end)
                    print(f"Resualt : {txt}\n")
                    wait=input("Press Enter to continue...")
                    ch=input("Save changes ? y/n :")
                    if ch=='y':
                        inputstring=Mystring(str(txt))
                        StringFile=open("String Class/StringFile/String.txt",'a')
                        StringFile.write("\nAdd To Start & End :\t"+txt.__str__()+f"\tLen {txt.getlen()}")
                        StringFile.close()
                        print("TASK DONE!! ")
                        os.system('clear')
                    elif ch=='n':
                        os.system('clear')
                    os.system('clear')
        # Sum of Digit
        case 4:
            print(f"Your Base : {inputstring}\n")
            txt=Mystring(str(inputstring))
            sumD=txt.sumdigits()
            print(f"Sum of Digit : {sumD}\n")
            wait=input("Press Enter to continue...")
            os.system('clear')
        # Delete Comaa
        case 5:
            print(f"Your Base : {inputstring}\n")
            txt=Mystring(str(inputstring))
            txt.DeleteComaa()
            print(f"Resualt : {txt}\n")
            wait=input("Press Enter to continue...")
            ch=input("Save changes ? y/n :")
            if ch=='y':
                inputstring=Mystring(str(txt))
                StringFile=open("String Class/StringFile/String.txt",'a')
                StringFile.write("\nDelete Comaa :\t"+txt.__str__()+f"\tLen {txt.getlen()}")
                StringFile.close()
                print("TASK DONE!! ")
                os.system('clear')
            elif ch=='n':
                os.system('clear')
            os.system('clear')
        # Enter New STRING
        case 6:
            inputstring=Mystring(input("Enter Your NEW STRING : \n"))
            lenstring=inputstring.getlen()
            StringFile=open("String Class/StringFile/String.txt",'a')
            StringFile.write("\n______________________________________________\n")
            StringFile.write(inputstring.__str__()+f"\tLen {lenstring}")
            StringFile.close()
            print("TASK DONE!! ")
            wait=input("Press Enter to continue...")
            os.system('clear')
        case 7:
            StringFile=open("String Class/StringFile/String.txt",'r')
            print(StringFile.read())
            wait=input("Press Enter to continue...")
            os.system('clear')
        # Exit
        case 8:
            print("GOOD LUCK ! <3")
            wait=input("Press Enter to Exit ... ")
            Key=0
            break; 
# THE END