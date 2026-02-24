from __future__ import annotations
from typing import TypeVar, Type, final

T = TypeVar("T", int, str)


class HelperClass:
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
        def expected_type(t: type) -> str:
            return (
                f"{HelperClass.AnsiColorCodes.Red}"
                f"Fehlerhafte Eingabe! Erwartet wird: {t.__name__}."
                f"{HelperClass.AnsiColorCodes.Reset}"
            )

    @staticmethod
    def WasCapacityReached(capacity_value: int, number_of_visitors: int) -> bool:
        return number_of_visitors >= capacity_value

    @staticmethod
    def IsNumberOfVisitorsValid(number_of_visitors: int) -> bool:
        return number_of_visitors >= 0  # int can never be None, removed redundant check

    @staticmethod
    def IsCapacityValueValid(capacity_value: int) -> bool:
        return capacity_value > 0  # same

    @staticmethod
    def ValidateData(capacity_value: int, number_of_visitors: int) -> bool:
        if (not HelperClass.IsCapacityValueValid(capacity_value)
                or not HelperClass.IsNumberOfVisitorsValid(number_of_visitors)):
            return False
        return not HelperClass.WasCapacityReached(capacity_value, number_of_visitors)

    @staticmethod
    def GetValidInput(prompt: str, expected_type: Type[T]) -> T:
        while True:
            user_input: str = input(prompt).strip()
            if expected_type is int:
                if user_input.isdigit():
                    return int(user_input)  # type: ignore[return-value]
                print(HelperClass.CliMessages.integer_expected())
            elif expected_type is str:
                if user_input:
                    return user_input  # type: ignore[return-value]
                print(HelperClass.CliMessages.string_empty())
            else:
                print(HelperClass.CliMessages.expected_type(expected_type))
