import pymysql;
db = pymysql.connect("localhost","root","","anbu");
cursor = db.cursor();
#sql = "create table excel(name varchar(30))";
sql=  "delete from ex3 where user='root'";
try:
   cursor.execute(sql);
   db.commit();
   print("Sucess");
except:
    db.rollback();
    print("Check");
db.close();
----------------------------------------------------
