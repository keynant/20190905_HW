import json
import requests


class WebRest:
    def getWebResult(url, id):
        return WebResult(url, id)


class WebResult:
    def __init__(self, url, id):
        response = requests.get(str(url) + str(id))
        if response.status_code != 404:
            self.result = json.loads(response.content)
        if response.status_code == 404:
            self.result = f'{url+id}: 404 - Request not found'

    def __str__(self):
        result = ''
        try:
            for k, v in self.result.items():
                result += f'{k} : {v}\n'
        except AttributeError:
            result = self.result
        return result


def main():
    result = WebRest.getWebResult('https://jsonplaceholder.typicode.com/', 'todos/11')
    print(result)


if __name__ == "__main__":
    main()

