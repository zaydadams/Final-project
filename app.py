import sqlite3
from flask import Flask, request
from flask import jsonify


def init_sqlite_db():

    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, country TEXT, password TEXT)')
    print("Table created successfully")
    conn.close()


init_sqlite_db()


app = Flask(__name__)

@app.route('/')
@app.route('/registration-form/')
def enter_new_client():
    return jsonify('registration-form.html')


@app.route('/add-new-record/', methods=['POST'])
def add_new_record():
    if request.method == "POST":
        msg = None
        try:
            name = request.form['name']
            email = request.form['email']
            country = request.form['country']
            password = request.form['password']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO clients (name, email, country, password) VALUES (?, ?, ?, ?)", (name, email, country, password))
                con.commit()
                msg = name + " was successfully added to the database."
        except Exception as e:
            con.rollback()
            msg = "Error occurred in insert operation: " + str(e)

        finally:
            con.close()
            return jsonify('results.html', msg=msg)


@app.route('/show-records/', methods=["GET"])
def show_records():
    records = []
    try:
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM clients")
            records = cur.fetchall()
    except Exception as e:
        con.rollback()
        print("There was an error fetching results from the database: " + str(e))
    finally:
        con.close()
        return jsonify('records.html', records=records)


@app.route('/delete-clients/<int:clients_id>/', methods=["GET"])
def delete_clients(client_id):

    msg = None
    try:
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM clients WHERE id=" + str(client_id))
            con.commit()
            msg = "A record was deleted successfully from the database."
    except Exception as e:
        con.rollback()
        msg = "Error occurred when deleting a client in the database: " + str(e)
    finally:
        con.close()
        return jsonify('delete-success.html', msg=msg)


