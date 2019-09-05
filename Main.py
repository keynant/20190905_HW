from addressapi import AddressParser
from webapi import WebRest


address = AddressParser.getAddress('Israel', 'Ramat Gan', 'Herut')
print(address)

result = WebRest.getWebResult('https://jsonplaceholder.typicode.com/', 'todos/1')
print(result)
result = WebRest.getWebResult('https://jsonplaceholder.typicode.com/', 'photos/45')
print(result)
result = WebRest.getWebResult('https://jsonplaceholder.typicode.com/', 'users/1')
print(result)
result = WebRest.getWebResult('https://jsonplaceholder.typicode.com/', 'users/111')
print(result)