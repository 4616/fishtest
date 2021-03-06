import sys
from datetime import datetime
from pymongo import ASCENDING, DESCENDING

class ActionDb:
  def __init__(self, db):
    self.db = db
    self.actions = self.db['actions']

  def get_actions(self, max_num):
    return self.actions.find(sort=[('_id', DESCENDING)], limit=max_num)

  def new_run(self, username, run):
    self._new_action(username, 'new_run', run)

  def modify_run(self, username, before, after):
    self._new_action(username, 'modify_run', {'before': before, 'after': after})

  def delete_run(self, username, run):
    self._new_action(username, 'delete_run', run)

  def stop_run(self, username, run):
    self._new_action(username, 'stop_run', run)

  def approve_run(self, username, run):
    self._new_action(username, 'approve_run', run)

  def _new_action(self, username, action, data):
    self.actions.insert({
      'username': username,
      'action': action,
      'data': data,
      'time': datetime.utcnow(),
    })
