import pickle 
import datetime

# Main menu
def Menu():
    print('*'*160)
    print('MAIN MENU'.center(100))
    print(' '*45+'1. Insert Employee Record/Records')
    print(' '*45+'2. Display Sorted Empolyee Records as per Emp No')
    print(' '*45+'3. Display Sorted Empolyee Records as per Names')
    print(' '*45+'4. Display Sorted Empolyee Records as per Designation')
    print(' '*45+'5. Display Employee Records as the Designation ')
    print(' '*45+'6. Delete Record')
    print(' '*45+'7. Update Record')
    print(' '*45+'8. Search Employee Record Details as per the Employee ID')
    print(' '*45+'9. Search Record Detalis as per the Customer Name')
    print(' '*45+'10. Apply for leave')
    print(' '*45+'11. Display Gross Salary Breakup')
    print(' '*45+'12. Display salary receipt')
    print(' '*45+'13. Display total number of active employee')
    print(' '*45+'14. EXIT')
    print('*'*160)


# Sort according to ID
def SortAcc(f):
    try:
        with open(f,'rb+') as fil:
            rec=pickle.load(fil)
            rec.sort(key=lambda rec:rec['ID'])
            fil.seek(0)
            pickle.dump(rec,fil)
    except FileNotFoundError:
        print(f,'File has no records')


# Sort according to Name
def SortName(f):
    try:
        with open(f,'rb+') as fil:
            rec=pickle.load(fil)
            rec.sort(key=lambda rec:rec['NAME'])
            fil.seek(0)
            pickle.dump(rec,fil)
    except FileNotFoundError:
        print(f,'File has no records')


# Sort according to Designation
def SortDesig(f):
    try:
        with open(f,'rb+') as fil:
            rec=pickle.load(fil)
            rec.sort(key=lambda rec:rec['Desig'])
            fil.seek(0)
            pickle.dump(rec,fil)
    except FileNotFoundError:
        print(f,'File has no records')


# Insertion function
def Insert(f):
    try:
        fil=open(f,'ab+')
        print(fil.tell())
        Des=['MGR','CLK','VP','PRES']
        Dep=['HR','IT','SALES','FINANCE']
        if fil.tell()>0:
            fil.seek(0)
            Rec1=pickle.load(fil)
        else:
            Rec1=[]
        while True:
            while True:
                Eid=input('Enter Emp Id: ')
                Eid=Eid.upper()
                if any(dict.get('ID')==Eid for dict in Rec1):
                    print('Employee already exists')
                else:
                    break
            Name=input('Enter Employee Name: ')
            while True:
                Mob=input('Enter Mobile Number: ')
                if len(Mob)!=10 or Mob.isdigit()==False:
                    print('Please enter valid Mobile No: ')
                else:
                    break
            while True:
                Email=input('Enter Email: ')
                if'@' not in Email or '.'not in Email:
                    print('Enter valid mail address: ')
                else:
                    break
            while True:
                DeptId=input('Enter Dept Name of the Empolyee(HR/IT/SALES/FINANCE): ')
                if DeptId.upper() in Dep:
                    break

            while True:
                Desig=input('Enter the Designation(MGR/CLK/PRES/VP): ')
                if Desig.upper() in Des:
                    break

            Sal=float(input('Enter Salary'))
            Dat=datetime.datetime.now()
            Dat=Dat.date()

            while True:
                Leaves=int(input("Enter leave status, 0 for not taken, 1 for taken: "))
                if Leaves==0 or Leaves==1:
                    break
            while True:
                Salary_status=int(input("Enter salary status, 0 for pending 1 for given: "))
                if Salary_status==0 or Salary_status==1:
                    break

            Rec={
            'ID':Eid.upper(),
            'NAME':Name.upper(),
            'Mob':Mob,
            'Email':Email.upper(),
            'DeptId':DeptId.upper(),
            'Desig':Desig.upper(), 
            'Sal':Sal,
            'Date':Dat,
            'Leaves': Leaves,
            'Salary_status':Salary_status
            }

            Rec1.append(Rec)
            pickle.dump(Rec,fil)
            ch=input('Do you want to enter more records')
            if ch=='N' or ch=='n':
                break
        fil.close()
        with open(f,'wb')as fil:
            pickle.dump(Rec1,fil)
            
    except ValueError:
        print('Invalid values entered')


