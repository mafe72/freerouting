import pcbnew
import os

class Freeroute(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Freeroute"
        self.category = "Autorouting"
        self.description = "Triggers Freerouting"

    def Run(self):
        # The entry function of the plugin that is executed on user action
        board = pcbnew.GetBoard()
        basename = os.path.splitext(board.GetFileName())
        
        os.system(pcbnew.GetKicadConfigPath()+'\\FreeRouting.jar -de \"'+basename[0]+'.dsn\"')

Freeroute().register() # Instantiate and register to Pcbnew