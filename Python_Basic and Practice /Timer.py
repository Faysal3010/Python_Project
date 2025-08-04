import time
week=day=hr=min=sec=0
while True:
    time.sleep(.1)
    sec+=1
    if(sec>59):
        sec=0
        min+=1
    elif(min>59):
        min=0
        hr+=1
    elif(hr>24):
        hr=0
        day+=1
    elif(day>7):
        day=0
        week+=1
    print(week,'week',day,'day',hr,'hour',min,'min',sec,'sec')