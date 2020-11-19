var1 = 777777
var2 = "ggggggggggggggg"
var3 = [666, "opop"]

print(type(var1))
print(type(var2))
print(type(var3))
print("\r\n")

a_dict = {type(var1): var1, type(var2): var2, type(var3): var3}

print("印出各自的資料型態")
for key in a_dict:
    if key == int:
        print("{} is a integer".format(a_dict.get(key)))
    elif key == str:
        print("{} is a string".format(a_dict.get(key)))
    elif key == list:

        print("{} is a list".format(a_dict.get(key)))
print("\r\n")
