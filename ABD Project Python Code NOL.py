# Niamh O'Leary  ID: G00376339
# Applied Databases Project 2020

# Running pymysql and connecting to database
import pymysql
import pymongo

conn = None

myClient = None

def connect():
    global conn
    conn = pymysql.connect("localhost", "root",
                            "root", "world",
                            cursorclass=pymysql.cursors.DictCursor)

def mongoConnect():
    global myClient
    myClient = pymongo.MongoClient()
    myClient.admin.command('ismaster') 

# 4.4.1     
def main():
    # Initialise array
    array = []

    display_menu()


    while True:
        choice = input("Enter choice: ")
            
        if (choice == "1"):
            View_People()
            display_menu()
        elif (choice == "2"):
            View_Countries_By_Independence_Year()
            display_menu()
        elif (choice == "3"):
            Add_New_Person()
            display_menu()
        elif (choice == "4"):
            View_Countries_By_Name()
            display_menu()
        elif (choice == "5"):
            View_Countries_By_Population()
            display_menu()
        elif (choice == "6"):
            Find_Students_By_Address()
            display_menu()
        elif (choice == "7"):
            Add_New_Course()
            display_menu()
        elif (choice == "x"):
            break;
        else:
            display_menu()



# Choice 1 (View People)

def View_People():
    print("Choice 1")
    cur = db.cursor()
    cur.execute("SELECT * FROM person")
    count = 0
    for row in cur.fetchall():
        print(row[0],row[1],row[2])
        if (count % 2 == 1):
            os.system("""bash -c 'read -s -n 1 -p "Press any key to continue or q to quit..."'""")
            print("\n")
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                print('You Pressed q Key!')
                break
        count +=1

    db.close()

# Choice 2 (View Countires by Independence Year)

def View_Countries_By_Independence_Year():
    print("Choice 2")
    print("Countries_By_Independence_Year")
    print("------------------------------")
    independence_year = input("Enter year:")
    cur = db.cursor()
    cur.execute("SELECT Name, Continent , IndepYear FROM country WHERE IndepYear = " + independence_year)  # using SQL
    for row in cur.fetchall(): 
        print(row[0],row[1],row[2])
    db.close()


# Choice 3 (Add new Person)  
def Add_New_Person():
    print("Choice 3")
    #to store duplicate name check for adding new people to database
    Duplicate_Name_Check = []
    
    print("Add_New_Person")
    cur = db.cursor()
    cur.execute("SELECT * FROM person")  # use SQL 
    for row in cur.fetchall():  # print 
        namecheck = row[1]

        Duplicate_Name_Check.insert(0, namecheck)

    db.close()

# 4 (View Countries by Name)

def View_Countries_By_Name():
    print("Choice 4")
    print("Countries_By_Name")
    print("------------------------------")

    if len(Countries_By_Name_Dictionary) == 0:
        print("Country Name")
                # you must create a Cursor object. It will let
        #  you execute all the queries you need
        cur = db.cursor()

        # Use all the SQL you like
        cur.execute("SELECT Name FROM country")
        # print all the first cell of all the rows
        for row in cur.fetchall():
            dictvalue = []
            Countries_By_Name_Dictionary[dictkey]=dictvalue #add key and list to dictionary
        db.close()

    country_name = input("Enter Country Name:")



# 5 (View Countries by population)
def View_Countries_By_Population):
    print("Choice 4")
    print("Countries_By_Population")
    print("------------------------------")

            cmp = input("Enter < > or = : ")
            # if user does not enter one of these, repeatedly asked until a valid choice is entered.
            while cmp not in("<",">",'='):
                cmp = input("Enter < > or = : ")
                if cmp in("<",">",'='):
                    break
            while True: 
                try:  
                    pop = int(input("Enter population :"))
                    break
                except ValueError:
                    print("Invalid population value, please enter a valid number...")
                    
                except Exception as e:
                    print(e)
            
                    
            countries = mysql_connect.getCountryData()
                
            print("Countries by Pop \n ----------------")
            for country in countries:
                # print country details
                
                if cmp ==">":
                    if int(country["Population"]) > int(pop):
                        print(country["Code"]," : ", country["Name"]," : ", country["Continent"]," : ",country["Population"])
                elif cmp =="=":
                    if int(country["Population"]) > int(pop):
                        print(country["Code"]," : ", country["Name"]," : ", country["Continent"]," : ",country["Population"])
                elif cmp =="<":
                    if int(country["Population"]) < int(pop):
                        print(country["Code"]," : ", country["Name"]," : ", country["Continent"]," : ",country["Population"])


# 6 (Find Students Address)

def Find_Students_By_Address():
    addressquery = input("Input Address:")
    print("RESULTS BY ADDRESS")
    collection  = db.docs
    # Make a query to list all the documents

    for doc in collection.find({"details.address":"" + addressquery + ""}): #find records by address

        #Print each document

        print(doc)

# 7 (Add New Course)

def Add_New_Course():

    ids = [] # create an empty list for IDs
    # iterate pymongo documents with a for loop
    for doc in mycol.find():
        # append each document's ID to the list
        ids += [doc["_id"]]

    print("Choice 7")
    print("Add New Course")
    print("--------------")
    
    _id = input("_id :")


    while _id in ids:
        print("*** ERROR ***: _id " + _id + " already exists")
        _id = input("_id :")
 
    name = input("Name :")
    level = int(input("Level :"))

    mylist = [
      { "_id" : _id, "name" : name, "level" : level},

    ]

    x = mycol.insert_many(mylist)

    print("Added " , x.inserted_ids , " to courses")

def display_menu():
    print("World DB")
    print("--------")
    print("MENU")
    print("====")
    print("1 – View People")
    print("2 – View Countries by Independence Year")
    print("3 – Add New Person")
    print("4 – View Countries by name")
    print("5 – View Countries by population")
    print("6 – Find Students by Address")
    print("7 – Add New Course")
    print("x – Exit application")

# References

# Code used in this project has been adapted from the following refernces
# https://github.com/g00387822
# https://pynative.com/python-mysql-insert-data-into-database-table/
# Course Code: 52553, Applied Databases G. Harrison, GMIT 2020.
# https://www.w3schools.com/python/python_mongodb_insert.asp
# https://github.com/angela1C
# https://github.com/shkyler
# https://github.com/G00364778
