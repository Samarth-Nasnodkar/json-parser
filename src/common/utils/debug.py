from common.config import DEBUG

def dprint(*args, **kwargs):
  """
  Custom print function that only prints if DEBUG is True.
  """
  if DEBUG:
    print(*args, **kwargs)