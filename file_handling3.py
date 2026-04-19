class Expense:
    def store_in_file(self):
        amt=input('Enter amount:')
        category=input('Enter category:')
        date=input('Enter date:')
        with open('expense.txt','a') as f:
            f.write(f"{amt},{category},{date}\n")
    def view_expense(self):
        total=0
        with open('expense.txt','r') as k:
            data=k.readlines()
            for i in data:
                a,c,d=i.strip().split(',')
                a=int(a)
                total+=a
                print(f"{a}-{c}-{d}")
            print(f'Total expense:{total}\n')
    def category(self):
        food_lst=[]
        travel_lst=[]
        shopping_lst=[]
        with open('expense.txt','r') as l:
            d=l.readlines()
            for i in d:
                a,c,date=i.strip().split(',')
                if 'food' in c:
                    food_lst.append(i)
                elif 'travel' in c:
                    travel_lst.append(i)
                elif 'shopping' in c:
                    shopping_lst.append(i)
                else:
                    print('Category not found.')
        print("\nFOOD:")
        for i in food_lst:
            print(i.strip())
        print("\nTRAVEL:")
        for i in travel_lst:
            print(i.strip())
        print("\nSHOPPING:")
        for i in shopping_lst:
            print(i.strip())

ob1=Expense()
ob2=Expense()
ob3=Expense()
ob4=Expense()
ob5=Expense()
ob6=Expense()
ob1.store_in_file()
ob2.store_in_file()
ob3.store_in_file()
ob4.store_in_file()
ob5.store_in_file()
ob6.store_in_file()
ob1.view_expense()
ob1.category()