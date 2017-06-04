from FaustBot.Communication.Connection import Connection
from FaustBot.Modules.PrivMsgObserverPrototype import PrivMsgObserverPrototype
from getraenke import getraenke
import random


class GiveDrinkObserver(PrivMsgObserverPrototype):

    def update_on_priv_msg(self, data: dict, connection: Connection):
        if data['message'].find('.drink') == -1:
            return
        connection.send_back('\001ACTION schenkt ' + data['nick'] + ' ' + random.choice(getraenke) + ' ein.\001', data)
