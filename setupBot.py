from errbot import BotPlugin, botcmd
import requests

class setupBot(BotPlugin):
    """
    This bot does setup stuff
    """
    def get_configuration_template(self):
        return {'ID_TOKEN': '00112233445566778899aabbccddeeff','USERNAME':'changeme'}

    @botcmd  # flags a command
    def tryme(self, msg, args):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """
        token = self.config['ID_TOKEN']
        requests.get("https://ifconfig.co", verify=True)
        return 'It *works* !'  # This string format is markdown.
