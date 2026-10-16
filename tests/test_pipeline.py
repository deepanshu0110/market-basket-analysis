import sys

import pandas as pd

from tests.helpers import ROOT, run_script


def test_rules_are_mined():
    run_script("create_sample_data.py")
    run_script("market_basket_analysis.py")
    rules = pd.read_csv(ROOT / "results" / "association_rules.csv")
    assert len(rules) > 0
    assert rules["confidence"].between(0, 1).all()
    assert (rules["lift"] > 0).all()


def test_api_recommends_for_cart():
    from fastapi.testclient import TestClient

    sys.path.insert(0, str(ROOT))
    import realtime_api

    with TestClient(realtime_api.app) as client:
        response = client.post("/recommend", json={"cart_items": ["bread"]})
        assert response.status_code == 200
        recs = response.json()["recommendations"]
        assert recs, "expected at least one recommendation for bread"
        assert all(0 <= r["confidence"] <= 1 for r in recs)
