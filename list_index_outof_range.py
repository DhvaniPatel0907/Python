try :
    l1=[8,12,65,71,16,32]
    n=int(input("Enter index:"))
    print("Value of index is",l1[n])
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)
