from __future__ import annotations

from whenever_bug import __version__


def test_main() -> None:
    TimeDelta.parse_common_iso("PT0.001")
