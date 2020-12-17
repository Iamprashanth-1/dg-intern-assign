import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import pandas as pd
import cust

app=Flask(__name__)
df=pd.read_csv(r"D:\Software files\dg-intern-assign\RESTAPI\Northwind_database_csv\customers.csv")


@app.route("/")
def hello():
    return render_template("home1.html")

@app.route("/customers",methods=["GET", "POST"])
def customers():
    df=pd.read_csv(r"D:\Software files\dg-intern-assign\RESTAPI\Northwind_database_csv\customers.csv")
    cv=[]
    for i in df.columns:
        cv.append(i)
    #print(cv)
    mv=[]
    if request.method=="POST":
        re=request.form
        az=1
        for k,v in re.items():
            az=v
        for i in cv:
            mv.append(df[i][int(az)-1])
        jk=[]
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
        y=int(s[0])
        cv=[]
        for i in df.columns:
            cv.append(i)
        for i in cv:
            te.append(df[i][y-1])
        pe=[te]
       # print(te)

    return render_template('customers.html',bookie=pe)

@app.route('/cupdat',methods=["GET","POST"])
def cupdat():
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
        #print(df['ProductName'][66])
    return render_template("customers.html")
