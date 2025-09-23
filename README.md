# Market Basket Analysis — Real‑Time Recommendations

A beginner‑friendly project that analyzes transaction data to discover association rules (Apriori) and serves real‑time product recommendations via a simple API. It also includes scripts for data preprocessing, rule mining, visualization, and an API client/CLI that prints a compact table with confidence, lift, price, and natural‑language explanations.

> Built for Python 3.9+ and tested locally on Windows with VS Code.

---

## Folder Structure

```
MARKET_BASKET_ANALYSIS/
├─ data/                         # Raw & sample CSVs (e.g., groceries.csv)
├─ results/
│  ├─ plots/                     # Exported charts
│  ├─ *.csv                      # Derived datasets & reports (rules, segments, etc.)
│  └─ *.md                       # Generated analysis reports
├─ src/
│  ├─ data_preprocessing.py      # cleans/aggregates transactions
│  ├─ market_basket_analyzer.py  # association rules (Apriori / FP-Growth style)
│  ├─ visualizations.py          # charts for support/lift/network, etc.
│  ├─ advanced_analysis.py       # (optional) segments, seasonality, RFM extras
│  ├─ realtime_api.py            # FastAPI (or aiohttp) service exposing /recommend
│  ├─ api_client.py              # CLI client for the running API
│  └─ explore_results.py         # quick exploration of mined rules
├─ requirements.txt
└─ README.md
```

> Names are based on the screenshot you provided; adjust if your local filenames differ.

---

## Quick Start

### 1) Create and activate a virtual environment
```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

> If you use VS Code, select the **.venv** interpreter (bottom-right status bar) and install the **Python** extension.

---

## Data

Place your transactional data (CSV) in `data/`. For first runs you can use `data/groceries.csv` (or `create_sample_data.py` to synthesize sample baskets). Expected minimal schema:

- `transaction_id` (str/int)
- `item` (str)
- `timestamp` (optional, for seasonality / trends)
- `price` (optional, improves explanations)

---

## Offline Analysis Workflow

Run the steps below in order—or execute the individual scripts as needed.

```bash
# 1) Clean and prepare data
python -m src.data_preprocessing

# 2) Mine frequent itemsets & association rules
python -m src.market_basket_analyzer

# 3) (Optional) Extra analytics
python -m src.advanced_analysis

# 4) Visualize results & export charts
python -m src.visualizations

# 5) Explore outputs
python -m src.explore_results
```

Outputs will be saved under `results/` (e.g., `association_rules.csv`, `frequent_itemsets.csv`, `enhanced_transactions.csv`, plots in `results/plots/`, and markdown summaries such as `analysis_report.md`).

---

## Real‑Time API

The API exposes a simple endpoint for recommendations based on the items in a cart. By default it runs on `http://localhost:8000`.

### Run the API

If `realtime_api.py` is a FastAPI app named `app`:
```bash
uvicorn src.realtime_api:app --host 0.0.0.0 --port 8000 --reload
```

(If you’re using `aiohttp`/`Flask`, run the equivalent entry‑point; the default base URL in the client is `http://localhost:8000`.)

### Endpoint (example)

- `POST /recommend`
  - **Body**: `{"items": ["bread", "eggs", "milk"]}`
  - **Response**: top N recommendations with confidence, lift, optional price, and a short explanation

> Make sure your rules (`results/association_rules.csv`) exist before starting the API.

---

## API Client / CLI

Use the included client to test recommendations interactively:

```bash
python -m src.api_client
```

When prompted, enter items comma‑separated (e.g., `bread, eggs`), or type `sample` to use predefined examples. The client renders a table like:

```
Item    Confidence  Lift  Price  Explanation
Butter  75.0%       1.61  $3.49  Customers who buy bread often also buy this
...
```

To change the server URL, edit `base_url` in `src/api_client.py` or pass an ENV variable if implemented.

---

## Configuration

Create a `.env` file if you want to override defaults:

```
API_HOST=0.0.0.0
API_PORT=8000
MODEL_TOP_N=5
MIN_SUPPORT=0.01
MIN_CONFIDENCE=0.3
```

(Only include keys that your scripts actually read.)

---

## Testing (optional)

You can add quick smoke tests with `pytest`:

```
tests/
  test_rules_exist.py   # ensures association_rules.csv is produced
  test_api_heartbeat.py # requests GET /health if implemented
```

Run:
```bash
pytest -q
```

---

## Tips & Troubleshooting

- **No recommendations?** Increase data size or lower `MIN_SUPPORT` / `MIN_CONFIDENCE` in your analyzer.
- **Long runtimes?** Use pruning or limit max antecedent length.
- **Unicode paths on Windows:** keep project path short (e.g., `C:\work\mba`).
- **VS Code terminal Python mismatch:** confirm the selected interpreter matches your `.venv`.
- **Port already in use:** change `--port` in the API run command or stop the conflicting process.

---

## License

This project is released under the MIT License (see `LICENSE`).

## Citation / Credits

If you adapt this template in a paper/blog, a link back to this repo is appreciated. 🙌
