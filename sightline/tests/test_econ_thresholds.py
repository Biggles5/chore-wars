"""The kill thresholds, encoded as failing tests.

Addendum 1: blended CAC under $1,000; monitoring marginal cost under
$6/home/month; blended gross margin over 60%; attrition never better than
8% without a cited justification.

Addendum 2: modeled install under 3.5 crew hours on site (single story,
the crew's wall-clock duration); installer productive by job 3; first-pass
QC over 85% by job 5; callback rate under 5%; a metro reaches 100
installs/month of capacity within 90 days on the modeled funnel alone.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "econ"))

import throughput as tp  # noqa: E402
import unit_economics as ue  # noqa: E402


# ---- Addendum 1 thresholds ----

def test_blended_cac_under_1000():
    assert ue.blended_cac() < 1000, "the whole thesis dies here"
    for name in ue.SCENARIOS:
        assert ue.run_scenario(name)["cac"] < 1000


def test_monitoring_marginal_under_6():
    b = ue.blended()
    assert b["marginal_cost_mo"] < 6.0, b
    for plan in ("plus",):
        assert ue.monitoring_marginal_cost_mo(plan) < 6.0
    # shield carries the $5.99 wholesale station pass-through; the AGENT'S
    # own marginal cost must still be single-digit-cents class
    assert ue.COST_TO_SERVE["guardian_compute_mo"] < 1.0


def test_blended_margin_over_60():
    assert ue.blended()["margin_pct"] > 60.0
    for name in ("dealer-led", "insurer-led"):
        assert ue.run_scenario(name)["blended"]["margin_pct"] > 60.0


def test_attrition_floor_enforced():
    with pytest.raises(ValueError):
        ue.ltv(0.05)
    ok = ue.ltv(0.05, justification="hypothetical: cited pilot data would go here")
    assert ok["justification"]
    assert ue.ATTRITION_SCENARIOS["base"] >= ue.ATTRITION_FLOOR


def test_scenarios_all_run():
    for name in ue.SCENARIOS:
        r = ue.run_scenario(name)
        assert r["ltv_to_cac"] > 3.0, f"{name} below venture bar"


# ---- Addendum 2 thresholds ----

def test_install_under_3p5_hours_on_site():
    assert tp.install_hours("new") < 3.5
    assert tp.install_hours("old") > 7.0  # the baseline we beat


def test_installer_productive_by_job_3():
    assert tp.job_hours_at(3) < 3.5, "half-day cert must beat a season of apprenticeship"


def test_qc_first_pass_over_85_by_job_5():
    assert tp.qc_first_pass_at(5) > 0.85


def test_callback_rate_under_5pct():
    assert tp.CALLBACK_RATE_NEW < 0.05


def test_metro_100_installs_within_90_days():
    months = tp.metro_capacity(3)
    assert months[-1]["capacity_installs_mo"] >= 100, months[-1]


def test_throughput_gap_is_the_thesis():
    ie = tp.install_economics()
    assert ie["new_model"]["jobs_per_day"] >= 3 * ie["old_model"]["jobs_per_day"]
    assert ie["new_model"]["cost_with_callbacks"] < ie["old_model"]["cost_with_callbacks"]
    assert ie["installer_earnings"]["margin_per_crew_day"] > 500  # the recruiting pitch


def test_reports_generate(tmp_path, monkeypatch):
    import report
    monkeypatch.setattr(report, "OUT", tmp_path)
    report.main()
    for name in ("dealer-led", "insurer-led", "licensing-pivot", "throughput"):
        html = (tmp_path / f"{name}.html").read_text()
        assert "—" not in html, "no em dashes, even generated"
        assert "SightLine" in html
