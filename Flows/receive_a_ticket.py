from Flows.helper_class import HelperClass
class ReceiveATicket:
    def __init__(self):
        pass

    def Run(self, desired_tickets: int, current_visitors: int, max_capacity: int) -> int:
        remaining = max_capacity - current_visitors

        if desired_tickets <= remaining:
            for i in range(desired_tickets):
                print(f"{HelperClass.AnsiColorCodes.Yellow}  Ticket ausgegeben – Besucher Nr. {current_visitors + i + 1}{HelperClass.AnsiColorCodes.Reset}")
            return desired_tickets

        if remaining > 0:
            print(f"{HelperClass.AnsiColorCodes.Yellow}Leider sind nur noch {remaining} Ticket(s) verfügbar.{HelperClass.AnsiColorCodes.Reset}")
            answer = HelperClass.GetValidInput("Möchten Sie diese kaufen? (ja/nein): ", str)
            if answer.lower() == "ja":
                for i in range(remaining):
                    print(f"{HelperClass.AnsiColorCodes.Yellow}  Ticket ausgegeben – Besucher Nr. {current_visitors + i + 1}{HelperClass.AnsiColorCodes.Reset}")
                return remaining
            return 0

        print(f"{HelperClass.AnsiColorCodes.Red}Das Schwimmbad ist voll. Es können keine Tickets mehr verkauft werden.{HelperClass.AnsiColorCodes.Reset}")
        return 0
