from pick import pick
import requests

globalposts = "https://bliish.com/api/v1/posts"

postdata = {
    "body": "",
    "client_mutation_id": "ajs-bliishtoolbox"
}

tokenprompt = input("enter your bliish token (sb-prkqirdzadljdpkrvjvz-auth-token): ")
def post():
    postdata["body"] = prompt
    response = requests.post(globalposts, json=postdata, headers={"cookie": f"sb-prkqirdzadljdpkrvjvz-auth-token={tokenprompt};"})
    print(response.text)

options = ["1. make a post", "2. bliip a user", "3. get posts from someone's wall", "4. exit"]
option = pick(options)

if option == "1. make a post":
    prompt = input("what do you want to post?")
    post()
elif option == "2. bliip a user":
    print("wip")
