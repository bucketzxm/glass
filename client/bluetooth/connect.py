import bluetooth


def rfcomm_server_sdp():
	server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	
	port = 1
#	port = bluetooth.get_available_port(bluetooth.RFCOMM)
	server_sock.bind(("",port))
	server_sock.listen(1)

	print "listening on port %d "% port
	client_sock,address = server_sock.accept()
	print "Accepted connection from " , address
	data = client_sock.recv(1024)
	print "received [%s] " % data
	client_sock.close()
	server_sock.close()		
	
if __name__=="__main__":
	rfcomm_server_sdp()
	#test()
