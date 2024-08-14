code="jack and jill went up the hill"
for temp in code.split():
    if(temp.endswith("ill")):
        print("Count : ", code.count("ill"))
        break
code=code.replace("j","m")
for temp in code.split():
    if(len(temp)%2!=0):
        temp_string=(str)(temp)
        code=code.replace(temp_string,temp_string.upper())
print(code)            