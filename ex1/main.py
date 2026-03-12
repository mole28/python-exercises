from model import User

print("Hi")
all_users = User.get_user()
for i in all_users:
    print("User ID: " + str(i.id) + " Name: " + str(i.name))
    i.save()

    user_from_disk = User.load(i.id)

print("Name: " + user_from_disk.name)
print("Username: " + user_from_disk.username)