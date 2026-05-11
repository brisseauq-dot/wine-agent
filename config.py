# CONFIGURATION AGENT ENCHÈRES VIN
CATAWIKI_URL = "https://www.catawiki.com/fr/c/443-vins"
WINE_SEARCHER_API_KEY = "VOTRE_CLE_API_WINE_SEARCHER ��MAX_PRICE_PER_BOTTLE = 50
MAX_LOT_SIZE = 6
MONTHLY_BUDGET = 200
CATAWIKI_BUYER_PREMIUM = 0.21
SHIPPING_COSTS = {1: 15, 2: 20, 3: 20, 4: 25, 5: 25, 6: 25}
THRESHOLDS = {"Grand Cru": 60, "Étranger": 50, "Régional": 35}
WEAK_VINTAGE_PENALTY = 10
URGENT_THRESHOLD_HOURS = 2
SCAN_WINDOW_HOURS = 24
EXCLUDED_CATEGORIES = ["champagne", "rosé", "rose", "porto", "cognac", "armagnac", "calvados", "rhum", "whisky", "whiskey", "spiritueux"]
EXCLUDED_FORMATS = ["0,375 l", "0.375l", "demi bouteille", "half bottle"]
WEAK_VINTAGES = {"Bordeaux": [2011, 2013, 2017], "Bourgogne": [2013, 2017, 2021], "Rhône": [2008, 2011, 2013], "Italie": [2014, 2017], "Espagne": [2013, 2016]}
REPORT_HOUR_UTC = 7
GITHUB_PAGES_BRANCH = "gh-pages"
TELEGRAM_BOT_TOKEN = "VOTRE_TOKEN_BOT_TELEGRAM"
TELEGRAM_CHAT_ID = "VOTRE_CHAT_ID"
HISTORY_FILE = "data/history.json"
MAX_HISTORY_ENTRIES = 500
