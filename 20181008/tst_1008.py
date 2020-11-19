list_garage = ["Banz", "BMW", "Rolls-Royce"]
tuple_garage = ("Honda", "Toyota", "Nissan")

print("迴圈取出(會多一個字尾)", end='-----')
for s in list_garage:
    print(s, end=" >")
print()

print("類指標取出", end='-----')
print(*list_garage, sep=" >")
