class Parking_garage():

    '''
        The program should take the following input types:
        - tickets should be lists
        - spaces should be a list
        - current_ticket is a dictionary
    '''

    def __init__(self, tickets = [], spaces = [], current_ticket = {}):
        self.tickets = tickets
        self.spaces = spaces 
        self.current_ticket = current_ticket

    def decision_tree(self):
        while True:
            result = input('How can we help? \n - Get Ticket ("Get") \n - Checkout ("Checkout") \n - Show Current Ticket(s) ("Show") \n - Help ("Help")\n - Quit ("Quit")\n')
            if result.lower() == 'get':
                Parking_garage.take_ticket(self)
            elif result.lower() == 'checkout':
                if len(self.tickets) == 10:
                    print("\nYou're not even in the garage\n")
                    Parking_garage.decision_tree(self)
                else:
                    Parking_garage.pay_for_parking(self)
            elif result.lower() == "show":
                print(self.current_ticket)
            elif result.lower() == 'quit':
                break
            else:
                print('''\n\nPlease type one of the following prompts: \n\nFor recieving a ticket and gaining access to the garage, \nplease type "Get".\nFor checking out and escaping the parking garage,\nplease type "Checkout". \nIf you'd like to quit the process and not get a ticket, \nplease type "Checkout". \nIf you'd like to show your current ticket(s)\nplease type "Show" \nIf you'd like to quit the process and not get a ticket,\nplease type "Quit".\n\n\n''')

    def take_ticket(self):
        if len(self.spaces) == 0:
            print("We're full! Sorry")
        else:
            if len(self.tickets) > 0:
                new_ticket = self.tickets.pop(0)
                print(f'Your ticket number is {new_ticket}\n')
                self.current_ticket[new_ticket] = "unpaid"
            else:
                print('We are out of space! Sorry!')
                Parking_garage.decision_tree(self)

    def pay_for_parking(self):
        ticket_num = input("What is your ticket number? ")
        ticket_num_int = int(ticket_num)
        if ticket_num_int in self.current_ticket:
            pay = input("Press 'p' to pay ")
            if pay.lower() == 'p':
                self.tickets.append(ticket_num_int)
                self.spaces.append(ticket_num_int)
                if len(self.current_ticket) > 0:
                    ccd = input('Credit Card Number: ')
                    exp = input('Expiration date: ')
                    security = input('Security code: ')
                    self.current_ticket.pop(ticket_num_int)
                    print("Have a great day! Watch for moose!\n")
                else:
                    print("Garage is full")
                    pass
            else:
                print("Press 'p' better next time\n")
                Parking_garage.decision_tree(self)
        else:
            print("That ticket is not available")


def run_garage():
    ticket_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    spaces_available = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    garage = Parking_garage(ticket_list, spaces_available)
    garage.decision_tree()

run_garage()   
