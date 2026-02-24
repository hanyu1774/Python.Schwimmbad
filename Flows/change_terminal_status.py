from Flows.helper_class import HelperClass


class ChangeTerminalStatus:
    def __init__(self) -> None:
        pass

    def Run(self, current_visitors: int, max_capacity: int) -> bool:
        return HelperClass.ValidateData(max_capacity, current_visitors)
