def human(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")

alex = {"Firstname":"Alex", "Lastname":"Shvab", "Age":24, "Phone":"+38093*****42"}
print(human(**alex))