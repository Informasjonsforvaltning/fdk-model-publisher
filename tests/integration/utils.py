"""Integration test utils."""


def get_skolem(base_url: str, count: int) -> str:
    """Get skolem according to base URL."""
    return base_url + ".well-known/skolem/" + str(count)


class SkolemUtils:
    """Testutils for mocking more than one skolemization."""

    skolemization_counter: int
    base_url: str

    def __init__(self, base_url: str) -> None:
        """Set up skolem utils."""
        self.skolemization_counter = 0
        self.base_url = base_url

    def get_skolemization(self) -> str:
        """Pops a skolemization from a stack of max 3 test skolemizations."""
        _skolemization = get_skolem(self.base_url, self.skolemization_counter)
        self.skolemization_counter = self.skolemization_counter + 1

        return _skolemization

    def reset_counter(self) -> None:
        """Reset skolemization counter."""
        self.skolemization_counter = 0
