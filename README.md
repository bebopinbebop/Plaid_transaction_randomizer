# Plaid Transaction Randomizer

Generate a fake set of Plaid-like transaction objects (200 by default) with randomized **dates (last ~6 months)**, **amounts ($10–$200)**, and **merchant logo/name pairs**, then save them to `transactions.json` sorted newest → oldest.

This is used for test data when testing the **Plaid API:
- mocking transaction feeds in a UI
- testing filters/search/categories
- demo data for mvp

> Note: This repo **does not call Plaid**. It just produces JSON shaped similarly to Plaid transactions after studying the API deliveriables. :contentReference[oaicite:1]{index=1}

---

## What’s in this repo

- `plaid_randomize_transactions.py` — main generator script :contentReference[oaicite:2]{index=2}  
- `seed_transaction.json` — a “template-ish” example transaction object (reference sample) :contentReference[oaicite:3]{index=3}  
- `transactions.json` — generated output file (created/overwritten by the script) :contentReference[oaicite:4]{index=4}  

---

## How it works (high level)

The script:

1. Defines a mapping of `logo_url -> merchant_name` (Walmart, Uber, Venmo, Netflix, etc.). :contentReference[oaicite:5]{index=5}  
2. Randomizes:
   - `date`: any day from today back ~180 days
   - `amount`: random float from 10.00 to 200.00  
3. Builds 200 transaction objects using the Plaid-ish schema.
4. Sorts them by `"date"` descending (most recent first).
5. Writes them to `transactions.json`.

---

## Requirements

- Python 3.x

No external packages required (only standard library: `json`, `random`, `datetime`). :contentReference[oaicite:6]{index=6}

---

## Quick start

Clone the repo and run:

```bash
python3 plaid_randomize_transactions.py
