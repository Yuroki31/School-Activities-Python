#Variable declaration and input
lot_n = str(input("Please enter the lot's name and press enter: "))
lot_a = str(input("Please enter the lot's address and press enter: "))
time_in = int(input("Please enter the time in (24 hour notation) and press enter: "))
time_out = int(input("Please enter the time out and press enter: "))

#Parking fee calculation
parking_hours = (time_out - time_in) // 100
parking_fee = parking_hours * 40

#Printing the receipt
print("\n",lot_n)
print(lot_a)
print("Time-in: " +str(time_in) + "\n" "Time out: " + str(time_out))
print("Amount due: ₱",parking_fee)
print("Thank you for using", lot_n)
print("BUCKLE UP")
print("AND DRIVE SAFELY")


