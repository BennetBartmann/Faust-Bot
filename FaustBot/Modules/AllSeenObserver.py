import datetime
import time
from collections import defaultdict

from FaustBot.Communication.Connection import Connection
from FaustBot.Model.IRCData import IRCData
from FaustBot.Model.UserProvider import UserProvider
from FaustBot.Modules.PrivMsgObserverPrototype import PrivMsgObserverPrototype
from FaustBot.Modules.UserList import UserList


class AllSeenObserver(PrivMsgObserverPrototype):
    @staticmethod
    def cmd():
        return []

    @staticmethod
    def help():
        return None

    def __init__(self, user_list: UserList):
        super().__init__()
        self.user_list = user_list

    def update_on_priv_msg(self, data, connection: Connection):
        if data.message.find('.allseen') == -1:
            return
        users = self.user_list.userList[data.channel]
        if users is None:
            return
        if not self._is_idented_mod(data, connection):
            return
        User_afk = defaultdict(int)
        for who in users.keys():
            user_provider = UserProvider()
            activity = user_provider.get_activity(who, data.channel)
            delta = time.time() - activity
            User_afk[who] = delta
        for w in sorted(User_afk, key=User_afk.get):
            output = (w+":\t"+str(datetime.timedelta(seconds=User_afk[w])))
            connection.send_back(output, data)

    def _is_idented_mod(self, data: IRCData, connection: Connection):
        mods = self._config.get_channel_by_name(data.channel).mods
        return data.nick in mods and connection.is_identified(data.nick)
