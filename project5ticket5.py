age=int(input("enter the age:"))
day_of_weak=input("enter the day:")

if age>0 and age<12:
    ticket_price=5
    if day_of_weak=="saturday" or day_of_weak=="sunday":
        discount=10
    else:
        discount=0

elif age>=13 and age<17:
        ticket_price=8
        if day_of_weak=="saturday" or  day_of_weak=="sunday":
            discount=10
        else:
            discount=0

      

elif age>=18 and age<65:
        ticket_price=12
        if day_of_weak=="saturday" or day_of_weak=="sunday":
            discount=10
        else:
            discount=0
      

elif age>65:
        ticket_price=7
        if day_of_weak=="saturday" or day_of_weak=="sunday":
            discount=10
        else:
            discount=0
        

dis_price=ticket_price*discount/100
after_dis_price=ticket_price-dis_price
print(f"""________________________________movie ticket_____________________
        age:{age} 
        the day_of_week {day_of_weak}
        after dis={after_dis_price}
        discount   {discount}""")

    

    

    


        
    
    
    

    

