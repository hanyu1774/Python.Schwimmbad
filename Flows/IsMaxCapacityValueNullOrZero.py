class IsMaxCapacityValueNullOrZero:
    @staticmethod
    def Run(capacity_value) -> bool:
        return (capacity_value == 0) or (capacity_value is None)

