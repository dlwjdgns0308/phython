url = "http://naver.com"
pas = url.replace("http://", "")
n = pas.index(".")
passw = pas[:n]
pas1 = passw[:3]
pas2 = len(passw)
pas3 = passw.count("e")
print(str(pas1) + str(pas2) + str(pas3) + "!")