def register():
#Reading our file , 'r' means that the file should be opened in read mode (i.e. you will get an error if the file does not exist).
    db=open('file.txt','r')
    username=input("Register your Mail ID/Password:  ")
    password=input("Enter password: ")
#using for loop we split our file like a column  to check and print.
    for i in db:
        x=i.split(",")
        y=x[0]
#A regular expression (or RE) specifies a set of strings that matches it;
#the functions in this module let you check if a particular string matches a given regular expression
#(or if a given regular expression matches a particular string, which comes down to the same thing).
    import re
    terms=re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
# here y is x[0] i.e username in our data base. If its already exist we need to intimate.
    if y==username:
        print("username exist, restart: ")
        register()

    elif  re.fullmatch(terms,username):
        print("Valid email")

#our password need to check its within our limitaions
        if len(password)<=6 or len(password)>=12:
                    print("invalid password: not enough length")
                    register()

        elif not re.search("[!@#$%^&*]", password):
                    print("invalid password: special character not found")
                    register()

        elif not re.search("[0-9]", password):
                    print("invalid pasword: digit not found")
                    register()

        elif not re.search("[A-Z]", password):
                     print("invalid password:upper case not found")
                     register()

        elif not re.search("[a-z]", password):
                     print("invalid password:lower case not found")
                     register()
# 'a' is opening text file for appending text.
        else:
                     print("valid password")
                     db = open("file.txt", 'a')
                     db.write(username + ', ' + password + '\n')
                     home()

    else:
        print("Invalid email/username")
        register()

#Here during login we will check username exist or not , username and password matches or not from out database.
def access():
    db=open('file.txt','r')
    username = input("Enter mail id / username:  ")
    password = input("Enter password: ")
    c=[]
    d=[]
    for i in db:
        a=i.split(',')
        x=a[0].strip()
        c.append(x)
        y=a[1].strip()
        d.append(y)

    if username not in c:
        print("username not exist")
    elif password not in d:
        print("password not exist")
    elif c.index(username) == d.index(password):
        print('hi'+" "+username+" "+"login success")
    else:
        print("login mismatch")
        home()

# Here we retrive our password from database if someone forgets their password.
def retrivepassword():
    db = open('file.txt', 'r')
    username = input("Enter mail id / username:  ")
    for i in db:
            x=i.split(',')
    if x[0]==username:
        print("your mail-id/user name is :"+x[1])
        home()
    else:
        print("username not registered")
        home()

#Initial screen
def home(option=None):
    option = input("l for login|s for signup|f for forgetpassword: ")
    if option == "l":
        access()
    elif option == "s":
        register()
    elif option == "f":
        retrivepassword()
    else:
        print("please enter an option")
        home()


home()