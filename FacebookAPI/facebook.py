import requests
import json

url = "https://graph.facebook.com/v14.0/me?fields=id%2Cname&access_token=EAAp4yIylZAs0BAI0nke1ntTqgJ3ZAIOfeZC09niQYRcQrkWjB2PSfZCk805eZBA67wcSWCeNDp5p6f9HYbDAzlfcm2HUNh1PLV1lXC87GrHdVYmVLrYiHWw7Gwjx1hSRFHXF3ZAGQsuTKvX4vIOm1qsVy09VZAcxbvMF6q3EJgkp6NXyBPLhKF2g7NbfCkvu2BcEmFeZCSlTGYSvMybja44GQomf9TZBwQ6l2t78QlHAuVeHFkmvDNLez"
response = requests.get(url)
print(response)
print(response.content)
# ALWAYS var.content to output actual INFO Not only 200
