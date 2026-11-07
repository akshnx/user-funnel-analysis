"""Central configuration for FunnelLens.

Everything that changes the *meaning* of a metric lives here so the
definitions are easy to find, explain and tweak.
"""

APP_NAME = "FunnelLens"
APP_TAGLINE = "E-commerce funnel analytics"
USER_NAME = "Analyst"

# ---------------------------------------------------------------------------
# Funnel definition
# ---------------------------------------------------------------------------
# "Engaged" = users who viewed at least N distinct products in the period.
# Set ENGAGED_ENABLED = False to get the plain View -> Cart -> Purchase funnel.
ENGAGED_ENABLED = True
ENGAGED_MIN_DISTINCT_PRODUCTS = 2

# Strict funnel: a user only counts at a stage if they also reached every
# previous stage (so percentages can never exceed 100%).
# Non-strict: each stage is simply the unique users who did that action.
FUNNEL_STRICT = True

STAGE_LABELS = {
    "visits": "Visits",
    "engaged": "Engaged",
    "cart": "Cart",
    "purchase": "Purchase",
}

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------
REQUIRED_COLUMNS = ["event_time", "event_type", "product_id", "user_id"]
OPTIONAL_COLUMNS = ["category_id", "category_code", "brand", "price", "user_session"]
VALID_EVENT_TYPES = ["view", "cart", "remove_from_cart", "purchase"]

# Safety cap for very large REES46 files (the full months are several GB).
# None = no cap.
MAX_UPLOAD_ROWS = 3_000_000

# Synthetic sample data (REES46-shaped)
SAMPLE_SEED = 46
SAMPLE_START = "2019-10-01"
SAMPLE_DAYS = 61
SAMPLE_SESSIONS = 70_000
SAMPLE_USERS = 30_000

# ---------------------------------------------------------------------------
# Filters
# ---------------------------------------------------------------------------
DATE_PRESETS = ["Last 7 days", "Last 30 days", "All data", "Custom"]
DEFAULT_PRESET = "Last 30 days"
ALL_CATEGORIES = "All categories"

PAGE_SUBTITLES = {
    "Overview": "Your store's funnel at a glance",
    "Funnel": "Where visitors drop off, stage by stage",
    "Segmentation": "Compare categories, brands and time slots",
    "Time Analysis": "How long it takes visitors to convert",
    "Insights": "Automated, rule-based findings from your data",
    "Data": "Upload a REES46-style CSV and review cleaning",
}
