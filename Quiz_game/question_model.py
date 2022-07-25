# Question class
class Question:
    """
    The base of th equestion model
    """
    def __init__(self, text: str, answer: bool) -> None:
        self.text = text
        self.answer = answer

    def __str__(self) -> str:
        return f"{self.text} - {self.answer}"