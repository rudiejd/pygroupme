import requests


# send a message to a GroupMe group given a bot id from the GroupMe API (api.groupme.com)
def gm_msg(bid, text):
    msg_params = {'bot_id': bid, 'text': text}
    try:
        requests.post('https://api.groupme.com/v3/bots/post', params=msg_params)
    except (requests.exceptions.RequestException) as e:
        print('An error occurred: {0}'.format(e))
        return False
    finally:
        return True


# receive a given limit of GroupMe messages supplied in a json. supply gid and limit.
# format can be found at https://dev.groupme.com/docs/v3
def gm_rec(token, gid, limit=1):
    rec_params = {'token': token, 'limit': limit}
    try:
        api_return = requests.get('https://api.groupme.com/v3/groups/{0}/messages'.format(gid), params=rec_params).json()
    except (TypeError, requests.exceptions.RequestException) as e:
        print('An error occurred: {0}'.format(e))
        return None
    finally:
        return api_return
