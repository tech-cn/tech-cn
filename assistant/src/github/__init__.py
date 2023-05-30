class Github:
  def __init__(self, token):
    self.token = token
    self.headers = {
      "Authorization": f"token {self.token}",
      "Accept": "application/vnd.github.v3+json"
    }
    self.url = "https://api.github.com"
