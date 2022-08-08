from __future__ import annotations

import json

from typing import Any, Dict, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from aiohttp import ClientResponse

def _to_dict(text: str) -> dict:
    """Convert text to dict"""
    return json.loads(text)

async def json_or_text(response: ClientResponse) -> Union[Dict[str, Any], str]:
    text = await response.text(encoding='utf-8')
    if 'Content-Type' in response.headers:
        if response.headers['Content-Type'] == 'application/data':
            return await response.json()

    try:
        return _to_dict(text)
    except (json.JSONDecodeError, TypeError):
        return text

class _MissingSentinel:
    __slots__ = ()

    def __eq__(self, other):
        return False

    def __bool__(self):
        return False

    def __hash__(self):
        return 0

    def __repr__(self):
        return '...'


MISSING: Any = _MissingSentinel()
