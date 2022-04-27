import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
# print(f"{r.status_code}")
response_dict = r.json()
# print(response_dict.keys())

repo_dicts = response_dict['items']

repo_names, stars = [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'marker':{
        'color':'rgb(60,100,150)',
        'line': {'width':1.5, 'color':'rgb(25,25,25)'}
    },
    'opacity':0.6
}]

my_layout = {
    'title': "Github 上最受欢迎的仓库",
    'xaxis': {'title':'Repository'},
    'yaxis': {'title': 'Stars'}
}

fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='python_repos.html')
