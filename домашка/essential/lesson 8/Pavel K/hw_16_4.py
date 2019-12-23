#  Создайте список товаров в интернет-магазине. Сериализуйте и сохраните его при помощи pickle и JSON.
import json
import pickle
shop_list = {
    'pickle':'50 jar',
    'bananas':'10 box',
    'milk':'50 bottle'
}
################json#################################

with open('D:\\random.txt', 'w') as k:
    json.dump(shop_list, k) # record to json

with open('D:\\random.txt', 'r') as k1:
    after_save = json.load(k) # reading from json

print(after_save)

####################pickle###########################

with open('D:\\data.pickle', 'wb') as pic:
    pickle.dump(shop_list, pic)

with open('D:\\data.pickle', 'rb') as pic2:
    after_save_p = pickle.load(pic2)

print(after_save_p)
