# get name of embedded device and print the characteristics of the device inputted

devicetable = {
    "Microwave" : {"Function" : "Make food hot and cook it",
                   "User Interface" : "Buttons and screen to control settings",
                   "Inputs" : "Dial and button to change time in microwave" 
                },
    "Washing Machine" : {"Function" : "Wash clothes to make clean",
                        "User Interface" : "Screen and dial to change washing mode",
                        "Inputs" : "Dial and on/off button" 
                    },
    "Air Conditioning" : {"Function" : "Condition the air to make cooler",
                        "User Interface" : "Remote control and screen",
                        "Inputs" : "Buttons and buzzer to sound press sound effect" 
                    },
    "Heater" : {"Function" : "Make the air to make warmer",
                "User Interface" : "Remote control and screen",
                "Inputs" : "Buttons and buzzer to sound press sound effect" 
            },
    "Toaster" : {"Function" : "Make toast through heating bread up",
                "User Interface" : "Dial and slide button",
                "Inputs" : "Dial and slide button" 
            },
    
}

def infoAboutDevice(device, funcTable):
    firstTimeRun = True
    while True:

        if firstTimeRun:
            print("What would you like to know about a " + device + "?") 
            valueWanted = int(input("1. Function\n2. User Interface\n3. Inputs"))

            firstTimeRun = False
        else:
            print("What else would you like to know about a " + device + "?, or you can choose another device")
            valueWanted = int(input("1. Function\n2. User Interface\n3. Inputs\n4. Choose other device"))
            if valueWanted == 4:
                break

        keys = list(funcTable)
        keyWantedInList = keys[valueWanted - 1]
        print(funcTable[keyWantedInList])
    
    return True

def getDevice():

    inputDevice = str.lower(input("Enter name of embedded device "))

    for device, funcTable in devicetable.items():
        if str.lower(device) == inputDevice:

            print(device, " is an embedded device because it has one function")
            done = infoAboutDevice(device, funcTable)
            if done:
                getDevice()

getDevice()

