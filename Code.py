s=0
r=0
sp=30
rp=40
e1hrs=0
e2hrs=0
A_wr=0
B_wr=0
tss=0
trs=0
boutique_sales=0

#to add samosa and roll in stock 
def add(asa,aro):
    global s,r
    s+=asa
    r+=aro
    return

#to show quantity of samosa and roll in stock 
def item_quantity():
    print ('samosa =',s, 'roll=',r)
    return 

#to order roll and samosa and to create bill and adjust stock
def order(oro,osa):
    global s,r,tss,trs
    if s<osa:
        if s!=0:
            print('we have only samosas',s,"\n please order within our stock")    
        else:
            print ('samosa out of stock')
    elif s>=osa:
        s-=osa
        tss+=osa
        priceofsamosa=osa*sp
        print('samosa price', priceofsamosa)
    if r<oro:
        if r!=0:
            print ("rolls in stock left",r,"\n please order within our stock")   
        else:
            print ('rolls out of stock')
    elif r>=oro:
        r-=oro
        trs+=oro
        priceofroll=oro*rp
        print ('roll price', priceofroll)
   
    
    
   
 
#set employee wage rate input by user
def employee_wage_rate(wr1,wr2):
    global A_wr,B_wr
    A_wr=wr1
    B_wr=wr2  
    print(f'Wage rate per hour for employee 1is set to{A_wr} and employee 2\'s is{B_wr} ')  


#add hrs worked by each employee
def hrs(h1,h2):
    global e1hrs,e2hrs
    e1hrs+=h1
    e2hrs+=h2
    print (f'Worked hours of both employees are updated, employee 1 hrs are {e1hrs} and 2 hrs are{e2hrs}   ')
    
     
#calculate salary of employees
def salary():
    Sal1=A_wr*e1hrs
    Sal2=B_wr*e2hrs
    print ('Employee1 salary for',e1hrs,'hours', ':',Sal1,"\nEmployee 2 salary for ",e2hrs,"hours is",Sal2)
    return 

#to calculate bonus if sales in 6 hrs reach 100(50 samosa and 50 roll)
def bonus():
    if e1hrs<=1  and tss>=asa/2 and trs>=aro/2:
        b1=A_wr*0.1
        print ('bonus is awarded to employee1 as he sales in 1 hr samosa and rolls equal to or more then half of stock ',b1)
    else:
        print('bonus  is not awarded to employee1 as he not sales in 1 hr samosa and rolls equal to or more then half of stock ')    
            
    if e2hrs<=1 and tss>=asa/2 and trs>=aro/2:
        b2=B_wr*0.1
        print ("bonus is awarded to employee2 as he sales in 1 hr samosa and rolls equal to or more then half of stock ",b2)
    else:
        print('bonus  is not awarded to employee2 as he not sales in 1 hr samosa and rolls equal to or more then half of stock ')


#if boutique sales is greater than 15000 then 1 dozen samosas and rolls are free                
def boutique():
    global boutique_sales,s,r
    if boutique_sales >=15000:
        s-=12
        r-=12
        print ('Congratulations! you got free 1 dozen both samosa and roll from my bake shop for buying cloths of more than 15000 from our boutique shop')
    else:
         print ('Oops! you don\'t got free 1 dozen both samosa and roll from my bake shop for not buying cloths of more than 15000 from our boutique shop')
 
                     
while True:  
    print('Welcome to bake shop\n1 For add items in stock \n2 for show quantity of stock\n3 for place order and generate bill\n4 for setting employee wage rate\n5 for add hours worked by employees\n6 for calculate salary of employees\n7 for issue bonus\n8 for providing boutique customers free samosas and rolls\n9 for exit')
    choose =int(input('enter your choice'))
    if choose ==1:
        asa=int(input('add samosa in stock:'))
        aro=int(input('add roll in stock:'))
        add(asa,aro)
        print ('see samosas and rolls are successfully add into stock')
        item_quantity()
    if choose ==2:
        item_quantity()
    if choose ==3:
        oro=int(input('order roll'))
        osa=int(input('order samosa'))
        order(oro,osa)    
    if choose ==4:
        wr1=float(input('wage rate per hour for employee A:'))
        wr2=float(input('wage rate per hour for employee B:'))
        employee_wage_rate(wr1,wr2)
    if choose ==5:
        h1=float(input('hours work by employee A'))
        h2=float(input('hours work by employee B'))    
        hrs(h1,h2)
    if choose ==6:
        salary()
    if choose ==7:
        bonus ()
    if choose ==8:
        boutique_sales=float (input('Enter customer\'s bought price '))
        boutique ()
    if choose ==9:
        break
    
