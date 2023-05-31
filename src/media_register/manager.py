class Manager:
  def __init__(self, template_path, redis_config, sql_config):
    self.template_path = template_path
    self.redis_config = redis_config
    self.sql_config = sql_config

  def create(self, media_name, API_user):
    pass

  def rebuild(self, media_name, API_user):
    pass

  def register(self, media_name, API_user):
    pass