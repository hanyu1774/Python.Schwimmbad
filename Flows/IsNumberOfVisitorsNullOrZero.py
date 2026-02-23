class IsNumberOfVisitorsNullOrZero:
    @staticmethod
    def Run(number_of_visitors) -> bool:
        return (number_of_visitors == 0) or (number_of_visitors is None)

