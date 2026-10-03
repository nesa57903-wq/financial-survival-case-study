"""Run the whole case study:  python run_pipeline.py        (real Kaggle data)
                             python run_pipeline.py --demo  (FAKE data, code test only)
"""
import argparse

from src import analyze
from src.config import (
    DEMO_PATH, DEMO_REPORT_DIR, PROCESSED_PATH, RAW_PATH, REPORT_DIR,
)
from src.load_clean import clean, load_raw, select_columns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", action="store_true", help="use simulated data to test the code")
    args = ap.parse_args()

    if args.demo:
        from src.make_demo_data import make_demo
        make_demo().to_csv(DEMO_PATH, index=False)
        raw, out_dir = load_raw(DEMO_PATH), DEMO_REPORT_DIR
        print("DEMO MODE: data is simulated. Do not publish these results.")
    else:
        raw, out_dir = load_raw(RAW_PATH), REPORT_DIR

    df, log = clean(select_columns(raw))
    if not args.demo:
        PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(PROCESSED_PATH, index=False)
    analyze.run(df, log, out_dir, demo=args.demo)
    print(f"Done. Results in {out_dir}")


if __name__ == "__main__":
    main()
