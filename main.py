import email.message
import smtplib
import os

# 設定寄件者
acc = "Your Mail Account"
password = "Your App Apssword"


def send_fun(msg, acc, password):
	server=smtplib.SMTP_SSL("smtp.gmail.com",465) #建立gmail連驗
	server.login(acc,password)
	server.send_message(msg)
	server.close() #發送完成後關閉連線

def read_file(filename, acc, password):
	msg_f = open(filename, "r")
	#建立訊息物件
	msg=email.message.EmailMessage()
	m = "<h3>表單內容</h3>\n"
	cnt = 0
	# creating msg
	msg["From"] = acc
	for msg_r in msg_f:
		if cnt == 0:
			print("\nsending to:\n"+msg_r+"\n\n")
			msg["To"] = msg_r.replace("\n", "")
			msg["Subject"]="你好"
			cnt += 1
		else:
			m += "<p>" + msg_r + "</p>"
	msg.add_alternative(m,subtype="html") #HTML信件內容
	print(msg)
	print(m)
	print("\n\nfinish\n\n")
	send_fun(msg, acc, password)
	msg_f.close()

# 讀取文件(.csv)
def get_info():
	# store
	lis = ""
	res = []
	# open file
	fin = open("yourfile.csv", "r")
	# print index
	for lis in fin:
		lis = lis.replace("\n", "").split(",")
		# print(lis, "\n\n\n\n")
		res.append(lis)
	# close the file
	fin.close()
	# retuen
	return res

# 把文件轉換成Html格式
def trans_main():
	info = get_info()
	qes = info[0]
	cnt = 0
	tmp_name = ""
	for i in info:
		if cnt == 0:
			cnt+=1
			continue
		else:
			# write in 00_filename
			fname = open("00_filename.txt", "a")
			tmp_name = str(cnt) + ".txt"
			fname.write(tmp_name+"\n")
			mail = open(tmp_name, "a")
			c = 0
			for j in i:
				if c == 0:
					c+=1
					continue
				elif c == 1:
					mail.write(j)
				else:
					mail.write("\n")
					mail.write(qes[c])
					mail.write("\n")
					if str(j) == "":
						mail.write("none")
					else:
						mail.write(j)
				c+=1
			mail.close()
		fname.close()
		cnt+=1

# main function
def main(acc, password):
	trans_main()
	filename = open("00_filename.txt", "r")
	for name in filename:
		name = name.replace("\n", "")
		read_file(name, acc, password)
	filename.close()

# 刪除產生的文件
def rm_txt():
	# remove
	filename = open("00_filename.txt", "r")
	for name in filename:
		os.remove(name.replace("\n", ""))
	filename.close()
	os.remove("00_filename.txt")



main(acc, password)
rm_txt()
