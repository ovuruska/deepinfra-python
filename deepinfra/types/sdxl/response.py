from typing import List

from dataclasses import dataclass


@dataclass
class SdxlResponseItem:
    format: str
    type: str


@dataclass
class SdxlResponse:
    items: List[SdxlResponseItem]
    title: str
    type: str
