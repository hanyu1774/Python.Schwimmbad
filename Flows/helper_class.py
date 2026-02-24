from __future__ import annotations
from typing import final, overload

class HelperClass:
    # Laut Clean Code über static, sollen mittels static
    # keine objekt-spezifischen oder globale Änderungen gemacht werden.
    # Diese Klasse dient für Utility-Zwecke, die man
    # global nutzen kann.
    # In Python gibt es keine Zugriffsmodifikationen wie public, private, readonly etc..

    @final
    class AnsiColorCodes:
        Red:    str = "\033[31m"
        Green:  str = "\033[32m"
        Yellow: str = "\033[33m"
        Reset:  str = "\033[0m"

    class CliMessages:
        @staticmethod
        def integer_expected() -> str:
            return (
                f"{HelperClass.AnsiColorCodes.Red}"
                f"Fehlerhafte Eingabe! Bitte eine ganze Zahl eingeben."
                f"{HelperClass.AnsiColorCodes.Reset}"
            )

        @staticmethod
        def string_empty() -> str:
            return (
                f"{HelperClass.AnsiColorCodes.Red}"
                f"Fehlerhafte Eingabe! Die Eingabe darf nicht leer sein."
                f"{HelperClass.AnsiColorCodes.Reset}"
            )

        @staticmethod
        def give_error_message_with_argument(condition: str = "") -> str:
            output_message = f"{HelperClass.AnsiColorCodes.Red}Fehlerhafte Eingabe!"
            if(condition == ""):
                return (
                    f"{output_message}{HelperClass.AnsiColorCodes.Reset}"
                )
            return (
                f"{output_message} {condition} {HelperClass.AnsiColorCodes.Reset}"
            )
                
        @staticmethod
        def expected_type(type: type) -> str:
            return (
                f"{HelperClass.AnsiColorCodes.Red}"
                f"Fehlerhafte Eingabe! Erwartet wird: {type.__name__}."
                f"{HelperClass.AnsiColorCodes.Reset}"
            )

    @staticmethod
    def WasCapacityReached(capacity_value: int, number_of_visitors: int) -> bool:
        return number_of_visitors >= capacity_value

    @staticmethod
    def IsNumberOfVisitorsValid(number_of_visitors: int) -> bool:
        return number_of_visitors >= 0

    @staticmethod
    def IsCapacityValueValid(capacity_value: int) -> bool:
        return capacity_value > 0

    @staticmethod
    def ValidateData(capacity_value: int, number_of_visitors: int) -> bool:
        if (not HelperClass.IsCapacityValueValid(capacity_value)
                or not HelperClass.IsNumberOfVisitorsValid(number_of_visitors)):
            return False
        return not HelperClass.WasCapacityReached(capacity_value, number_of_visitors)


    # Overloading wie in C#
    # Beispiel:
    # public int Methode() {}
    # public double Methode() {}
    @staticmethod
    @overload
    def GetValidInput(prompt: str, expected_type: type[int]) -> int: ...
    @staticmethod
    @overload
    def GetValidInput(prompt: str, expected_type: type[str]) -> str: ...
    @staticmethod
    def GetValidInput(prompt: str, expected_type: type[int] | type[str]) -> int | str:
        while True:
            user_input: str = input(prompt).strip()
            if expected_type is int:
                if user_input.isdigit():
                    return int(user_input)
                print(HelperClass.CliMessages.integer_expected())
            elif expected_type is str:
                if user_input:
                    return user_input
                print(HelperClass.CliMessages.string_empty())
            else:
                print(HelperClass.CliMessages.expected_type(expected_type))
