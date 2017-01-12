import os

GITLAB_URL         = os.getenv("GITLAB_URL", "https://gitlab.com")
CLIENT_ID          = os.getenv("GITLAB_CLIENT_ID")
CLIENT_SECRET      = os.getenv("GITLAB_CLIENT_SECRET")
# GitLab does not support revoking keys on logout, we emulate it by frequently expiring keys
EXPIRATION_MINUTES = int(os.getenv("GITLAB_EXPIRATION_MINUTES", "5"))

ACCESS_TOKEN       = os.getenv("GITLAB_ACCESS_TOKEN")
