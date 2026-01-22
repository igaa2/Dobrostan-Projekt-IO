from dataclasses import dataclass
from typing import Any, Literal


@dataclass(frozen=True)
class DataParams:
    unit_level: Literal[0, 2, 5]
    format: Literal["json", "xml"]
    page_size: int

    def __post_init__(self):
        if self.unit_level not in (0, 2, 5):
            raise ValueError("unit-level must be 0, 2, or 5")

        if self.format not in ("json", "xml"):
            raise ValueError("format must be 'json' or 'xml'")

        if not (0 <= self.page_size <= 100):
            raise ValueError("page-size must be between 0 and 100")

    @classmethod
    def from_dict(cls, dictionary: dict[str, Any]) -> "DataParams":
        """Tworzy DataParams z dicta."""

        required = {"unit-level", "format", "page-size"}
        missing = required - dictionary.keys()
        if missing:
            raise KeyError(f"Missing keys in dictionary: {missing}")

        return cls(
            unit_level=dictionary["unit-level"],
            format=dictionary["format"],
            page_size=dictionary["page-size"],
        )

    def to_dict(self) -> dict:
        return {
            "level": self.unit_level,
            "unit-level": self.unit_level,
            "format": self.format,
            "page-size": self.page_size,
        }
