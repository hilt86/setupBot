from errbot import BotPlugin, botcmd
import requests

class setupBot(BotPlugin):
    """
    This plugin helps provision users
    """
    def get_configuration_template(self):
        return {'ID_TOKEN': 'abc123','URLBASE':'https://www.example.com/'}

    @botcmd  
    def resend(self, msg, args): 
        """
        Calls an API and returns response from that API
        """
        token = self.config['ID_TOKEN']
        url = self.config['URLBASE']
        r = requests.get(str(url) + str(token) + "/" + str(args), verify=True)
        return r.status_code
