from typing import Optional, Dict

from pydantic import BaseModel


class Item(BaseModel):
    id: str
    title: str = None
    params: Optional[Dict[str, str]] = None
