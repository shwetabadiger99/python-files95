rent=int(input("enter the rent"))
food=int(input("total food orderd"))
electricity=int(input("total electricity used"))
charge=int(input("enter the per unit"))
persons=int(input("enter the persons in living"))

total_bill=electricity * charge

output=(food+rent+total_bill) / persons

print("the total rent:",output)  
