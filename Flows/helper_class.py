class HelperClass:
    def __init__(self)

    def WasCapacityReached(self, capacity_value, number_of_visitors) -> bool:
        return number_of_visitors == capacity_value

    def IsNumberOfVisitorsNullOrZero(self,number_of_visitors) -> bool:
        return (number_of_visitors == 0) or (number_of_visitors is None)

    def IsCapacityValueNullOrZero(self, capacity_value) -> bool:
        return (capacity_value == 0) or (capacity_value is None)

    @staticmethod
    def ValidateData(capacity_value, number_of_visitors) -> bool:
        if not WasCapacityReached(capacity_value) and not IsNumberOfVisitorsNullOrZero(number_of_visitors)
            and not ICapacityValueNullOrZero(capacity_value):
            return true
        return false


