import requests
import json
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the respnse.
url = 'https://api.github.com/search/repositories?q=language:python'
headers = {'Accept': 'application/vnd.github.v3json'}
r = requests.get(url, headers = headers)
# print(r.status_code)

response_dict = r.json()
repo_dicts = response_dict['items']

repo_links, watchers, labels = [], [], []
for repo_dict in repo_dicts:
	repo_name = repo_dict['name']
	repo_url = repo_dict['html_url']
	repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
	repo_links.append(repo_link)
	watchers.append(repo_dict['watchers'])

	# owner = repo_dict['owner']['login']
	open_issues = f"The amount of current open issues " + str(repo_dict['open_issues'])
	forks = f"The total amount of forks " + str(repo_dict['forks'])
	label = f"{open_issues}<br />{forks}"
	labels.append(label)

# Make visualisation.
data = [{
	'type': 'bar',
	'x': repo_links,
	'y': watchers,
	'hovertext': labels,
	'marker': {
		'color': 'rgb(80, 25, 180)',
		'line': {'width': 1.5, 'color': 'rgb(75, 75, 75)'}
	},
	'opacity': 0.6,
}]

my_layout = {
	'title': 'Python Projects with the most watchers on Github',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Repository',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
	'yaxis': {
		'title': 'Watchers',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='Python_repos.html')