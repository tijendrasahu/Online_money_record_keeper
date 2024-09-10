from main import customer
from main import client
import const

print(" -----------------WELCOME TO KHATA ----------------")
print(const.menu)
print("for negative money use - sign before amount")

cst = customer()

while True:
    cmd = input(">>> ")
    if cmd == 'ADD':
        inp1 = input("ENTER NAME >>>")
        inp2 = float(input("ENTER BALANCE >>>"))
        cst.add_new_data(cst.gen_CID(), inp1, cst.bal(inp2), inp2)
    elif cmd == 'EXIT':
        client.close()
        print("---------------Connection Closed Successfully--------------------------")
        exit()
    elif cmd == 'SEARCH':
        inp1 = input("ENTER NAME OF ACC.>>>")
        print(cst.search(inp1))
        inp2 = input("Enter Action (+ OR - TO ADD BAL OR PRESS ENTER)>>>")
        if inp2 == '+' or '-':
            inp3 = int(input("enter Amount>>>"))
            print(cst.search(inp1, inp3))
        else:
            pass
    elif cmd == 'DELETE':
        inp1 = input("Enter ACC Name ")
        print(cst.acc_del(inp1))
    else:
        pass
