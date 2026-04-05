name: BLS Bot

on:
  schedule:
    - cron: "*/5 * * * *"  # toutes les 5 minutes
  workflow_dispatch:

jobs:
  run-bot:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Install dependencies
        run: |
          pip install selenium requests webdriver-manager

      - name: Run bot
        run: python bot.py
