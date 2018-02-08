import pytoml as toml
import os

# Currently this reads a file to get the configuration, though we might in the
# future turn this whole thing into a web service, so this will become an
# abstraction to that database.
class AnnounceConfiguration:
    _config = None
    # Set up and parse the configuration.
    # Awful function. Please clean up
    def __init__(self, config_file):
        with open(config_file, 'rb') as config:
            obj = toml.load(config)
            self._config = obj
            self._recursive_obj_search(self._config)
        #print self._config
    # Used to replace strings that start with "env:" with whatever that environ
    # variable resolves to.
    @staticmethod
    def _attempt_patch_str(in_dict, key):
        if in_dict[key][0:4] == "env:":
            in_dict[key] = os.environ[in_dict[key][4::]]

    def _recursive_obj_search(self, in_dict):
        if type(in_dict) not in [list, dict]:
            return None
        if type(in_dict) == dict:
            search = in_dict.keys()
        else:
            search = range(0, len(in_dict))
        for key in search:
            # the testcase depends on the type.
            if type(in_dict) == dict:
                testcase = in_dict[key]
            else:
                testcase = key
            testcase_type = type(testcase)
            # Now search in_dict
            if testcase_type in [list, dict]:
                self._recursive_obj_search(testcase)
            elif testcase_type in [str,unicode]:
                self._attempt_patch_str(in_dict, key)
            else:
                # Not a data type we care about
                pass

    def get_accounts(self):
        try:
            return self._config['accounts']
        except:
            return []
    def get_lists(self):
        try:
            return self._config['lists']
        except:
            return []

if __name__ == "__main__":
    config = AnnounceConfiguration("examples/example.toml")
    print(config._config)
