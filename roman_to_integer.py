s="XL"
convertor={
'I':'1',"V":"5","X":"10","L":"50",
"C":"100","D":"500","M":"1000",
"IV":"4",
"IX":"9",
"XL":"40","XC":"90",
"CD":"400","CM":"900"}
answer=0
if "XL" in s:
    s.replace('XL','')
    answer+=40
if "XC" in s:
    s.replace('XC','')
    answer+=90
if "CD" in s:
    s.replace('CD','')
    answer+=400
if "CM" in s:
    s.replace('CM','')
    answer+=900

for i in s:

    answer+= int(convertor[i])
print (answer)     