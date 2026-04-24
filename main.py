from pick import pick
import requests
import sys

globalposts = "https://bliish.com/api/v1/posts"
bliips = "https://bliish.com/api/v1/bliips"

postdata = {
    "body": "",
    "client_mutation_id": "ajs-bliishtoolbox"
}

bliip_data = {
    "handle": ""
}

tokenprompt = input("enter your bliish token (sb-prkqirdzadljdpkrvjvz-auth-token): ")
def post():
    postdata["body"] = prompt
    response = requests.post(globalposts, json=postdata, headers={"cookie": f"sb-prkqirdzadljdpkrvjvz-auth-token={tokenprompt};", "origin": "https://bliish.com", "referer": "https://bliish.com"})
    print(response.text)

def bliip():
    response = requests.post(bliips, json=bliip_data, headers={"cookie": f"sb-prkqirdzadljdpkrvjvz-auth-token={tokenprompt};", "origin": "https://bliish.com", "referer": "https://bliish.com"})
    print(response.text)
options = ["1. make a post", "2. bliip a user", "3. get posts from someone's wall", "4. mass bliip a set of users", "5. exit"]
title = "welcome to bliish toolbox! made by aj"

option, index = pick(options, title)
print(option)
if index == 0:
    prompt = input("what do you want to post? ")
    post()
elif index == 1:
    bliipprompt = input("username to bliip? is rate limited lol: ")
    bliip_data["handle"] = bliipprompt
    bliip()
elif index == 2:
    walls = input("username to get posts from? ")
    response = requests.get(f"https://bliish.com/api/v1/profiles/{walls}/wall?fresh=1&limit=20", headers={"cookie": f"sb-prkqirdzadljdpkrvjvz-auth-token={tokenprompt};", "origin": "https://bliish.com", "referer": "https://bliish.com"})
    print(response.text)
elif index == 3:
    users = input(" usernames to bliip? (comma separated no spaces): ")
    for user in users.split(","):
        bliip_data["handle"] = user.strip()
        bliip()
elif index == 4:
    sys.exit()