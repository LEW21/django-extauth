# GitLab auth module for Django

## Configuration

Environment variables:
* GITLAB_URL - GitLab installation URL, without trailing slash. Default: https://gitlab.com
* GITLAB_CLIENT_ID - GitLab OAuth client ID
* GITLAB_CLIENT_SECRET - GitLab OAuth client secret
* EXPIRATION_MINUTES - For how long to assume that user is still logged in; after this time, we'll retry logging in (which is invisible for GET requests, and breaks other ones). Default: 5
* GITLAB_ACCESS_TOKEN - Personal Access Token of any account, used for checking profiles of people without logging in

## settings.py

```python
EXTAUTH_BACKEND = "gitlab"
```

## GitLab

Redirect URI: http(s)://app-domain/accounts/login/callback
