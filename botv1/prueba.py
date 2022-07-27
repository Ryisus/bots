my_file = open("idestudiantes.txt", "r")
content = my_file.read()
content_list = str(content)[1:-1] 
print(content_list)#ya lol arregle
my_file.close()