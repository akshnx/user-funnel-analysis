# FunnelLens

E-commerce funnel analytics dashboard for REES46-style event data
(`event_time, event_type, product_id, category_id, category_code, brand, price, user_id, user_session`).

```bash
pip install -r requirements.txt
streamlit run app.py          # open http://localhost:8501  (add ?demo to auto-load sample data)
```

## Structure

| Path | Purpose |
|---|---|
| `app.py` | Entry point: theme, top navigation (`st.navigation(position="top")`), header + filters |
| `config.py` | Metric definitions (Engaged threshold, strict funnel, presets) |
| `services/data.py` | Synthetic sample data, CSV loading, cleaning, period/category filtering |
| `services/metrics.py` | Funnel, revenue, unique visits, weekday, heatmap, time-to-purchase |
| `services/insights.py` | **Automated insights – rule-based**, no AI model |
| `ui/theme.py` | Design tokens, global CSS, shared Plotly template |
| `ui/components.py` | HTML cards, pills, progress bars, SVG stepped funnel, count-up |
| `ui/layout.py` | Page header, filter bar, data-source controls, empty states |
| `views/*.py` | Overview, Funnel, Segmentation, Time Analysis, Insights, Data |

## Metric definitions

* **Visits** – unique users with any event in the period.
* **Engaged** – users who viewed ≥ 2 distinct products (`ENGAGED_MIN_DISTINCT_PRODUCTS`). Turn off with
  `ENGAGED_ENABLED = False` (or the toggle on the Funnel page) for a plain View → Cart → Purchase funnel.
* **Cart / Purchase** – users with a `cart` / `purchase` event. With `FUNNEL_STRICT = True` a user must also
  have passed every earlier stage.
* **Revenue** – sum of `price` over `purchase` events.
* **Previous period** – the same number of days immediately before the selected range.

The insights panel is **rule-based**: each rule in `services/insights.py` checks a threshold
(e.g. add-to-cart rate < 5 %, cart abandonment ≥ 40 %) and writes a plain-English explanation.
