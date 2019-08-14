from pizzapi import *
import os
#this is a test line to see if contributions are being checked

def main():
    #Customer
    carlos = os.environ['carlos']
    #carlos = Customer('first', 'last', 'email', 'phone number')

    #Addresses
    #florida_address = Address('10952 Crescendo Circle', 'Boca Raton', 'FL', '33498')
    wake_address = Address('1834 Wake Forest Road', 'Winston Salem', 'NC', '27109')

    #Find stores based on address
    #FL_store = florida_address.closest_store()
    Wake_store = wake_address.closest_store()
    #closest dominos to FL address is Dominos pizza on 10101 Glades Rd

    #initialize menu from stores near your address
    menu = Wake_store.get_menu()

    #search for menu items
    #menu.search(Name="bacon")

    #Order for store in florida/wake, customer, and where its going
    order = Order(Wake_store, carlos, wake_address)

    #Add items to order
    order.add_item('10SCREEN')   #10SCREEN Small (10") Hand Tossed Pizza $7.99 10 S_PIZZA {'X': '1', 'C': '1'}
    order.add_item('20BCOKE')    #20BCOKE 20oz Bottle Coke® $1.99 20OZB F_COKE {}
    order.add_item('20BSPRITE')  # 20BSPRITE 20oz Bottle Sprite® $1.99 20OZB F_SPRITE {}
    
    # Other Examples below
    # order.add_item('P12IPAZA') # add a 12-inch pan pizza
    # order.add_item('MARINARA') # with an extra marinara cup
    # order.add_item('20BCOKE')  # and a 20oz bottle of coke

    #remove items from order
    #order.remove_item('')

    #payment details
    card = os.environ['card']    
    # PaymentObject('card number', 'exp date', 'security code', 'zip code')

    #to actually order
    #order.place(card)       

    #for testing
    order.pay_with(card)

if __name__ == '__main__':
    main() 