from .manager import *

class MediaManager(Manager):
  
  def __init__(self, template_path, redis_config, sql_config):
    super().__init__(template_path, redis_config, sql_config)

  def create(self, media_name, API_user):
    pass

  def rebuild(self, media_name, API_user):
    pass

  def register(self, media_name, API_user):
    pass
