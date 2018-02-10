from marionette_driver.marionette import Marionette, Actions, Keys
from marionette_driver import By
import random
import time

# Class that implements an announcer for facebook messenger using a development
# build of Firefox (either the nightly or beta channels).
# You need to run Firefox already with the `--marionette` command line flag.
class AnnounceMessenger:
    # Create our marionette instance.
    def __init__(self):
        self.client = Marionette('localhost', port=2828)
        self.client.start_session()
        random.seed()
    def send_message(self, to_user, message, wait_load=0.5):
        # Make firefox go to the users page.
        self.client.navigate("https://www.messenger.com/t/{}".format(to_user))
        # Give a little bit of time to load.
        time.sleep(wait_load)
        for letter in message:
            # Make the typing look realistic.
            keep_down = random.uniform(0.005, 0.010)
            wait_time = keep_down+random.uniform(0.02,0.05)
            # Send off the action
            action = Actions(self.client)
            if letter != '\n':
                action.key_down(letter).wait(keep_down).key_up(letter)
            else:
                # Handle multi line messages.
                action.key_down(Keys.SHIFT).key_down(Keys.ENTER)\
                    .wait(keep_down).key_up(Keys.SHIFT).key_up(Keys.ENTER)
            action.perform()
            # wait for it to complete.
            time.sleep(wait_time)
        # Send message.
        action.key_down('\n').wait(keep_down).key_up('\n')
        action.perform()

if __name__ == "__main__":
    announcer = AnnounceMessenger()
    # Can be ID for a group chat.
    username = "<USERNAME_HERE>"
    message = "Test message\nBlah\ncool"
    announcer.send_message(username, message)
