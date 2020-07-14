import requests
import sys
from sys import argv

url = "https://notify-api.line.me/api/notify"
header = {"Authorization": "Bearer {}".format(argv[1])}
message = {"message": "\n\n {}{}\n\n".format(argv[2], argv[3])}
print(message)
result = requests.post(url, data=message, headers=header)
print(result)
