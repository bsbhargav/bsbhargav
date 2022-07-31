#import Admin1 
# User 
# menu_list = {'Email': {'Full_Name': 'Bhargav', 'Phone_no': 8618698304, 'Address': 20, 'Password': 9698}}
class Food_delivery :
      login_info = {}
      def __init__(self,name,Email,address,phone_no,password):
          self.name = name
          self.Email = Email
          self.address = address
          self.phone_no = phone_no
          self.password = password
          Food_delivery.login_info[self.email] ={'Full_Name':self.name,
                                               'Email':self.Email,
                                               'Address':self.address,
                                               'Phone_no':self.phone_no,
                                               'Password':self.password,
                                               }
          self.order_items = {}

# 1:{'foodId':1,'Name':'Tandoori Chicken','Quantity':4,'Price':240,'Discount':4,'Stock':20}

      def place_new_order(self):
          print("What you want to order here in at the Restaurent ")
          add.show_menu_item()
          choice_user = int(input("If you want to order then select 1.YES  2.NO"))
          if choice_user == 1:
              n=int(input("How many Item do You Want to Order "))
              total_bill=0
              total_discount=0
              for i in range(n):
                  itemid = int(input("Enter the Item id here: "))
                  quan = int(input("Enter the quantity of the item: "))
                  total_bill = total_bill + add.menu_list[itemid]['Price'] * quan
                  total_discount += add.menu_list[itemid]['Discount']
                  add.menu_list[itemid]['Stock'] = add.menu_list[itemid]['Stock']-quan
# Add Item in User List
                  self.order_history[itemid] = {
                      "Name": add.menu_list[itemid]["Name"],
                      "Price": add.menu_list[itemid]["Price"],
                      "Quantity": quan
                  }
              again_ask = input("Confirmed ?? Yes Otherwise NO ")
              if again_ask == 'Yes':
                  print(f"Total Discount Allowed is {total_discount} ")
                  print(f"After Deduced Discount It costs is {total_bill-total_discount} INR in total")
                  print("You're order is successfully placed...")

              elif again_ask=="No":
                  print("Your Order has Cancelled Now...")
                  self.order_history.clear()

              else :
                  print("Invalid Input")

          elif choice_user == 2:
              print("You Selected 2 option So we Cancelled This....")

          else:
              print(" Invalid no ")


      def order_history_see(self):
        print(self.order_history)


      def update_profile(self):
          print("Update Profile Here")
          email=input("Enter Your Mail-id ")
          if email in Food_delivery.login_info.keys():
              print("Email Matched 1")
              del Food_delivery.login_info[email]

# update
              new_name=input("Enter new  Name ")
              new_email = input("Enter new  Email ")
              new_address= int(input("Enter Address "))
              new_phone_no = input("Enter new  Phone_no ")
              new_password = input("Enter new  Password ")

              Food_delivery.login_info[self.email] ={'Full_Name':self.name,
                                               'Email':self.Email,
                                               'Address':self.address,
                                               'Phone_no':self.phone_no,
                                               'Password':self.password,
                                               }
              print("Profile Updated Successfully")

          else :
              print("Email not Registered Please Try Again  ")

      @classmethod
      def login(cls, email, password):
          if  email in cls.login_info.keys():
              if cls.login_info.get(email)['Password'] == password:
                 print(f"logged in * Successfully * {cls.login_info.get(email)['Full_Name']}")
                 return True
              else:
                 print("Not valid These are the Wrong Credentials")
                 return False
          else:
              print(f"email Not Registered.. First Register email and try Again")
              return False


# Testing
"""obj=Food_delivery('Bhargav', 'Bhargavbs123' ,BS_96, '8618698304', '9698')
obj.print_profile()"""


def check_user(self, email, password):
    if email in Food_delivery.login_info.keys():
        if Food_delivery.login_info[email]['Password'] == password:
            print("Now...  You are Loggedin  ")
        else:
            print("Password not matched")
    else:
        print(f"email Not Registered.. First Register email and try Again")
