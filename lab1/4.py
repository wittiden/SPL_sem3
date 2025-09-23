text = "Never look back"
newText = {}
for i in text:
    
    if i == " ":
        continue

    newText[i] = text.count(i)
print(newText)