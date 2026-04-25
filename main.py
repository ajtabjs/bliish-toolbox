from pick import pick
import requests
import sys
import requests
import logging

logging.basicConfig(level=logging.DEBUG)


tokenprompt = input("enter your bliish token (sb-prkqirdzadljdpkrvjvz-auth-token): ")


globalposts = "https://bliish.com/api/v1/posts"
bliips = "https://bliish.com/api/v1/bliips"

headers = {
    "cookie": f"sb-prkqirdzadljdpkrvjvz-auth-token={tokenprompt};",
    "origin": "https://bliish.com",
    "referer": "https://bliish.com"
}

postdata = {
    "body": "",
    "client_mutation_id": "ajs-bliishtoolbox"
}

bliip_data = {
    "handle": ""
}

def post():
    postdata["body"] = prompt
    response = requests.post(globalposts, json=postdata, headers=headers)
    print(response.text)

def bliip():
    response = requests.post(bliips, json=bliip_data, headers=headers)
    print(response.text)
options = ["1. make a post", "2. comment on a post", "3. bliip a user", "4. get posts from someone's wall (json response, no parsing yet :P)", "5. mass bliip a set of users", "6. exit"]
title = "welcome to bliish toolbox! made by aj"

option, index = pick(options, title)
print(option)
if index == 0:
    prompt = input("what do you want to post? ")
    post()
elif index == 2:
    bliipprompt = input("username to bliip? is rate limited lol: ")
    bliip_data["handle"] = bliipprompt
    bliip()
elif index == 1:    
    postid = input("post id to comment on? (obtained via url so https://blii.sh/p/QZQXftQz would be an example)")
    comment = input("thing to say: ")
    postdata["body"] = comment
    response = requests.post(f"https://bliish.com/api/v1/posts/{postid}/comments", json=postdata, headers=headers)
elif index == 3:
    walls = input("username to get posts from? ")
    response = requests.get(f"https://bliish.com/api/v1/profiles/{walls}/wall?fresh=1&limit=20", headers=headers)
    print(response.text)
elif index == 4:
    users = input("usernames to bliip? (comma separated no spaces): ")
    for user in users.split(","):
        bliip_data["handle"] = user.strip()
        bliip()
elif index == 5:
    sys.exit()