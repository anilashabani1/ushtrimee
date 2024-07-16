person = {
    "Emri": "Anila",
    "Mbiemri": "Shabani",
    "Shkolla": "ISP",
    "Titulli": "Nxenes",
    "Mosha":16
}
emri = person["Emri"]
print(emri)

x = person.get("emri")
print(x)

person ["Titulli"] = "Asistent"
print(person)

for i in person.values():
    print(i)
    
if "Shkolla" in person:
    print("Po eshte ne objekt")
else:
    print("Jo nuk eshte ne objekt")