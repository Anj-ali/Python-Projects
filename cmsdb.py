#BLL
import pymysql
class Customer:
    con = pymysql.connect(host="localhost",user="root",password="xxxxxxx",database="xxxxxx")
    mycur=con.cursor()

    listCus = []
    def __init__(self):
        self.id = 0
        self.age = 0
        self.name = 0

    def addCustomer(self):
        Customer.listCus.append(self)
        qry="insert into cust values('%s','%s','%s')"%(self.id,self.age,self.name)
        Customer.mycur.execute(qry)
        Customer.con.commit()

    def searchCustomer(self):
        qry = "select * from cust where id='%s'" % (self.id)
        Customer.mycur.execute(qry)
        data = Customer.mycur.fetchone()
        return data

    def delCustomer(self,id):
        qry = "delete from cust where id='%s'" % (self.id)
        Customer.mycur.execute(qry)
        Customer.con.commit()

    def modifyCustomer(self):
        qry = "update cust set age = '%s', name = '%s' where id = '%s'" % (self.age,self.name,self.id)
        Customer.mycur.execute(qry)
        Customer.con.commit()

    def showCustomer(self):
        qry = "select * from cust"
        Customer.mycur.execute(qry)
        data = Customer.mycur.fetchall()
        return data

while(1):
    ch = input('''Enter 1 to 6 
                1 for add customer 
                2 for search customer 
                3 for delete customer 
                4 for modify customer 
                5 for display customer 
                6 for exit''')

    if(ch == "1"):              #Add Customer
        cus = Customer()
        cus.id = input("Enter customer id : ")
        cus.age = input("Enter customer age : ")
        cus.name = input("Enter customer name : ")
        cus.addCustomer()
        print("Customer added successfully")

    elif(ch == "2"):          #Search customer by id
        cus = Customer()
        cus.id = input("Enter Customer ID")
        data = cus.searchCustomer()
        print("Cust ID:", data[0], "Cust Name:", data[2], "Cust Age:", data[1])

    elif(ch == "3"):          #Delete Customer
        cus = Customer()
        cus.id = input("Enter customer id to delete : ")
        cus.delCustomer(id)
        print('Customer deleted successfully')

    elif(ch == "4"):    #Modify Customer
        cus = Customer()
        cus.id = input("Enter id ")
        cus.age = input("Enter age ")
        cus.name = input("Enter name ")
        cus.modifyCustomer()
        print("Customer updated successfully")


    elif (ch == "5"):  # Display
        cus = Customer()
        data = cus.showCustomer()
        print(data)

    elif(ch == "6"):     #Show Customer
        break

    else:
        print("Incorrect choice")
