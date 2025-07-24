cp=int(input("enter the cost price of item:"))
sp=int(input("enter the selling price of the item:"))
if cp<sp:
    p=sp-cp
    print("profit:",p)
elif cp==sp:
    print("there is no prifit or loss")
else:
    l=cp-sp
    print("loss:",l)