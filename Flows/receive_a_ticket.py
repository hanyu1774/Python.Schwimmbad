from Flows.HelperClass import HelperClass
class ReciveATicket:
    def __init__(self) -> None:
        pass

    def Run(self, given_tickets, max_capacity) -> int:
        if HelperClass.ValidateData(given_tickets, max_capacity):
            print("A customer receives a ticket!")
            return 1
        
        elif not HelperClass.ValidateData(given_tickets, max_capacity):
            print("Capacity of public swimming pool has been reached.")
            print("As a result, further customers can't get their tickets.")
            return 0;

        return 0;
