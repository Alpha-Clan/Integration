import os 
print(" ____    _    ____ _____ _   _  __     ___    ____  _____ ____ ")
print("|  _ \  / \  |  _ \_   _| | | | \ \   / / \  |  _ \| ____|  _ \ ")
print("| | | |/ _ \ | |_) || | | |_| |  \ \ / / _ \ | | | |  _| | |_) |")
print("| |_| / ___ \|  _ < | | |  _  |   \ V / ___ \| |_| | |___|  _ <")
print("|____/_/   \_\_| \_\|_| |_| |_|    \_/_/   \_\____/|_____|_| \_\ ")
print("\n")  
u_inp=int(input("Enter The Tool Number to be executed:")) #interactivequestion 

if u_inp==1:
    os.system("python3 wlgen.py -i") #(1)

elif u_inp==2:
    os.system("./pentmenu") #(2)
    
elif u_inp==3:
    os.system("python3 photon.py") #(3)
    

else:
    print("1 -2 -3 not found")