from sys import argv
from tabnanny import check
from constants_store import *
from objects import *
from operations import return_discount
from collections import OrderedDict

TOTAL = 0
TOTAL_DISCOUNT = 0
TOTAL_FASTAG = 0
TOTAL_CASH = 0

def addVehicle(vehicle, fastag):
    if (vehicle[0] == 'C'):
        VEHICLES.update({vehicle:Car(vehicle, fastag)})
    if (vehicle[0] == 'V'):
        VEHICLES.update({vehicle:Van(vehicle, fastag)})
    if (vehicle[0] == 'B'):
        VEHICLES.update({vehicle:Bus(vehicle, fastag)})
    if (vehicle[0] == 'T'):
        VEHICLES.update({vehicle:Truck(vehicle, fastag)})
    if (vehicle[0] == 'R'):
        VEHICLES.update({vehicle:Rikshaw(vehicle, fastag)})
    if (vehicle[0] == 'S'):
        VEHICLES.update({vehicle:Scooter(vehicle, fastag)})
    if (vehicle[0] == 'M'):
        VEHICLES.update({vehicle:Motorbike(vehicle, fastag)})
        

def getVehicle(vehicle):
    type = ""
    if (vehicle[0] == 'C'):
        type = "CAR"
    if (vehicle[0] == 'V'):
        type = "VAN"
    if (vehicle[0] == 'B'):
        type = "BUS"
    if (vehicle[0] == 'T'):
        type = "TRUCK"
    if (vehicle[0] == 'R'):
        type = "RIKSHAW"
    if (vehicle[0] == 'S'):
        type = "SCOOTER"
    if (vehicle[0] == 'M'):
        type = "MOTORBIKE"
    return type

        
def calculate_total():
        global TOTAL
        TOTAL += TOTAL_FASTAG + TOTAL_CASH
        
    
def main():
    if len(argv) != TWO:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    total, discount = [ZERO, ZERO]
    newdict = {}
    arr = []
    
    global TOTAL ,TOTAL_DISCOUNT ,TOTAL_FASTAG ,TOTAL_CASH 
    
    for line in lines:
        if (len(line.split(" ")) > ONE):
            action, vehicle, fastag = line.split()
            
            if (action == "FASTAG"):
                addVehicle(vehicle, int(fastag))
                
            if (action == "COLLECT_TOLL"):
                
                vehicle = fastag
                discount = ZERO
                
                if (vehicle in VEHICLES):
                    VEHICLES[vehicle].add_trip()
                else:
                    addVehicle(vehicle, ZERO)
                    VEHICLES[vehicle].add_trip()
                    
                if (VEHICLES[vehicle].get_trip() > 1):
                    discount = return_discount(
                        VEHICLES[vehicle].get_trip(), VEHICLES[vehicle].get_price(), discount)
                    TOTAL_DISCOUNT = return_discount(
                        VEHICLES[vehicle].get_trip(), VEHICLES[vehicle].get_price(), TOTAL_DISCOUNT)
                
                
                if (VEHICLES[vehicle].get_fastag_balance() >= VEHICLES[vehicle].get_price()):
                    
                    VEHICLES[vehicle].set_fastag_balance()
                    TOTAL_FASTAG += VEHICLES[vehicle].get_price()-discount
                
                elif (VEHICLES[vehicle].get_fastag_balance() == ZERO):
                    
                    VEHICLES[vehicle].set_cash(VEHICLES[vehicle].get_price())
                    TOTAL_CASH += VEHICLES[vehicle].get_price() + PENALTY -discount
                    
                else:
                    
                    remaining = VEHICLES[vehicle].get_price() - VEHICLES[vehicle].get_fastag_balance()
                    TOTAL_CASH += remaining + PENALTY-discount
                    TOTAL_FASTAG += remaining-discount
                    VEHICLES[vehicle].set_cash(remaining)
                    
                
                    
                
        else:
            
            calculate_total()
            print("TOTAL_COLLECTION ", int(TOTAL), int(TOTAL_DISCOUNT))
            print("PAYMENT_SUMMARY ", int(TOTAL_FASTAG), int(TOTAL_CASH))
            print("VEHICLE_TYPE_SUMMARY")
            
            print(" ")
            print("old dictionary = ", VEHICLES)

            for vehicle in VEHICLES.keys():
                arr.append(VEHICLES[vehicle].get_cash())
                arr.sort()
                # newdict.update({VEHICLES[vehicle].get_cash(): VEHICLES[vehicle]})
                # print(VEHICLES[vehicle].get_cash())
             
            print(" ")   
            print("new array = ",arr)
            
            


            for i in range(len(arr)):
                for vehicle in VEHICLES.values():
                    if vehicle.get_cash() == arr[i]:
                        print(getVehicle(vehicle.get_vehicle()), " ", vehicle.get_trip())
                        del(vehicle)
                        break

            # od = OrderedDict(sorted(VEHICLES.items()))
            
            # print(" ")
            # print(od)
            # print(" ")
            
            # for v in od.keys():
            #     print(getVehicle(od[v].get_vehicle()), " ", od[v].get_trip())

            # print("<vehcle type wth max colecton>< no of trips>", , )
            
            
    print(" ")
    
if __name__ == "__main__":
    main()