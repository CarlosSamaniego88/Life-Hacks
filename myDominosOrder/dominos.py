from pizzapi import *

def main():
    print('hello')
    carlos = Customer('Carlos', 'Samaniego', 'email@gmail.com', 'phone#')
    Florida_address = Address('street', 'city', 'state', 'zip code')

    FL_store = Florida_address.closest_store()

    # menu = FL_store.get_menu()

    # menu.search(Name="custompizza")

    # order = Order(FL_store, carlos, Florida_address)
    # order.add_item('')

    # order.remove_item('')

    # card = PaymentObject('card number', 'exp date', 'security code', 'zip code')

    # order.place(card)       #to actually order

    # order.pay_with(card)    #for testing

if __name__ == '__main__':
    main() 
