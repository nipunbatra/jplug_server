import web
import MySQLdb

 
 
urls = ("/jplug","upload"
		)
app = web.application(urls, globals())
db = web.database(dbn='mysql', db='jplug', user='root', pw='password')

 
class upload:
	def POST(self):
		data = str(web.data())
		[mac,timestamp,voltage,frequency,active_power,reactive_power,dummy]=data.split(",")
	
		try:
			sequence_id = db.insert('data', mac=mac,timestamp=int(timestamp),voltage=float(voltage),frequency=float(frequency),active_power=float(active_power),reactive_power=float(reactive_power))
			
		except Exception,e:
			print e
 
if __name__ == "__main__":
	app.run()
