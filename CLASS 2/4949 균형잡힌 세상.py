while True:
    text = input()
    
    if text == ".":
        break
     
    check = []
    result = "yes"
            
    for i in text:
        if i == "(" or i == "[":
            check.append(i)
        elif i == ")" or i == "]":
            if check == []:
                result = "no"
                break
            if i == ")" and check[-1] != "(":
                result = "no"
                break
            if i == "]" and check[-1] != "[":
                result = "no"
                break
            else:
                check.pop()
                
    if check != []:
        result = "no"
        
    print(result)