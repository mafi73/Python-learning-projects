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
        if len(current_line)==1: #تک کلمه ای
            line=current_line[0]+(fazaha*' ')#
        else:
            fazaye_vasat = fazaha // (len(current_line)-1)#tedade faza bein kalamat
            space_namosavi=fazaha % (len(current_line)-1)#adad
            space= fazaye_vasat*' ' #tedad space ha
            strline=''
            for i in range(len(current_line)-1):
                strline += current_line[i]
                if i < space_namosavi:
                    strline += ' ' *((fazaye_vasat)+1)#ezafe kardan faza ezafe be samte chap tar
                else:
                    strline += ' '*fazaye_vasat
            strline += current_line[-1] #ezafe kardan kalame akhar bedone space
        lines.append(strline)
        current_lenght=len(w)
        current_line=[w]
final_line=' '.join(current_line)+ ' '*(maxWidth - len(' '.join(current_line)))
lines.append(final_line)
print (lines)