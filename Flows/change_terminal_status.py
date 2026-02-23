from Flows.HelperClass import HelperClass
class ChangeTerminalStatus:
    def __init__(self):
        pass

    def Run(self, current_visitors, max_capacity) -> bool: 
        if HelperClass.ValidateDate(current_visitors, max_capacity):
            return False
        elif not HelperClass.ValidateDate:
            return True
        return False
