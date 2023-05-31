from .manager import *
from redis import Redis

class TemplateManager(Manager):
  
  def __init__(self, template_path, redis_db, sql_db):
    super().__init__(template_path, redis_db, sql_db)

  def create(self, template_name, API_user):
    if self.redis_db.get(f'template_{template_name}') != 'nil':
      raise KeyError(f'Template \'{template_name}\' already exists!')
    
    
    pass

  def rebuild(self, template_name, API_user):
    pass

  def register(self, template_name, API_user):
    pass
