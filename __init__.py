from flask import Flask,render_template,request, redirect, url_for, session
from Forms import CreateUserForm,CreateCustomerForm,CreateLoginForm,createCompanyForm
import shelve, User, Customer

app=Flask(__name__)
app.secret_key = "12345"

@app.route('/')
def home():
    """
    user=shelve.open('user.db')
    customer=shelve.open('customer.db')
    try:
        print(user['Users'])
        print(customer['Customers'])
    finally:
        user.close()
        customer.close()
    """
    return render_template('home.html')

@app.route('/login', methods=["GET","POST"])
def login():
    session.clear()
    error=None
    login_form=CreateLoginForm(request.form)
    if request.method=='POST' and login_form.validate():
        users_dict={}
        db=shelve.open('user.db','c')
        users_dict=db['Users']
        print(users_dict)
        db.close()

        userList=[]
        for key in users_dict:
            user=users_dict[key]
            if login_form.userID.data==user.get_first_name() and login_form.userPwd.data==user.get_last_name():
                print("found")
                session['loginUser']=user.get_user_id()
                return redirect(url_for('home'))
            else:
                error="Invalid login credentials"

    return render_template('login.html', form=login_form, error=error)

@app.route('/createCompanyInfo')
def create_company():
    create_company_form=createCompanyForm(request.form)
    return render_template('createCompany.html',form=create_company_form)

@app.route('/contactUS')
def contact_us():
    return render_template('contactUS.html')

@app.route('/createUser',methods=['GET','POST'])
def create_user():
    create_user_form=CreateUserForm(request.form)
    if request.method=='POST' and create_user_form.validate():
        users_dict={}
        db=shelve.open('user.db','c')

        try:
            users_dict=db['Users']
            for user in users_dict:
                print(user.get_user_id(),user.get_first_name())
        except:
            print("Error in retrieving users from user.db")

        user=User.User(create_user_form.first_name.data,create_user_form.last_name.data, create_user_form.gender.data,
                       create_user_form.membership.data, create_user_form.remarks.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        """
        # Test codes
        users_dict = db['Users']
        user = users_dict[user.get_user_id()]
        print(user.get_first_name(), user.get_last_name(), "was stored in user.db successfully with user_id ==", user.get_user_id())
        db.close()
        """

        return redirect(url_for('retrieve_users'))
    return render_template('createUser.html',form=create_user_form)

@app.route('/createCustomer', methods=['GET', 'POST'])
def create_customer():
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'c')

        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")

        customer = Customer.Customer(create_customer_form.first_name.data, create_customer_form.last_name.data,
                                     create_customer_form.gender.data, create_customer_form.membership.data,
                                     create_customer_form.remarks.data, create_customer_form.email.data,
                                     create_customer_form.date_joined.data,
                                     create_customer_form.address.data, create_customer_form.contactby.data)
        print(customer.get_contactby())
        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        db.close()

        return redirect(url_for('retrieve_customers'))
    return render_template('createCustomer.html', form=create_customer_form)

@app.route('/retrieveUser')
def retrieve_users():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('retrieveUser.html', count=len(users_list), users_list=users_list)

@app.route('/retrieveCustomers')
def retrieve_customers():
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()

    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        print(customer.get_contactby())
        customers_list.append(customer)

    return render_template('retrieveCustomers.html', count=len(customers_list), customers_list=customers_list)

@app.route('/updateUser/<int:id>/', methods=['GET','POST'])
def update_user(id):
    update_user_form=CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_gender(update_user_form.gender.data)
        user.set_membership(update_user_form.membership.data)
        user.set_remarks(update_user_form.remarks.data)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_users'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.gender.data = user.get_gender()
        update_user_form.membership.data = user.get_membership()
        update_user_form.remarks.data = user.get_remarks()

        return render_template('updateUser.html',form=update_user_form)

@app.route('/accountInfo', methods=['GET','POST'])
def myaccount_info():
    update_user_form=CreateUserForm(request.form)
    id=session.get('loginUser')
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_gender(update_user_form.gender.data)
        user.set_membership(update_user_form.membership.data)
        user.set_remarks(update_user_form.remarks.data)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_users'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.gender.data = user.get_gender()
        update_user_form.membership.data = user.get_membership()
        update_user_form.remarks.data = user.get_remarks()

        return render_template('updateUser.html',form=update_user_form)

@app.route('/updateCustomer/<int:id>/', methods=['GET','POST'])
def update_customer(id):
    update_customer_form=CreateCustomerForm(request.form)
    if request.method == 'POST' and update_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']

        customer = customers_dict.get(id)
        customer.set_first_name(update_customer_form.first_name.data)
        customer.set_last_name(update_customer_form.last_name.data)
        customer.set_gender(update_customer_form.gender.data)
        customer.set_membership(update_customer_form.membership.data)
        customer.set_remarks(update_customer_form.remarks.data)
        customer.set_address(update_customer_form.address.data)
        customer.set_date_joined(update_customer_form.date_joined.data)
        customer.set_email(update_customer_form.email.data)
        customer.set_contactby(update_customer_form.contactby.data)

        db['Customers'] = customers_dict
        db.close()

        return redirect(url_for('retrieve_customers'))
    else:
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        update_customer_form.first_name.data = customer.get_first_name()
        update_customer_form.last_name.data = customer.get_last_name()
        update_customer_form.gender.data = customer.get_gender()
        update_customer_form.membership.data = customer.get_membership()
        update_customer_form.remarks.data = customer.get_remarks()
        update_customer_form.email.data=customer.get_email()
        update_customer_form.address.data=customer.get_address()
        update_customer_form.date_joined.data=customer.get_date_joined()
        update_customer_form.contactby.data=customer.get_contactby()

        return render_template('updateCustomer.html',form=update_customer_form)

@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
    users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()

    return redirect(url_for('retrieve_users'))

@app.route('/deleteCustomer/<int:id>', methods=['POST'])
def delete_customer(id):
    customers_dict = {}
    db = shelve.open('customer.db', 'w')
    customers_dict = db['Customers']

    customers_dict.pop(id)

    db['Customers'] = customers_dict
    db.close()

    return redirect(url_for('retrieve_customers'))

if __name__=='__main__':
    app.run()
