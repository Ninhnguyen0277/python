
for td in range(0,21):
    for tn in range(0,34):
        for tg in range(0,100):
            if(td+tn+tg==100 and 5*td+3*tn+tg/3==100):
                print(td,tn,tg)
