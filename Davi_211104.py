print("Question 2 ************************")
dc={"nome":"davi","idade":12}
print("Question 3 ************************")
print(dc)
print("Question 4 ************************")
print(dc["nome"])
print("Question 5 ************************")
del dc["nome"]
print("Question 6 ************************")
print(dc)
print("Question 7 ************************")
dc["u"]=1
print("Question 8 ************************")
print(dc)
print("Question 9 ************************")
dc["f"]=2
dc["c"]=5
print("Question 10 ************************")
for item in dc.keys():
    print(item)
