def min_to_hr(a,b): 
    #b=True代表是地球時間一小時60分鐘,b=False 則為火星時間一小時70分鐘

    if bool(b)==True:
        hr=a/60
    else:
        hr=a/70

    return(hr)



x=min_to_hr(350,False)
print(x)
