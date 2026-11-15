---
name: trading-sentiment-intelligence
description: Market sentiment, funding rates, open interest, Fear & Greed index, on-chain whale activity, and economic calendar risk gating. Use when auditing crowd sentiment, detecting perpetual squeeze conditions, or dodging high-impact news spikes.
metadata:
  version: "1.0.0"
  author: HyperCraft Core Team
  license: Apache-2.0
---

# Market Sentiment & On-Chain Intelligence

Markets are driven by liquidity and human emotion. This skill provides systematic sentiment ingestion, perpetual funding rate analysis (detecting short/long squeezes), and high-impact macro calendar gating.

## Core Metrics & Signals

1. **Crypto Fear & Greed Index:**
   - 0 - 25: Extreme Fear (Contrarian buying opportunities).
   - 75 - 100: Extreme Greed (High probability of local top / liquidation cascade).
2. **Perpetual Funding Rates:**
   - Highly positive funding (> 0.03% per 8h): Retail is overly leveraged long. Risk of long squeeze.
   - Deeply negative funding (< -0.03% per 8h): Overly aggressive shorting. Prime condition for short squeeze.
3. **Macro News Gating:**
   - Freeze all automated entries 15 minutes before and 30 minutes after:
     - FOMC Interest Rate Decisions & Fed Chair Speeches
     - US CPI (Consumer Price Index) & Core Inflation
     - US Non-Farm Payrolls (NFP)

---

## Production Sentiment Fetcher

```python
import urllib.request
import json
from typing import Dict, Any

def get_fear_and_greed_index() -> Dict[str, Any]:
    url = "https://api.alternative.me/fng/?limit=1"
    req = urllib.request.Request(url, headers={'User-Agent': 'HyperCraft-Quant'})
    
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            entry = data['data'][0]
            return {
                'value': int(entry['value']),
                'classification': entry['value_classification'],
                'timestamp': entry['timestamp']
            }
    except Exception as e:
        return {'value': 50, 'classification': 'Neutral', 'error': str(e)}
```
