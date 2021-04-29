import requests

url = "http://auth.popchat/cgi-bin/basic"
data = {"token": "MTYxOTY2NjU3NC4xOTU3OQ=="}

rs = requests.post(url, data=data)

print(rs.text)


# import socket
#
# url = "auth.popchat"
# print("IP:", socket.gethostbyname(url))
