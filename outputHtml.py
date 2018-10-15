# coding: utf-8
print("<h1>Head 1</h1>")
print("<p>test</p>", end="")
print("<p>幼児</p>")

print("<select name=\'age\'>")
for i in range(6):
    print("<option>" + str(i) + "才</option>")
print("</select>")