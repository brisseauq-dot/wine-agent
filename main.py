"""
main.py - Orchestrateur principal
"""
import asyncio, json, sys, argparse
from pathlib import Path
from datetime import datetime
sys.path.insert(0, str(Path(__file__).parent / "scraper"))
from scraper.catawiki_scraper import scrape_catawiki
from scraper.wine_searcher import enrich_lots_with_prices
from scraper.price_calculator import classify_all_lots
from alerts.telegram_alert import process_urgent_alerts, send_daily_summary

DATA_DIR = Path("data")
OUTPUT_JSON = DATA_DIR / "auctions.json"
HISTORY_FILE = DATA_DIR / "history.json"


def save_json(data, path):
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def update_history(report):
    history = []
    if HISTORY_FILE.exists():
        try: history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except: pass
    today = datetime.now().strftime("%Y-%m-%d")
    for lot in report.get("alertes", []):
        history.append({"date": today, "title": lot.get("title"), "url": lot.get("url"), "real_decote": lot.get("real_decote"), "savings_total": lot.get("savings_total"), "status": "manquée"})
    save_json(history[-500:], HISTORY_FILE)


def generate_dashboard(report):
    t = Path("dashboard/index.html")
    if not t.exists(): return
    html = t.read_text(encoding="utf-8").replace("/* DATA_PLACEHOLDER */", f"const AUCTION_DATA = {json.dumps(report, ensure_ascii=False)};")
    (DATA_DIR / "dashboard.html").write_text(html, encoding="utf-8")


async def run(headless=True, send_telegram=True, daily_summary=False, urgent_only=False):
    print(f"\n{'='*60}\n  AGENT ENCHÈRES VIN — {datetime.now().strftime('%d/%m/%Y %H:%M')}\n{'='*60}\n")
    raw_lots = await scrape_catawiki(headless=headless)
    if not raw_lots: return
    enriched = enrich_lots_with_prices(raw_lots)
    report = classify_all_lots(enriched)
    s = report["stats"]
    print(f"  ✓ ALERTES: {s['alertes_count']} ({s['urgentes_count']} urgentes) | PIÈGES: {s['pieges_count']} | ÉCONOmie: {s['total_savings_eur']}€")
    save_json(report, OUTPUT_JSON)
    update_history(report)
    generate_dashboard(report)
    if send_telegram:
        if urgent_only or not daily_summary: process_urgent_alerts(report)
        if daily_summary: send_daily_summary(report)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--no-headless", action="store_true")
    p.add_argument("--no-telegram", action="store_true")
    p.add_argument("--daily-summary", action="store_true")
    p.add_argument("--urgent-only", action="store_true")
    a = p.parse_args()
    asyncio.run(run(headless=not a.no_headless, send_telegram=not a.no_telegram, daily_summary=a.daily_summary, urgent_only=a.urgent_only))

if __name__ == "__main__": main()
