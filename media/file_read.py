def file_read():
	with open('read.txt', 'r') as f:
		text = f.read()
		print(text)
		

file_read() 


def file_write():
	with open('write.txt', 'w') as f:
		f.write("This is write operation")
		
file_write()