# Display function
def Display(f):
    try:
        with open(f,'rb')as fil:
            print('='*160)
            f='%15s %15s %15s %15s %15s %15s %15s %15s %15s %16s'
            print(f%('ID','NAME','MOBILE','EMAIL ADDRESS','Dept ID','Designation','SALARY','DATE OF JOINING', 'Leave status', 'Salary status'))
            print('='*160)
            Rec=pickle.load(fil)
            c=len(Rec)
            for i in Rec:
                for j in i.values():
                    print('%15s' % j,end='')
                print()
            print()
            print('*'*160)
            print('Records Read :',c)

    except EOFError:
        print('='*160)
        print('Records Read :',c)

    except FileNotFoundError:
        print(f,"File Doesn't exist")



# Display according to Designation
def DisplayonDesig(f):
    try:
        with open(f,'rb')as fil:
            Des=['MGR','CLK','VP','PRES']
            print('='*160)
            Rec=pickle.load(fil)
            while True:
                D=input('Enter the Designation(MGR/CLK/PRES/VP)')
                if D.upper() in Des:
                    break
            c=0
            f='%15s %15s %15s %15s %15s %15s %13s %15s %15s'
            print(f%('ID','NAME','MOBILE','EMAIL ADDRESS','Dept ID','Designation','SALARY','DATE OF JOINING', 'Leave status'))
            print('='*160)
            for i in Rec:
                if i['Desig']==D.upper():
                    c+=1
                    for j in i.values():
                        print('%15s'% j,end='')
                    print()
            print('*'*160)
            print('Records Read:',c)

    except EOFError:
        print('='*160)
        print('Records Read :',c)

    except FileNotFoundError:
        print(f,"Files Doesn't exist")


# Update function
def Update(f):
    try:
        with open(f,'rb+')as fil:
            found=0
            Rec=pickle.load(fil)
            A=input('Enter the Emp ID whose details to be changed: ')
            for p in Rec:
                if A==p['ID']:
                    found=1
                    for i in p.items():
                        if i!='Date':
                            if i!='Sal':
                                ch=input('Change '+i+'(Y/N): ')
                                if ch=='y'or ch=='Y':
                                    p[i]=input('Enter new '+i)
                                    p[i]=p[i].upper()
                            elif i=='Sal':
                                ch=input('Change '+i+'(Y/N): ')
                                if ch=='y'or ch=='Y':
                                    p[i]=float(input('Enter new '+i))
                    
                    break
                
            if found==0:
                print('Employee details not found ')
            else:
                fil.seek(0)
                pickle.dump(Rec,fil)

    except EOFError:
        print('Records not found ')
    except FileNotFoundError:
        print(f,"Files Doesn't exist")


# Delete function
def Delete(f):
    try:
        with open(f,'rb+')as fil:
            Rec=pickle.load(fil)
            ch=input('Enter the Employee ID to be deleted: ')
            for i in range(0,len(Rec)):
                if Rec[i]['ID']==ch:
                    print('*'*160)
                    f='%15s %15s %15s %15s %15s %15s %15s %15s %15s %15s'
                    print(f%('ID','NAME','MOBILE','EMAIL ADDRESS','Dept ID','Designation','SALARY','DATE OF JOINING','Leave status', 'Salary status'))
                    N=Rec.pop(i)
                    for j in N.values():
                        print('%15s'% j,end='')
                    print()
                    print('Record Deleted')
                    break
            else:
                print('Record Not found')

            fil.seek(0)
            pickle.dump(Rec,fil)

    except FileNotFoundError:
        print('Records not found ')
    except KeyError:
        print('Record not found')
    except IndexError:
        print('Record not found')


# Search function according to ID
def SearchID(f):
    try:
        with open(f,'rb')as fil:
            Rec=pickle.load(fil)
            found=0
            ch=input('Enter the Customer ID to be searched: ')
            print('*'*160)
            f='%15s %15s %15s %15s %15s %15s %15s %15s %15s %15s'
            print(f%('ID','NAME','MOBILE','EMAIL ADDRESS','Dept ID','Designation','SALARY','DATE OF JOINING', 'Leave Status', 'Salary Status'))
            print('*'*160)
            for i in Rec:
                if i['ID']==ch.upper():
                    found+=1
                    for j in i.values():
                        print('%15s'% j,end='')
                    print()
            if found==0:
                print('Record not found')
            else:
                print('Total records displayed:',found)

    except FileNotFoundError:
        print(f,"File Doesn't exist")


# Search According to Name
def SearchName(f):
    try:
        with open(f,'rb')as fil:
            Rec=pickle.load(fil)
            found=0
            ch=input('Enter the Customer name to be searched: ')
            print('*'*160)
            f='%15s %15s %15s %15s %15s %15s %15s %15s %15s %15s'
            print(f%('ID','NAME','MOBILE','EMAIL ADDRESS','Dept ID','Designation','SALARY','DATE OF JOINING','Leave Status', 'Salary Status'))
            print('*'*160)
            for i in Rec:
                if i['NAME']==ch.upper():
                    found+=1
                    for j in i.values():
                        print('%15s'% j,end='')
                    print()
            if found==0:
                print('Record not found')
            else:
                print('Total records displayed:',found)

    except FileNotFoundError:
        print(f,"File Doesn't exist")
    except EOFError:
        print('Record not found')


