class Address:
    def __init__(self, country, city, street):
        self.country = country
        self.city = city
        self.street = street
    def __str__(self):
        result = ''
        for k,v in self.__dict__.items():
            result += f'{k} : {v}\n'
        return result

class AddressParser:
    def getAddress(country, city, street):
        return Address(country, city, street)


def main():
    a = AddressParser.getAddress('Israel', 'Tel Aviv', 'HaShalom')
    print(type(a))
    print(a)

if __name__ == '__main__':
    main()
