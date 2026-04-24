from pick import pick
import requests

globalposts = "https://bliish.com/api/v1/posts"

postdata = {
    "body": "",
    "client_mutation_id": "ajs-bliishtoolbox"
}

print("welcome!")

options = ["1. make a post", "2. bliip a user", "3. get posts from someone's wall", "4. exit"]

if index == 0:
prompt = input("what do you want to post?")
