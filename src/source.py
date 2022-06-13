import urllib.request, json

# Get a organizations repo
def get_org_repositories(org):
    url = 'https://api.github.com/orgs/' + org + '/repos'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode())
    return [repo['name'] for repo in data]

# Get a users repo
def get_user_repositories(user):
    url = 'https://api.github.com/users/' + user + '/repos'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode())
    return [repo['name'] for repo in data]