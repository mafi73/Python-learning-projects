x=input('Adade 3 raghami vared konid? ')
x=int(x)
if x>=100 and x<1000:
    y=x//100 # sadgan adade aval #yekane adade dovom
    t=x//10
    z=t%10  # dahgan adade aval
    u=x%10  # yekan adade aval
    a=u*100 #sadgan adade dovom
    b=z*10  #dahgane adade dovom
    d=y+a+b #baraxe adade 3raghami
    e=d*2   #2barabare baraxe adade 3raghami
    print(d)
    print(e)
else:
    print('adad 3 raghami nist')



