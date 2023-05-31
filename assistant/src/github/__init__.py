class Github:
  def __init__(self, url, token):
    self.token = token
    self.headers = {
      "Authorization": f"token {self.token}",
      "Accept": "application/vnd.github.v3+json"
    }
    self.url = url

