from __future__ import annotations

from whenever import TimeDelta


def test_main() -> None:
    TimeDelta.parse_common_iso("PT0.001")
