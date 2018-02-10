# AnnounceBot3000
Automating our announcements to our Slack/Facebook {Page,Group,Chat}/Email list.

## Setting Up

Run `virtualenv .` and `pip install -r requirements.txt`

To get the tool chain setup.

### Configuration

The configuration file is in TOML.

### Services

How to set up all the different services supported.

#### Slack

Register a new app and give it permissions to send messages. Then place its
OAUTH key under the environment variable `SLACK_OAUTH_TOKEN` (You can also place
it in `.env`)

## Todo

* Port to Python 3.
* Add Facebook Support
* Add support of mailing lists.
* Probably add Unicode support.
* Write a basic CLI
* Maybe make it a web service.
