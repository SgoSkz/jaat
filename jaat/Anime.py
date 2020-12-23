class Anime(object):
    options = {
        "source": "",
        "quality": "",
    }
    anime = {
        "title": "",
        "description": "",
        "release": "",
        "home_link": "",
    }
    episode_links = []

    def __init__(self, *args, **kwargs):
        pass

    def __config(self):
        with open("./config", "r") as config:
            opts = config.read()
            for i in opts.split("\n"):
                set_opt = i.split(": ")
                self.options[set_opt[0]] = set_opt[1]

    def search(self, query):
        """
        Searchs stuff based on the selected source in self.options dictionary
        """
        # TODO search query stuff
        pass

    def episodes(self):
        """
        Gets the episodes of selected anime
        """
        # TODO Finishes sources to figure out how this works
        pass

