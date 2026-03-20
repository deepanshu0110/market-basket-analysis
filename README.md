# Market Basket Analysis — Real-Time Recommendations

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square&logo=fastapi)
![Apriori](https://img.shields.io/badge/Algorithm-Apriori-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

Analyzes transaction data to discover association rules (Apriori / FP-Growth) and serves real-time product recommendations via a FastAPI endpoint. Includes scripts for data preprocessing, rule mining, visualization, and a CLI client that outputs confidence, lift, price, and natural-language explanations.

---

## Business Problem

Retail stores lose revenue when customers leave without discovering complementary products. Association rule mining identifies item pairs (e.g., bread + butter) that are frequently bought together, enabling intelligent cross-sell recommendations at checkout.

---

## Features

- Apriori / FP-Growth association rule mining
- Real-time `/recommend` API endpoint via FastAPI
- CLI client with formatted table output (confidence, lift, price)
- Support, confidence, and lift visualization charts
- RFM segmentation and seasonality analysis
- Synthetic data generator for testing

---

## Project Structure

```
market-basket-analysis/
├── data/                          # Raw & sample CSVs
├── results/
│   ├── plots/                     # Charts (support/lift/network)
│   ├── *.csv                      # Mined rules and reports
│   └── *.md                       # Analysis summaries
├── src/
│   ├── data_preprocessing.py      # Clean and aggregate transactions
│   ├── market_basket_analyzer.py  # Association rule engine
│   ├── visualizations.py          # Chart generation
│   ├── advanced_analysis.py       # RFM, seasonality, segments
│   ├── realtime_api.py            # FastAPI recommendation service
│   ├── api_client.py              # CLI client
│   └── explore_results.py         # Quick rule exploration
├── create_sample_data.py          # Generate synthetic baskets
├── requirements.txt
└── README.md
```

---

## Quickstart

```bash
# 1. Clone & setup
git clone https://github.com/deepanshu0110/market-basket-analysis.git
cd market-basket-analysis
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux
pip install -r requirements.txt

# 2. Generate sample data (or place your own CSV in data/)
python create_sample_data.py

# 3. Run analysis
python src/market_basket_analyzer.py

# 4. Start recommendation API
uvicorn src.realtime_api:app --reload --port 8000

# 5. Query recommendations
python src/api_client.py
```

---

## Data Format

Expected minimal CSV schema:

| transaction_id | item |
|---|---|
| 1001 | bread |
| 1001 | butter |
| 1002 | milk |

---

## API Endpoint

```
POST /recommend
{ "items": ["bread", "butter"] }
```

Returns top N associated items with confidence, lift, and explanation.

---

## Tech Stack

Python · Pandas · MLxtend · FastAPI · Plotly · NetworkX

---

## License

MIT License