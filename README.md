# Market Basket Analysis — Real-Time Recommendations
[![CI](https://github.com/deepanshu0110/market-basket-analysis/actions/workflows/ci.yml/badge.svg)](https://github.com/deepanshu0110/market-basket-analysis/actions)

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

Mines transaction data for product association rules and serves cross-sell recommendations via a REST API.

**Data note:** `create_sample_data.py` generates 1,000 synthetic grocery transactions. The rules in `results/` come from that synthetic data.

---

## Business Problem

Customers leave revenue on the table when complementary products go unnoticed. Association rule mining finds item pairs that co-occur frequently — enabling targeted upsell at checkout.

---

## API

```bash
POST /recommend
{ "cart_items": ["bread"], "max_recommendations": 5, "min_confidence": 0.3 }
# Returns recommendations, each with item, confidence, lift, support and an explanation.
# Example rule from the committed results: bread → butter (confidence 0.75, lift 1.61)
```

---

## Quickstart

```bash
git clone https://github.com/deepanshu0110/market-basket-analysis.git
cd market-basket-analysis
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python create_sample_data.py
python market_basket_analysis.py
uvicorn realtime_api:app --reload --port 8000
```

---

## Tech Stack

Python · Pandas · MLxtend · FastAPI · Plotly · NetworkX

---

## Author

**Deepanshu Garg** — Freelance Data Scientist
- GitHub: [@deepanshu0110](https://github.com/deepanshu0110)
- Hire: [freelancer.com/u/deepanshu0110](https://www.freelancer.com/u/deepanshu0110)

MIT License