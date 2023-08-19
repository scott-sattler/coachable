from dataclasses import dataclass


@dataclass
class GenericTC:
    input_data: any
    expected: any

    def __repr__(self):
        return f"({self.input_data}, {self.expected})"

    def __hash__(self):
        return hash(self.__repr__())


@dataclass
class TestCase:
    pattern: str
    text: str
    match_index: list[int]

    def __repr__(self):
        return f"('{self.pattern}', '{self.text}', {self.match_index})"

    def __hash__(self):
        return hash(self.__repr__())


@dataclass
class Results:
    test_case: any = None
    result: any = None
    passed: bool = None

    def __repr__(self):
        return f"({self.test_case}, {self.result}, {self.passed})"

    def __hash__(self):
        return hash(self.__repr__())
