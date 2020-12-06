# function for registration in online store
def register(username, password, check_password):
    if password == check_password:
        if 8 < len(username) < 40 and 8 < len(password) < 14:
            print('Register finished successfully!')
            with open('database.txt', 'w') as db1:
                db1.write(username + '\n' + password)
                code = 1234
                return code
        else:
            print('Incorrect lenght of username or password!')
    else:
        print('Incorrect password')


# code for inputting the username and password, also code for inputting check_password
username = input('Please input your username: ')
password = input('Please input your password: ')
check_password = input('Please input your password again: ')
answer = register(username, password, check_password)


# function for checking code that returns from function register()
def check_code(guess, answer):
    if answer == guess:
        print('Success! You can log in!')
    else:
        print('Incorrect code!')
check_code(1234, answer)



# function for authorization in online store
def auth():
    username = input('Please input your username: ')
    password = input('Please input your password: ')
    db1 = open('database.txt')
    list_for_db1 = db1.readlines()
    for line in list_for_db1:
        line = line.strip()
        if username == line:
            if password == line:
                print(f'Welcome,', username)
                break
            else:
                print('Incorrect password! Please try again')
        else:
            print('Incorrect username! Please try again!')

auth()


# this is the list of products
products = ['Acer','ASUS razer','HP','hp zenbook','acer aspire','iphone x','Iphone PRO MAX','samsung galaxy','samsung TAB515',
            'Sony Ericson','nokia 3310', 'Nokia WIN','adata hdd1tb','ADATA SSD','Kingston 1tb','kiNGston ssd','GeForce RTX',
            'AMD','amd rx760','Intel HD','MacbOOk PRO','iMac','macbook air','lenovo','AMD','aMd ryzen']


# function for record the products and making them in the same condition(making the letters lower)
def record_products(products):
    with open('products.txt', 'w') as fproduct:
        for line in products:
            line = line.strip()
            line = line.lower()
            fproduct.write(line + '\n')

record_products(products)


# function for sorting the products to the different categories
def sort(option):
    with open('products.txt') as fproduct:
        list_of_product = fproduct.readlines()
        if option == 'phone':
            with open('phone.txt', 'w') as fphone:
                for line in list_of_product:
                    if 'iphone' in line or 'samsung' in line or 'sony' in line or 'nokia' in line:
                        fphone.write(line)
        elif option == 'computer':
            with open('computer.txt', 'w') as fcomputer:
                for line in list_of_product:
                    if 'acer' in line or 'asus' in line or 'hp' in line or 'mac' in line or 'lenovo' in line:
                        fcomputer.write(line)
        elif option == 'graphic card':
            with open('graphic.txt', 'w') as fgraphic:
                for line in list_of_product:
                    if 'geforce' in line or 'amd' in line or 'intel' in line:
                        fgraphic.write(line)
        elif option == 'hard drive':
            with open('hard.txt', 'w') as fhard:
                for line in list_of_product:
                    if 'adata' in line or 'kingston' in line:
                        fhard.write(line)
    print('Succesfully sorted!')


# function for inputting 'option' that you want to sort
def my_input():
    my_input = input('Please input what you want to sort: ')
    sort(my_input)

my_input()




