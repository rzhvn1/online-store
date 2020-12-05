# function for authorization in online store
def auth(username, password, check_password):
    if password == check_password:
        if 8 < len(username) < 40 and 8 < len(password) < 14:
            print(f'Welcome, {username}!')
            with open('database.txt', 'w') as db1:
                db1.write(username + '\n' + password)
                code = 1234
                return code
        else:
            print('Incorrect lenght of username or password!')
    else:
        print('Incorrect password')

answer = auth('0headshot1', 'erjan02qwerty', 'erjan02qwerty')

# function for checking code that returns from function auth()
def check_code(guess, answer):
    if answer == guess:
        print('Success! You can log in!')
    else:
        print('Incorrect code!')

check_code(1234, answer)

# this is the list of products
products = ['Acer','ASUS razer','HP','hp zenbook','acer aspire','iphone x','Iphone PRO MAX','samsung galaxy','samsung TAB515',
            'Sony Ericson','nokia 3310', 'Nokia WIN','adata hdd1tb','ADATA SSD','Kingston 1tb','kiNGston ssd','GeForce RTX',
            'AMD','amd rx760','Intel HD','MacbOOk PRO','iMac','macbook air','lenovo','AMD','aMd ryzen']

def record_products(products):
    with open('products.txt', 'w') as fproduct:
        for line in products:
            fproduct.write(line + '\n')

record_products(products)


def sort(option):
    with open('products.txt') as fproduct:
        list_of_product = fproduct.readlines()
        if option == 'phone':
            with open('phone.txt', 'w') as fphone:
                for line in list_of_product:
                    if line == 'iphone x\n' or line == 'Iphone PRO MAX\n' or line == 'samsung galaxy\n' or line == 'samsung TAB515\n' or line == 'Sony Ericson\n' or line == 'nokia 3310\n' or line == 'NokiaWIN\n':
                        fphone.write(line)
        elif option == 'computer':
            with open('computer.txt', 'w') as fcomputer:
                for line in list_of_product:
                    if line == 'Acer\n' or line == 'Asus razer\n' or line == 'HP\n' or line == 'hp zenbook\n' or line == 'acer aspire\n' or line == 'MacbOOk PRO\n' or line == 'iMac\n' or line == 'macbook air\n' or line == 'lenovo\n':
                        fcomputer.write(line)
        elif option == 'graphic card':
            with open('graphic.txt', 'w') as fgraphic:
                for line in list_of_product:
                    if line == 'GeForce RTX\n' or line == 'amd rx760\n' or line == 'AMD\n' or line == 'Intel HD\n' or line == 'aMd ryzen\n':
                        fgraphic.write(line)
        elif option == 'hard drive':
            with open('hard.txt', 'w') as fhard:
                for line in list_of_product:
                    if line == 'adata hdd1tb\n' or line == 'ADATA SSD\n' or line == 'Kingston 1tb\n' or line == 'kiNGston ssd\n':
                        fhard.write(line)

def my_input():
    my_input = input('Please input what you want to sort: ')
    sort(my_input)


my_input()




