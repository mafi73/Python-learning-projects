list=["This", "is", "an", "example", "of", "text", "justification."]
maxWidth=16
lines=[]#خطوط نهایی
current_line=[] #کلمات خط فعلی
current_lenght=0
for w in list:
    if current_lenght +len(w) + len(current_line) <= maxWidth:
        current_line.append(w)
        current_lenght += len(w)
    else:
        fazaha = maxWidth - current_lenght #koole fazahaye khali
        if len(current_line)==1: #فقط یک کلمه
            line=current_line[0]+(fazaha*' ')#
        else:
            fazaye_vasat = fazaha // (len(current_line)-1)#tedade faza bein kalamat
            space_namosavi=fazaha % (len(current_line)-1)#adad
            space= fazaye_vasat*' ' #tedad space ha
            line=space.join(current_line[:space_namosavi+1])+space+space.join(current_line[space_namosavi+1:])
        lines.append(line)
        current_lenght=len(w)
        current_line=[w]
final_line=' '.join(current_line)+ ' '*(maxWidth - len(' '.join(current_line)))
lines.append(final_line)
print (lines)