import requests
import contacts
from streaming import StreamingServer

ip = "192.168.1.3"
port = 8000
server = "http://192.168.1.3:5555"
data = requests.get(server+"/clients").json()
streamingserver = StreamingServer(ip, port, data)
streamingserver.start_server()
ui = contacts.ContactApp(data, streamingserver)
ui.mainloop()
streamingserver.stop_server()

