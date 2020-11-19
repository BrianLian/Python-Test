dict_student = {'sid': '9A417018', 'sname': 'Ian', 'age': '21'}

print(dict_student.keys())
print(dict_student.values())
print(dict_student.items())
print("\r\n")

print("印出dict內所有的(K,V)對應組合", end="\n\n")
print("方式1")
for (K, V) in dict_student.items():
    print("{} : {}".format(K, V))
print("方式2")
for key in dict_student:
    print("{} : {}".format(key, dict_student.get(key)))
print("\r\n")

print("更新資料 將sid改為8668")
dict_student.update({'sid': '99999999'})
for (K, V) in dict_student.items():
    print("{} : {}".format(K, V))

newList = []
for (K, V) in dict_student.items():
    newList.append("{} {}".format(K, V))

print(*newList)
print(",".join(newList))

field = ",".join(dict_student.keys())
value = ",".join(dict_student.values())
print(
    'insert into {} ({}) values ({});'
    .format("tableName", field, value)
)
