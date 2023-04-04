class Member:
    #Create a  member from uname and frame
    def __init__(self, uname, fname):
        #define attributes and give them values
        self.username = uname
        self.fullname = fname
        
this_instance_name = Member('uname', 'fname')

new_guy = Member('Rambo','Rocco Moe')
print(new_guy)
print(new_guy.username)
print(new_guy.fullname)
print(type(new_guy))