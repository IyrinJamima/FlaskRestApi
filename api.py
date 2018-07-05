#from flask import Flask
from flask import Flask, request, jsonify
#from flask_restful import Resource, Api
app = Flask(__name__)
import MySQLdb
connection = MySQLdb.connect(host="localhost", # The Host
                      user="root", # username
                      passwd="root", # password
                      db="customerprod") # name of the data base
cursor = connection.cursor()


@app.route('/prod',methods = ["GET"])
def prod():
    name = 'dress';
    productcode = 555;
    description = 'dress';
    price = 500;
    cursor.execute("insert into products (name, productcode, description, price) values ('"+ name +"'," + str(productcode) + ",'" + description +"'," + str(price) +")")
    connection.commit()
    return name

@app.route('/pro',methods = ["PUT"])
def update_prod():	
    prod_name = 'brush';
    prod_id = 10;	  
    update_brush = "update products set name = 'brush' where productcode = 555"
    cursor.execute(update_brush)
    return prod_name	

@app.route('/produ',methods = ["GET"])
def selectprod():
    name = 'dress';
    prodcts = cursor.execute("select * from products where name like '%s%' " )
    print(prodcts)
    connection.commit()
    return jsonify(prodcts)
	
@app.route('/product',methods = ["DELETE"])
def delet_prod():
    description = 'perfume';
    del_prod = ("delete from products where description = 'perfume' " )
    cursor.execute(del_prod)
    connection.commit()
    return description

if __name__ == '__main__':	
       app.run()
	
