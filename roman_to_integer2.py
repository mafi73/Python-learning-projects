#Given a roman numeral, convert it to an integer.
#راه دوم٫با متد ایندکس ها و کد تمیز تر
s="LVIII"
convertor={
"I":"1","V":"5","X":"10","L":"50",
"C":"100","D":"500","M":"1000",
"IV":"4",
"IX":"9",
"XL":"40","XC":"90",
"CD":"400","CM":"900"}
answer=0
i=0

while (i<len(s)):
    if s[i:i+2] in convertor:
        answer+=int(convertor[s[i:i+2]])
        i+=2
    else:
        answer += int(convertor[s[i]])
        i += 1
print (answer)     