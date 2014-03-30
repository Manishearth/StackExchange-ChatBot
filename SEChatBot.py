from ChatExchange.SEChatWrapper import *

class SEChatBot:
  def __init__(self, site="SE",trigger="!!"):
    self.wrap=SEChatWrapper(site)
    self.watchers=[]
  def login(self, username, password):
    self.wrap.login(username,password)
  def joinRoom(roomno):
    "Join some room"
  def watchCommand(commandname,handler):
    "Watch for a command, handler should take (args,roomnumber) as arguments and return a reply"
  def postMessage(roomno,message):
    "Expose inner postMessage here"
  def _watcher():
    "Use array of watch functions to watch room"
