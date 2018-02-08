import service.facebook
import service.slack
import service.email
import os
import config

from dotenv import load_dotenv
dotenv_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path)

class AnnounceBot:
    def __init__(self, config_file):
        # read configuration
        self._config = config.AnnounceConfiguration(config_file)
        self._accounts = self._config.get_accounts()
        self._lists = self._config.get_lists()
    # Sends the message to everyone on the list.
    def send_message(self, mailing_list, message):
        if mailing_list in self._lists:
            for account in self._lists[mailing_list]:
                account_details = self._accounts[account]
                if account_details['type'] == "slack":
                    slack_acc = service.slack.SlackAnnounce(account_details['key'])
                    for channel in self._lists[mailing_list][account]:
                        slack_acc.send_message(channel, message)

if __name__ == "__main__":
    #slack_vt =  os.environ['SLACK_OAUTH_TOKEN']
    #slack_bot = service.slack.SlackAnnounce(slack_vt)
    #print slack_bot.post_message("#tests", "Ahoy There!")
    bot = AnnounceBot('examples/example.toml')
    bot.send_message("main","Don't mind me, bear is just testing a script.")
