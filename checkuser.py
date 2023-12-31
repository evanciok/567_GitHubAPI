# auth: evan ciok
# course: ssw567
# assignment: hw04a

from datetime import datetime
def my_brand(assignment):
  datetime_obj = datetime.now()
  datetime_string = datetime_obj.strftime("%d/%m/%Y %H:%M:%S")
  print("=*=*=*= Evan Ciok =*=*=*=")
  print("=*=*=*= 2023F SSW 567-A =*=*=*=")
  print("=*=*=*= " + assignment + " =*=*=*=")
  print("=*=*=*= " + datetime_string + " =*=*=*=")
assignment_name = "HW04A - Develop With The Perspective Of The Tester In Mind"
my_brand(assignment_name)

import requests
import json

def getInfo(username):
        api = "https://api.github.com/users/" + username + "/repos"
        response = requests.get(f"{api}")
        if response.status_code == 200:
            repoList = []
            commitList = []
            for repo in response.json():
                repoList.append(repo['name'])
                commitList.append(getCommit(username, repo['name']))
            outputList = []
            element = 0
            for repo in repoList:
                 outputList.append(repo + " has " + str(commitList[element]) + " commits")
                 element+=1
            return outputList
        else:
            return "request error " + str(response.status_code)

def getCommit(username, repo):
        api = "https://api.github.com/repos/" + username + "/" + repo + "/commits"
        response = requests.get(f"{api}")
        if response.status_code == 200:
            commitCount = 0
            for commit in response.json():
                 commitCount+=1
            return commitCount
        else:
            return "request error " + str(response.status_code)
        
def main():
    print("input a github username to view all repositories and commit history")
    username = input()
    print(username + "'s github info:", getInfo(username))