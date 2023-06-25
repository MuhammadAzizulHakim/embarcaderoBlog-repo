from http import HTTPStatus

print(HTTPStatus.OK)
print(HTTPStatus.OK == 200)
print(HTTPStatus.OK.value)
print(HTTPStatus.OK.phrase)
print(HTTPStatus.OK.description)
print(list(HTTPStatus))