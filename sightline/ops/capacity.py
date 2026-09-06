"""Capacity + scheduling engine: the installer network as software.

Certified contractors, not employees. Job intake matches jobs to crews by
tier, rating, and route proximity; the forecaster answers "how many
certified crews does metro X need for Y installs/month" and how fast the
recruitment funnel gets there (econ/throughput.py owns the funnel math).

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import math
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "econ"))
import throughput as tp  # noqa: E402

TIER_ORDER = {"elite": 0, "pro": 1, "certified": 2}
MAX_DAY_HOURS = 9.0
ROUTE_SPEED_MPH = 28.0  # metro driving with ladders (est.)


@dataclass
class Crew:
    id: str
    tier: str = "certified"           # certified | pro | elite
    rating: float = 4.6               # homeowner rating, 5-max
    home_base: tuple = (0.0, 0.0)     # miles, metro frame
    jobs_done: int = 0
    schedule: dict = field(default_factory=dict)   # day -> [jobs]

    def day_hours(self, day: int) -> float:
        return sum(j["est_hours"] for j in self.schedule.get(day, []))


@dataclass
class Job:
    id: str
    site: tuple                       # miles, metro frame
    earliest_day: int
    est_hours: float = None           # from the crew's learning curve at match time
    assigned: str = None
    day: int = None


def travel_hours(a: tuple, b: tuple) -> float:
    return math.dist(a, b) / ROUTE_SPEED_MPH


def match_score(crew: Crew, job: Job, day: int) -> float:
    """Lower is better: tier priority, then route distance from the day's
    last stop (route-aware), then rating (better crews first on ties)."""
    stops = crew.schedule.get(day, [])
    last = stops[-1]["site"] if stops else crew.home_base
    dist = math.dist(last, job.site)
    return TIER_ORDER[crew.tier] * 100 + dist * 2 - crew.rating


def schedule_jobs(crews: list, jobs: list, horizon_days: int = 10) -> dict:
    """Greedy route-aware slotting. Returns summary; mutates crews/jobs."""
    unplaced = []
    for job in sorted(jobs, key=lambda j: j.earliest_day):
        placed = False
        for day in range(job.earliest_day, horizon_days):
            candidates = sorted(crews, key=lambda c: match_score(c, job, day))
            for crew in candidates:
                hours = tp.job_hours_at(crew.jobs_done + 1)
                stops = crew.schedule.get(day, [])
                last = stops[-1]["site"] if stops else crew.home_base
                total = crew.day_hours(day) + hours + travel_hours(last, job.site)
                if total <= MAX_DAY_HOURS:
                    crew.schedule.setdefault(day, []).append(
                        {"job": job.id, "site": job.site, "est_hours": hours})
                    crew.jobs_done += 1
                    job.assigned, job.day, job.est_hours = crew.id, day, hours
                    placed = True
                    break
            if placed:
                break
        if not placed:
            unplaced.append(job.id)
    scheduled = [j for j in jobs if j.assigned]
    return {
        "scheduled": len(scheduled),
        "unplaced": unplaced,
        "avg_est_hours": round(sum(j.est_hours for j in scheduled)
                               / max(len(scheduled), 1), 2),
        "crew_days_used": sum(len(c.schedule) for c in crews),
    }


def crews_needed(installs_per_month: float) -> dict:
    """The forecaster: 'metro X wants Y installs/month, how many crews.'"""
    per_crew = tp.crew_capacity_per_month()
    need = installs_per_month / per_crew
    add_rate = tp.crews_certified_per_month()
    return {
        "installs_per_month": installs_per_month,
        "capacity_per_crew_mo": round(per_crew, 1),
        "crews_needed": math.ceil(need),
        "crews_certified_per_month_from_funnel": round(add_rate, 1),
        "months_to_capacity": math.ceil(need / add_rate),
        "note": "funnel constants in econ/throughput.py; utilization 65% (est.)",
    }


if __name__ == "__main__":
    import json
    import random
    rng = random.Random(7)
    crews = [Crew(id=f"crew-{i}", tier=t, home_base=(rng.uniform(0, 18), rng.uniform(0, 18)),
                  jobs_done=rng.randint(0, 20))
             for i, t in enumerate(["elite", "pro", "certified", "certified"])]
    jobs = [Job(id=f"job-{i}", site=(rng.uniform(0, 18), rng.uniform(0, 18)),
                earliest_day=rng.randint(0, 3)) for i in range(30)]
    print(json.dumps(schedule_jobs(crews, jobs), indent=2))
    print(json.dumps(crews_needed(100), indent=2))
