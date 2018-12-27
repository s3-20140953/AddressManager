from address import Address
from addressmanager import AddressManager
import bottle

global manager
manager = AddressManager()


@bottle.route('/show')
def show_page():
    result = manager.show_address()
    return result


@bottle.route('/modify/<userInput>')
def modify_page(userInput):
    temp = userInput.split('|')

    initialData = Address()
    initialData.name = temp[0]
    initialData.number = temp[1]
    state = manager.modify_address(temp[0],initialData)
    if(state is None):
        str = "nothing modified."
        return str
    else:
        str = "complete."
        return str


@bottle.route('/add/<userInput>')
def add_page(userInput):
    temp = userInput.split('|')

    #set data
    initialData = Address()
    initialData.name = temp[0]
    initialData.number = temp[1]
    manager.add_address(initialData)

    #console log
    manager.show_address()


bottle.debug(True)
bottle.run(host='localhost',port=8080)
