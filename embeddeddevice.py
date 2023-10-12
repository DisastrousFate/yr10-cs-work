# get name of embedded device and print the characteristics of the device inputted

devicetable = {
    "Microwave" : "Heats up food",
    "Washing Machine" : "Cleans Clothes",
    "Air Conditioning" : "makes air conditioned",
    "Heater" : "heats up"
    
}

device = str.lower(input("Enter name of embedded device"))

for x, v in devicetable.items():
    if str.lower(x) == device:
        print(x, "is an embedded device")
        print(v)
