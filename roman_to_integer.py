#Given a roman numeral, convert it to an integer.
s="LVIII"
convertor={
"I":"1","V":"5","X":"10","L":"50",
"C":"100","D":"500","M":"1000",
"IV":"4",
"IX":"9",
"XL":"40","XC":"90",
"CD":"400","CM":"900"}
answer=0
if "IV" in s:
    s=s.replace("IV","")
    answer+=4
if "IX" in s:
    s=s.replace('IX','')
    answer+=9
if "XL" in s:
    s=s.replace('XL','')
    answer+=40
if "XC" in s:
    s=s.replace('XC','')
    answer+=90
if "CD" in s:
    s=s.replace('CD','')
    answer+=400
if "CM" in s:
    s=s.replace('CM','')
    answer+=900

for i in s:

    answer+= int(convertor[i])
print (answer)     