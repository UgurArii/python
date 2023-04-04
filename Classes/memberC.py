import datetime as dt


class Member:
    #Create a new class member
    def __init__(self, username, fullname):
        #define att and give them values
        self.username = username
        self.fullname = fullname
        
        #default data_joined to today's date
        self.data_joined = dt.date.today()
        #set is active to True initially.
        self.is_active =True
        
    # Define methods as functions, use self for "this" object.
    def show_datejoined(self):
        return f"{self.fullname} joined on {self.date_joined:%m/%d/%y}"
    # Method to activate (True) or deactivate (False) account.
    def activate(self, yesno):
    #True for active, False to make inactive """
        self.is_active = yesno
new_guy = Member('Rambo','Rocco Moe')

#try out the date_joined method
print(new_guy.show_datejoined())
print(new_guy.is_active)
