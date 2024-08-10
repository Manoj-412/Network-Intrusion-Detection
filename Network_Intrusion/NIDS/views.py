from django.shortcuts import render

# Create your views here.
def NTW(request):
    if (request.method=="POST"):
        data=request.POST
        index=int(data.get('textindex'))
        if ('buttonpredict' in request.POST):
            import pandas as pd
            path="Network_Intrusion/train_dataset.csv"  #change the directory
            data=pd.read_csv(path)
            inputs=data.drop('Label',axis=1)
            output=data['Label']

            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.8)

            from sklearn.naive_bayes import GaussianNB
            model=GaussianNB()
            model.fit(x_train,y_train)

            result=model.predict(x_test)[index]
            normal="Network instrusion is of Normal type"
            blackhole="Network instrusion is of Blackhole type"
            tcp="Network instrusion is of TCP-SYN type"
            portscan="Network instrusion is of PortScan type"
            diversion="Network instrusion is of Diversion type"
            overflow="Network instrusion is of Overflow type"
            if result==0:
                result=normal
            elif result==1:
                result=blackhole
            elif result==2:
                result=tcp
            elif result==3:
                result=portscan
            elif result==4:
                result=diversion
            else:
                result=overflow
            return render(request,'NTW.html',{'result':result})
    return render(request,'NTW.html')

