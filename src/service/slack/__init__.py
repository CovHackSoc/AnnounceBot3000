import requests

class SlackAnnounce:
    # Authorise us.
    def __init__(self, verification_token):
        self.base = "https://slack.com/api"
        self.verification_token = verification_token
        pass
    # Send the message to the Slack Workspace.
    def send_message(self, channel, message):
        data = {
            "text": message,
            "channel": channel
        }
        headers = {
            "Authorization": "Bearer {}".format(self.verification_token)
        }
        r = requests.post("{}/chat.postMessage".format(self.base),
                          data=data, headers=headers)
        return r.json()['ok']

if __name__ == "__main__":
    #testing
    pass
