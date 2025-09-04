import os, sys, json, yaml
from dotenv import load_dotenv
from requests import Session

def yprint(a):
    print(yaml.dump(a.json()))

def jprint(a):
    print(json.dumps(json.loads(a.text), indent=2))

load_dotenv('./.ghenv')
TOKEN = os.getenv('TOKEN')
GH = 'https://api.github.com'
ORG = 'test-bubutz-org'
REPO = 'testops-org'
headers = {
	"Accept": "application/vnd.github+json",
	"Authorization": f"Bearer {TOKEN}",
	"X-GitHub-Api-Version": "2022-11-28"
}
s = Session()
s.headers.update(headers)
