"""Minimal CodSpeed benchmarks for CI (pytest-codspeed)."""

from __future__ import annotations

from dns_manager.model import Record
from dns_manager.utils import generate_record


def test_generate_record_static_ipv4(benchmark) -> None:
    record = benchmark(generate_record, "home", "192.0.2.10")
    assert record.type == "A"
    assert record.value == "192.0.2.10"


def test_record_normalize_ipv6(benchmark) -> None:
    record = benchmark(
        Record,
        subdomain="home",
        value="2001:0DB8:0000:0000:0000:0000:0000:0001",
        type="AAAA",
    )
    assert record.type == "AAAA"
    assert record.value == "2001:db8::1"
