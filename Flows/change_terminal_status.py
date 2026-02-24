from Flows.helper_class import HelperClass
class ChangeTerminalStatus:
    def __init__(self):
        pass

    def Run(self, current_visitors, max_capacity) -> bool: 
      return HelperClass.ValidateData(max_capacity, current_visitors) 
