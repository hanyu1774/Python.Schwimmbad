class HelperClass:
    class AnsiColorCodes:
    
        # Erklärung:
        # In Python gibt es keine Standardfunktion zum Ändern von Schriftfarben in der Konsole.
        # Alternativ: Konsolen verstehen ANSI Escape Codes und hier kann man Farben angeben.
        # Sind diese Angaben vor irgendeinem einem String, wird dessen Schriftfarbe geändert.

        Red = "\033[31m"
        Green = "\033[32m"
        Yellow = "\033[33m"
        Reset = "\033[0m"

    class CliMessages:
        InputError_IntegerExpected = f"{AnsiColorCodes.Red}Fehlerhafte Eingabe! Bitte eine ganze Zahl eingeben.{AnsiColorCodes.Reset}"
        InputError_StringIsNullOrEmpty = f"{AnsiColorCodes.Red}Fehlerhafte Eingabe! Die Eingabe darf nicht leer sein.{AnsiColorCodes.Reset}"
        InputError_ExpectedType = f"{AnsiColorCodes.Red}Fehlerhafte Eingabe! Erwartet wird: {expected_type.__name__}.{AnsiColorCodes.Reset}"

    @staticmethod
    def WasCapacityReached(capacity_value: int, number_of_visitors: int) -> bool:
        return number_of_visitors >= capacity_value

    @staticmethod
    def IsNumberOfVisitorsValid(number_of_visitors: int) -> bool:
        return number_of_visitors is not None and number_of_visitors >= 0

    @staticmethod
    def IsCapacityValueValid(capacity_value: int) -> bool:
        return capacity_value is not None and capacity_value > 0

    @staticmethod
    def ValidateData(capacity_value: int, number_of_visitors: int) -> bool:
        if (not HelperClass.IsCapacityValueValid(capacity_value)
                or not HelperClass.IsNumberOfVisitorsValid(number_of_visitors)):
            return False
        return not HelperClass.WasCapacityReached(capacity_value, number_of_visitors)

    @staticmethod
    def GetValidInput(prompt: str, expected_type: type):
        while True:
            user_input = input(prompt).strip()
            if expected_type == int:
                if user_input.isdigit():
                    return int(user_input)
                print(CliMessages.InputError_IntegerExpected)
            elif expected_type == str:
                if user_input != "" or user_input is not None: ## Falls der Benutzer Strg + D drückt => EOF => null
                    return user_input
                print(CliMessages.InputError_StringIsNullOrEmpty)
            else:
                print(CliMessages.InputError_ExpectedType)
