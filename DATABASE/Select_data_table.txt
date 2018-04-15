	import pymysql;
	db = pymysql.connect("localhost","root","","anbu");
	cursor = db.cursor();
	sql=  "select * from ex3 where mob='9798'";
	try:
	   cursor.execute(sql);
	   results=cursor.fetchall();
	   for row in results:
       name=row[0];
       user=row[1];
       pass1=row[2];
       mob=row[3];
       print(name,user,pass1,mob);
	except:
       print("Error");
	db.close();
-----------------------------------------------------
