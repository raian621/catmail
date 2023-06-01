class Manager:
  def __init__(self, template_path, redis_config, sql_config):
    self.template_path = template_path
    self.redis_config = redis_config
    self.sql_config = sql_config

  def create(self, name, API_user):
    pass

  def upload(self, name, API_user, chunk, chunk_number):
    pass

  def rebuild(self, name, API_user):
    pass

  def register(self, name, API_user):
    pass