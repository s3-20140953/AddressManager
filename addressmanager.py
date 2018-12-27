from address import Address

class AddressManager():

    #Constructor

    def __init__(self):
        self.addressList = []

    def add_address(self,address):
        if address is []:
            pass
        else:
            self.addressList.append(address)

    def get_address(self,key):
        for address in self.addressList:
            if address.name == key:
                return address
        return None

    def modify_address(self,key,inputAdress):
        address = self.get_address(key)

        if address is None:
            return None
        else:
            #Modify Data
            address.name = inputAdress.name
            address.number = inputAdress.number

    def show_address(self):
        str = ''
        for address in self.addressList:
            str += address.name + ":" + address.number

        #Echo check
        print(str)
        return str
