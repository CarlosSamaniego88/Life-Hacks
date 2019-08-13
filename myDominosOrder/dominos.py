from pizzapi import *
#this is a test line to see if contributions are being checked

def main():

    #Customer
    # carlos = Customer('first', 'last', 'email', 'phone number')
    
    #Addresses
    Florida_address = Address('street address', 'city', 'state', 'zip code')

    #Find stores based on address
    FL_store = Florida_address.closest_store()
    #closest dominos to FL address is Dominos pizza on 10101 Glades Rd

    #initialize menu from stores near your address
    menu = FL_store.get_menu()

    #search for menu items
    #menu.search(Name="custom")

    #Order for store in florida, customer, and where its going
    order = Order(FL_store, carlos, Florida_address)

    #Add items to order
    order.add_item('10SCREEN')
    order.add_item('D20BCCKE')
    #10SCREEN Small (10") Hand Tossed Pizza $7.99 10 S_PIZZA {'X': '1', 'C': '1'}
    #D20BCCKE 20oz Bottle Cherry Coke® $1.99 20OZB F_CCKE {}

    # Examples below
    # order.add_item('P12IPAZA') # add a 12-inch pan pizza
    # order.add_item('MARINARA') # with an extra marinara cup
    # order.add_item('20BCOKE')  # and a 20oz bottle of coke

    #remove items from order
    #order.remove_item('')

    #payment details
    card = PaymentObject('card number', 'exp date', 'security code', 'zip code')

    #to actually order
    #order.place(card)       

    #for testing
    order.pay_with(card)

if __name__ == '__main__':
    main() 
