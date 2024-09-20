list=["This", "is", "an", "example", "of", "text", "justification."]
maxWidth=16
list1=[]#خطوط نهایی
current_line=[] #کلمات خط فعلی
current_lenght=0
for w in list:
    if current_lenght +len(w) + len(current_line) < maxWidth:
        current_line.append(w)
        current_lenght+=len(w)
print (current_line)
        