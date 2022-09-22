
items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

itemsL = []

if ruleKey == "type":
    for i in range(len(items)):
        if items[i][0] == ruleValue:
            itemsL.append(items[i][0])
elif ruleKey == "color":
    for i in range(len(items)):
        if items[i][1] == ruleValue:
            itemsL.append(items[i][1])
else:
    for i in range(len(items)):
        if items[i][2] == ruleValue:
            itemsL.append(items[i][2])

print(len(itemsL))