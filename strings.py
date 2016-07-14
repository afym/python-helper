string_name_1 = "some string '"
string_name_2 = 'some string "'
string_name_3 = 'some string \''
string_name_4 = "some string \""

print(string_name_1, "\n")
print(string_name_2, "\n")
print(string_name_3, "\n")
print(string_name_4, "\n")

# accessing string's possition

string_name_5 = "sweet home"
print("From string value : ", string_name_5)
print("0 possition is : ", string_name_5[0])
print("5 possition is : ", string_name_5[5])
print("from abc string possition 2 is :", "abc"[2])

# some string functions

string_name_6 = "some abc"
print("len(some abc):", len(string_name_6))

# some string methods
print("some abc / lower is :", string_name_6.lower())
print("some abc / upper is :", string_name_6.upper())
print("some concat : " + "a" + " " + "b")
string_name_7 = "no" * 12
print("* operator in strings : ", string_name_7)

# conver objetc in string object
numeric_value = 18
print("Using str(): " + str(numeric_value) + " value")

# some formating
string_name_8 = "Hello {} {}"
print(string_name_8.format("Angel", "Ybarhuen"))
string_name_8 = "I {0} and {0} a lot with {1}"
print(string_name_8.format("playing", "java"))
print("format doesnt care about numbers : ", string_name_8.format(1, 2))
print("table example:", "|{1:9} | {1:8}|".format(1, 2))