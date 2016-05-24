import logging
import subprocess

import requests


logger = logging.getLogger(__name__)


class Github(object):
    auth_token = None
    repo_path = None
    username = None

    # For url constructing
    owner = None
    repo = None
    url_base = "https://api.github.com/"

    def __init__(self, auth_token, repo_path, username):
        self.auth_token = auth_token
        self.repo_path = repo_path
        self.username = username
        logger.debug("Initializing repository: %s" % self.repo_path)

        data = subprocess.check_output(
            ["git", "config", "remote.origin.url"],
            cwd=self.repo_path
        )
        data = data.decode("utf-8")
        self.owner, self.repo = data.split(":")[1].split(".git")[0].split("/")
        logger.debug("Owner: %s, repo: %s" % (self.owner, self.repo))

    @property
    def auth(self):
        return (self.username, self.auth_token)

    def get_pull_requests(self):
        url = "repos/%s/%s/pulls" % (self.owner, self.repo)
        url = self.url_base + url
        response = self._make_get_request(url)
        print("%s pull requests" % len(response))

    def _make_get_request(self, url):
        """
        A helper that makes authenticated get request to the given url
        """
        response = requests.get(url, auth=self.auth)
        logger.debug("Getting url: %s -- %s" % (url, response.status_code))
        if response.status_code == 200:
            return response.json()
        raise APIException(
            "Unexpected status code %s: %s" % (
                response.status_code, response.json()
            )
        )


class APIException(BaseException):
    pass
