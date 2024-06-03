class User:
    def __init__(self,id,name,age,is_admin):
        self.id = id
        self.name = name
        self.age = age
        self.is_admin = is_admin

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, age={self.age}, is_admin ={self.is_admin})"

def view_profile(user_id):
    profile = fetch_profile_from_database(user_id)
    if profile:
        return profile
    else:
        return "Profile Not Found"

def fetch_profile_from_database(user_id):
    return User(user_id, 'John', 43, False)

print(view_profile(14))