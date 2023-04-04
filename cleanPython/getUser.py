users = [{"first_name":"Helen", "age":39},
         {"first_name":"Buck", "age":10},
         {"name":"anni", "age":9}
        ]

def get_user_name(user):
    return users["first_name"].lower
def get_sorted_dictionary(users):
    if not isinstance(users, dict):
        raise ValueError("Not a correct dictionary")
    if not len(users):
        raise ValueError("Empty dictionary")
    users_by_name = sorted(users, key=get_user_name)
    return users_by_name


print(get_sorted_dictionary(users))