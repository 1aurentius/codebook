import requests

# Replace these values with your own
owner = '1aurentius'
repo = 'codebook'
pull_number = 3

# Hey there

# Get the pull request URL
url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}'
response = requests.get(url)
data = response.json()
head_branch_url = data['head']['repo']['url']

# Get the code from the pull request
url = f'{head_branch_url}/pulls/{pull_number}/files'
response = requests.get(url)
data = response.json()

# Print the contents of each file
for file in data:
    contents_url = file['raw_url']
    response = requests.get(contents_url)
    print(response.text)