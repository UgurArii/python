import datetime as dt
# Class is used for all kinds of people.
import datetime as dt
# Base class is used for all kinds of Members.
class Member:
    """ The Member class attributes and methods are for everyone """
    # By default, a new account expires in one year (365 days)
    expiry_days = 365
    # Initialize a member object.
    def __init__(self, firstname, lastname):
        # Attributes (instance variables) for everybody.
        self.firstname = firstname
        self.lastname = lastname
        # Calculate expiry date from today's date.
        self.expiry_date = dt.date.today() + dt.timedelta(days=self.expiry_days)
        self.secret_code = ''
    def showxpriry(self):
        return f"{self.firstname} {self.lastname} expires on {self.expiry.date}"
Joee = Member('Joe','Anybody')
print(Joee.firstname)
print(Joee.lastname)
print(Joee.expiry_date)


class Admin(Member):
    expiry_days = 365.2422*100
    #Subclass parameter
    def __init__(self, firstname, lastname, secret_code):
        #pass Member parameteres on up to Member class
        super().__init__(firstname, lastname)
        #Assign the remainin paramater to this object
        self.secret_code = secret_code

class User(Member):
    pass


Ann = Admin('Annie','Angst','PRESTO')
print(Ann.firstname, Ann.lastname,Ann.expiry_date, Ann.secret_code)

Uli = User('Uli','Ungula')
print(Uli.firstname)
print(Uli.lastname)
print(Uli.expiry_date)
print(Uli.secret_code)

print(Ann.showxpriry())