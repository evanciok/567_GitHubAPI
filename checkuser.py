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

def getRepo(username):
        api = "https://api.github.com/users/" + username + "/repos"
        response = requests.get(f"{api}")
        if response.status_code == 200:
            repoList = []
            for repo in response.json():
                repoList.append(repo['name'])
            print("user " + username + " has repos: " + str(repoList))
        else:
            print(f"request error {response.status_code}")

def getCommit(username, reponame):
        api = "https://api.github.com/repos/" + username + "/" + reponame + "/commits"
        response = requests.get(f"{api}")
        if response.status_code == 200:
            commitCount = 0
            for commit in response.json():
                 commitCount+=1
            print("repo " + reponame + " has " + str(commitCount) + " commits")
                
        else:
            print(f"request error {response.status_code}")    

def main():
    print("input a github username to view all repositories")
    username = input()
    getRepo(username)
    print("input a repository name to view number of commits")
    reponame = input()
    getCommit(username, reponame)

main()