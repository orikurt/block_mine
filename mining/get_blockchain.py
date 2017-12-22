import requests
import json
from datetime import datetime

def get_block(hash):
    url = "https://blockchain.info/rawblock/{}".format(hash)
    response = requests.get(url)
    try:
        assert(response.status_code == 200)
        block = json.loads(response.text)
        return block
    except (AssertionError, json.decoder.JSONDecodeError) as e:
        print(e)
        return None


def get_latest_block():
    base = "https://blockchain.info/latestblock"
    response = requests.get(base)
    assert(response.status_code == 200)
    latest_block = json.loads(response.text)
    print("latest block hash: {0}, dated: {1}".format(latest_block['hash'], datetime.fromtimestamp(latest_block['time'])))
    return get_block(latest_block['hash'])

if __name__=="__main__":
    print(get_latest_block().keys())