# Gross salary function
def Debit(f):
    try:
        with open(f,'rb')as fil:
            Rec=pickle.load(fil)
            print('Please note gross salary is calculated on the basis of the following criteria:')
            print('1.HRA is 30% of Basic Salary')
            print('2.DA is 15% of Basic Salary')
            print('3.TAX deducted is 15% of (Basic+HRA+DA)')
            print('4.Total Gross Salary is:Basic +HRA+DA-TAX')
            ch=input('Continue(Y/N)')
            if ch=='y'or ch=='Y':
                f='%15s %15s %15s %15s %15s %15s %15s '
                print(f%('ID','NAME','Basic Salary','HRA','DA','TAX','GROSS SALARY'))
                for i in Rec:
                    HRA=round(30*i['Sal']/100,0)
                    DA=round(15*i['Sal']/100,0)
                    TAX=round(((i['Sal']+HRA+DA)*15/100),0)
                    GROSS=HRA+DA+i['Sal']-TAX
                    print(f%(i['ID'],i['NAME'],i['Sal'],HRA,DA,TAX,GROSS))
            else:
                print('Going to Main menu')

    except FileNotFoundError:
        print(f,"File Doesn't exist")



# Printing slip
def Slip(f):
    try:
        with open(f,'rb')as fil:
            Rec=pickle.load(fil)
            id=input("Enter Employe ID for slip: ")
            for i in Rec:
                if id.upper()==i['ID']:
                    if i['Salary_status']==0:
                        print("Salary is not paid. Hence slip cannot be given")
                        break
                    else:
                        print("Yes, the salary is paid, Generating slip........")
                        ch=input('Continue(Y/N)')
                        if ch=='y'or ch=='Y':
                            print('*'*160)
                            print("\n")
                            print("*******************Employee Salary Slip************************** ")
                            f='%15s %15s %15s %15s '
                            print(f%('ID','NAME','Basic Salary','Salary status'))
                            print()
                            print(f%(i['ID'],i['NAME'],i['Sal'],i['Salary_status']))

                        else:
                            print('Going to Main menu')

    except FileNotFoundError:
        print(f,"File Doesn't exist")


# Fucntion for counting employee
def Count(f):
    try:
        with open(f,'rb')as fil:
            Rec=pickle.load(fil)
            count=0
            for i in Rec:
                if i['ID']:
                    count+=1
        print("\n")
        print(f"************************Total number of currently active employees are : {count} ***********************")
        print("\n")
    

    except FileNotFoundError:
        print(f,"File Doesn't exist")


# Apply leave function
def Leave(f):
    try:
        with open(f,'rb+')as fil:
            found=0
            Rec=pickle.load(fil)
            A=input('Enter the Emp ID for which leave to be assigned: ')
            for p in Rec:
                if A==p['ID']:
                    found=1
                    if p['Leaves']==1:
                        print('Leaves already taken by the employee')   
                        break 
                    elif p['Leaves']==0:
                        p['Leaves']=1
                        print(f'Leave applied for Employee ID {A}')
                        break               
                
            if found==0:
                print('Employee details not found ')
            else:
                fil.seek(0)
                pickle.dump(Rec,fil)

    except EOFError:
        print('Records not found ')
    except FileNotFoundError:
        print(f,"Files Doesn't exist")


# Creating a file name 'Employee'
File='Employee'
while True:
    Menu()
    ch=input('Enter your choice: ')
    if ch=='1':
        Insert(File)
    elif ch=='2':
        SortAcc(File)
        Display(File)
    elif ch=='3':
        SortName(File)
        Display(File)
    elif ch=='4':
        SortDesig(File)
        Display(File)
    elif ch=='5':
        DisplayonDesig(File)
    elif ch=='6':
        Delete(File)
    elif ch=='7':
        Update(File)
    elif ch=='8':
        SearchID(File)
    elif ch=='9':
        SearchName(File)
    elif ch=='10':
        Leave(File)
    elif ch=='11':
        Debit(File)
    elif ch=='12':
        Slip(File)
    elif ch=='13':
        Count(File)
    elif ch=='14':
        print('Exciting....')
        quit(1)
    else:
        print('Wrong Choice Entered, Try again')
        
                    
                    
                
                
                
            

            

    

            
    
                
                    
                        
    
                
                        
    
            

            
        
                    
            
    
                
                    
                        
            
                    
                                    
        


            
    
