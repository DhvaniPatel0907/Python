try :
    n1=int(input("enter number:"))
    n2=int(input("enter  number:"))
    print("Division:",n1/n2)

    
except ValueError as e:
    print(e)

except ZeroDivisionError as e:
    print(e)