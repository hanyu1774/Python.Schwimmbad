from Flows.change_terminal_status import ChangeTerminalStatus
from Flows.receive_a_ticket import ReceiveATicket
from Flows.helper_class import HelperClass
from Models.public_swimming_pool import PublicSwimmingPool

class Workflow:
    def __init__(self):
        pass

    def Run(self):
        pool = PublicSwimmingPool()
        receive_a_ticket = ReceiveATicket()
        change_terminal_status = ChangeTerminalStatus()

        print(HelperClass.AnsiColorCodes.Green)
        print('#' * 45)
        print("   Willkommen am Ticketautomaten!")
        print(f"   Maximale Kapazität: {pool.max_capacity} Besucher")
        print('#' * 45)
        print(HelperClass.AnsiColorCodes.Reset)
        print()

        while pool.is_ticket_terminal_active:
            remaining = pool.max_capacity - pool.current_visitors
            print(f"\nAktuell im Schwimmbad: {pool.current_visitors} / {pool.max_capacity}")
            print(f"Noch verfügbare Plätze: {remaining}")

            desired = HelperClass.GetValidInput("Wie viele Tickets möchten Sie? ", int)
            if desired <= 0:
                print(f"{HelperClass.AnsiColorCodes.Red}Bitte eine positive Anzahl eingeben.{HelperClass.AnsiColorCodes.Reset}")
                continue

            issued = receive_a_ticket.Run(desired, pool.current_visitors, pool.max_capacity)
            pool.current_visitors += issued
            pool.is_ticket_terminal_active = change_terminal_status.Run(
                pool.current_visitors, pool.max_capacity
            )

        print()
        print('#' * 45)
        print(f"{HelperClass.AnsiColorCodes.Red}Das Schwimmbad ist voll.{HelperClass.AnsiColorCodes.Reset}")
        print(f"{HelperClass.AnsiColorCodes.Yellow}Der Ticketautomat wurde geschlossen.{HelperClass.AnsiColorCodes.Reset}")
        print('#' * 45)
