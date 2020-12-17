import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import pandas as pd

app=Flask(__name__)
df=pd.read_csv(r"D:\Software files\dg-intern-assign\RESTAPI\Northwind_database_csv\products.csv")


@app.route("/")
def hello():
    return render_template("home1.html")
@app.route("/home",methods=["GET", "POST"])
def hellos():
    return render_template("home1.html")

@app.route("/products",methods=["GET", "POST"])
def products():
    df=pd.read_csv(r"D:\Software files\dg-intern-assign\RESTAPI\Northwind_database_csv\products.csv")
    cv=[]
    for i in df.columns:
        cv.append(i)
    #print(cv)
    mv=[]
    if request.method=="POST":
        re=request.form
        jk=[]
        if re:
            for k,v in re.items():
                az=v
            for i in cv:
                mv.append(df[i][int(az)-1])

            for i in range(len(cv)):
                jk.append({cv[i]:mv[i]})
            print(jk)
    return render_template("products.html",result=jk)
@app.route("/insert", methods=["POST",'GET'])
def insert():
    if request.method=="POST":
        res=request.form
        l=[]
        for key,value in res.items():
            l.append(value)
        from csv import writer
        def append_list_as_row(file_name, list_of_elem):
            with open(file_name, 'a+', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(list_of_elem)
        print(l)
        append_list_as_row(r"D:\Software files\dg-intern-assign\RESTAPI\Northwind_database_csv\products.csv",l)

    return render_template("products.html")
@app.route("/selecte",methods=["GET","POST"])
def selecte():
    if request.method =="POST":
        reqs=request.form
        s=[]
       # print(reqs)
        for key,value in reqs.items():
            s.append(value)
            #print(s)
        te=[]
        y=int(s[0])
        cv=[]
        for i in df.columns:
            cv.append(i)
        for i in cv:
            te.append(df[i][y-1])
        pe=[te]
       # print(te)

    return render_template('products.html',booki=pe)

@app.route('/updat',methods=["GET","POST"])
def updat():
    if request.method=="POST":
        re=request.form
        l=[]
        for key,value in re.items():
           l.append(value)
        cv=[]
        for i in df.columns:
            cv.append(i)
        import csv
        for i in range(len(cv)):
            df[str(cv[i])][int(l[0])-1]=l[i]
            #print(df[str(cv[i])][int(l[0])-1])
        print(df['ProductName'][66])
    return render_template("products.html")

#customers code
dfc=pd.read_csv(r"D:\Software files\dg-intern-assign\RESTAPI\Northwind_database_csv\customers.csv")
@app.route("/customers",methods=["GET", "POST"])
def customers():
    dfc=pd.read_csv(r"D:\Software files\dg-intern-assign\RESTAPI\Northwind_database_csv\customers.csv")
    cv=[]
    for i in dfc.columns:
        cv.append(i)
    #print(cv)
    mv=[]
    if request.method=="POST":
        re=request.form
        az=''
        jk=[]
        if re:
            for k,v in re.items():
                az=v
            kk=0
            print(az)
            if re:
                for i in dfc['CustomerID']:
                    if az!=i:
                        kk+=1
                    # print(az,i)
                    else:
                        break
            for i in cv:
                mv.append(dfc[i][int(kk)])
            print(mv)
            for i in range(len(cv)):
                jk.append({cv[i]:mv[i]})
            print(jk)
    return render_template("customers.html",result=jk)
@app.route("/insertc", methods=["POST",'GET'])
def insertc():
    if request.method=="POST":
        res=request.form
        l=[]
        for key,value in res.items():
            l.append(value)
        from csv import writer
        def append_list_as_row(file_name, list_of_elem):
            with open(file_name, 'a+', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(list_of_elem)
        print(l)
        append_list_as_row(r"D:\Software files\dg-intern-assign\RESTAPI\Northwind_database_csv\customers.csv",l)

    return render_template("customers.html")
@app.route("/cselecte",methods=["GET","POST"])
def cselecte():
    if request.method =="POST":
        reqs=request.form
        s=[]
       # print(reqs)
        for key,value in reqs.items():
            s.append(value)
            #print(s)
        te=[]
        y=str(s[0])
        cv=[]
        for i in dfc.columns:
            cv.append(i)
        kk=0
        for i in dfc['CustomerID']:
            if y==i:
                break
            else:
                kk+=1
        for i in cv:
            te.append(dfc[i][kk])
        pe=[te]
        #print(te)

    return render_template('customers.html',bookie=pe)

@app.route('/cupdat',methods=["GET","POST"])
def cupdat():
    if request.method=="POST":
        re=request.form
        l=[]
        for key,value in re.items():
           l.append(value)
        cv=[]
        print(l)
        for i in dfc.columns:
            cv.append(i)
        kk=0
        y=''.join(l[0].strip())
        for j in dfc['CustomerID']:
            j=''.join(j.strip())
            if y==j:
                break
            else:
                kk+=1
        import csv
        #print(cv,kk)
        for i in range(len(cv)-1):
            dfc[cv[i]][kk]=l[i]
            #print(df[str(cv[i])][int(l[0])-1])
        #print(df['ProductName'][66])
    return render_template("customers.html")


################################################################
##Orders

dfo=pd.read_csv(r"D:\Software files\dg-intern-assign\RESTAPI\Northwind_database_csv\orders.csv")

@app.route("/orders",methods=["GET", "POST"])
def orders():
    dfo=pd.read_csv(r"D:\Software files\dg-intern-assign\RESTAPI\Northwind_database_csv\orders.csv")
    cv=[]
    for i in dfo.columns:
        cv.append(i)
    #print(cv)
    mv=[]
    if request.method=="POST":
        re=request.form
        jk=[]
        if re:
            az=10248
            for k,v in re.items():
                az-=int(v)
            for i in cv:
                mv.append(dfo[i][abs(az)])

            for i in range(len(cv)):
                jk.append({cv[i]:mv[i]})
        print(jk)
    return render_template("orders.html",result=jk)
@app.route("/inserto", methods=["POST",'GET'])
def inserto():
    if request.method=="POST":
        res=request.form
        l=[]
        for key,value in res.items():
            l.append(value)
        from csv import writer
        def append_list_as_row(file_name, list_of_elem):
            with open(file_name, 'a+', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(list_of_elem)
        print(l)
        append_list_as_row(r"D:\Software files\dg-intern-assign\RESTAPI\Northwind_database_csv\orders.csv",l)

    return render_template("orders.html")
@app.route("/oselecte",methods=["GET","POST"])
def oselecte():
    if request.method =="POST":
        reqs=request.form
        s=[]
       # print(reqs)
        for key,value in reqs.items():
            s.append(value)
            #print(s)
        te=[]
        y=int(s[0])-10248
        cv=[]
        for i in dfo.columns:
            cv.append(i)
        for i in cv:
            te.append(dfo[i][y])
        pe=[te]
       # print(te)

    return render_template('orders.html',bookies=pe)

@app.route('/oupdat',methods=["GET","POST"])
def oupdat():
    if request.method=="POST":
        re=request.form
        l=[]
        for key,value in re.items():
           l.append(value)
        cv=[]
        for i in dfo.columns:
            cv.append(i)
        import csv
        for i in range(len(cv)):
            dfo[str(cv[i])][int(l[0])-1]=l[i]
            #print(df[str(cv[i])][int(l[0])-1])
        #print(df['ProductName'][66])
    return render_template("orders.html")

############################################
### Order history

@app.route("/view",methods=["GET", "POST"])
def view():
    dfv=pd.read_csv(r"D:\Software files\dg-intern-assign\RESTAPI\Northwind_database_csv\order-details.csv")
    cv=[]
    for i in dfv.columns:
        cv.append(i)
    #print(cv)
    mv=[]
    if request.method=="POST":
        re=request.form
        jk=[]
        if re:
            az=10248
            for k,v in re.items():
                az-=int(v)
            for i in cv:
                mv.append(dfv[i][abs(az)])

            for i in range(len(cv)):
                jk.append({cv[i]:mv[i]})
        print(jk)
    return render_template("view.html",result=jk)


if __name__ == "__main__":
    app.run(debug=True)