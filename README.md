# AnnounceBot3000
Automating our announcements to our Slack/Facebook {Page,Group,Chat}/Email list.

## Setting Up

Run `virutalenv .` and `pip install -r requirements.txt`

To get the tool chain setup.

### Slack

Register a new app and give it permissions to send messages. Then place its
OAUTH key under the environment variable `SLACK_OAUTH_TOKEN` (You can also place
it .env)
