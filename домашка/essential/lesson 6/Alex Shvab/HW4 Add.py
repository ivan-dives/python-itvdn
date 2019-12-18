def human(**kwargs):
    for kay, value in kwargs.items():
        print(f"{kay} is {value}")

alex = {"Firstname":"Alex", "Lastname":"Shvab", "Age":24, "Phone":"+38093*****42"}
print(human(**alex))