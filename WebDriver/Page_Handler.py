import requests

def checkPage(current_response:requests.Response, desired_url:str) -> bool:
    """
    Checks that current url is the same or a queried version of the desired url

    :param current_response: the request object of the current session
    :param desired_url: the URL you want to confirm that you are viewing
    :return: bool, True if it passes the check and False if it fails, also raises error for type of fail along with response object
    """


    if current_response.status_code != 200:
        raise Exception(f"Did not get response from page {current_response.url} Error: {current_response.status_code}")
        return False
    if desired_url not in current_response.url:
        raise Exception(f"expected to be at {desired_url} instead was taken to {current_response.url}")
        return False
    return True