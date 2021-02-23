from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

db =
@app.route('/')
def home():
   return render_template('landing.html')

@app.route('/enternew')
def new_client():
   return render_template('landing.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         em = request.form['email']
         fm = request.form['full_name']
         un = request.form['user_name']
         p = request.form['password']

         with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO clients (email,full_name,user_name,password)
               VALUES (em,fm,un,p) )

            con.commit()
            msg = "sign up succesfully"
      except:
         con.rollback()
         msg = "error in insert operation"

      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from clients")

   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
