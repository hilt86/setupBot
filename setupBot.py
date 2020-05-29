from errbot import BotPlugin, botcmd
import requests

class setupBot(BotPlugin):
    """
    This bot does setup stuff
    """
    def get_configuration_template(self):
        return {'ID_TOKEN': 'abc123','URLBASE':'https://www.example.com/'}

    @botcmd  
    def tryme(self, msg, args):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """
        token = self.config['ID_TOKEN']
        url = self.config['URLBASE']
        requests.get(str(url) + str(token) + "/" + str(args), verify=True)
        return 'args: ' + str(args) + " message: " + str(msg)
