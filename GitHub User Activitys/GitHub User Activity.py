import requests
import sys  
import json

def fatch_data(user):
    responce = requests.get(f"https://api.github.com/users/{user}/events")
    if responce.status_code != 200:
        print("We had an error")
    j_responce = responce.json()
    for event in j_responce:
        if event["type"] == "PushEvent":
            repo_name = event["repo"]["name"]
            comit_count = len(event["payload"]["commits"])
            print(f"Pushed {comit_count} commits to {repo_name}")
        elif event["type"] == "IssuesEvent":
            action = event["payload"]["action"]
            repo_name = event["repo"]["name"] 
            print(f"{action} isuse in {repo_name}")
        elif event["type"] == "IssueCommentEvent":
            action = event["payload"]["action"]
            repo_name = event["repo"]["name"] 
            print(f"starred {repo_name}")
        else:
            print(f"{event["type"]} accurd in {event["repo"]["name"]}")
def main():
    if len(sys.argv) != 2:
        sys.exit("You need one argument")
    else:
        fatch_data(sys.argv[1])





if __name__ =="__main__":
    main()


