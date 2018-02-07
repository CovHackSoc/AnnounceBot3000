import facebook
import slack
import emails
import os

from dotenv import load_dotenv
dotenv_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path)


if __name__ == "__main__":
    slack_vt =  os.environ['SLACK_OAUTH_TOKEN']
    slack_bot = slack.SlackAnnounce(slack_vt)
    print slack_bot.post_message("#tests", "Ahoy There!")
