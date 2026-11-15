---
name: trading-exchange-connectors
description: Unified exchange execution via CCXT for 100+ crypto exchanges and Alpaca API for US equities, with async WebSocket order books and OCO orders. Use when placing orders, streaming live order books, or managing API keys.
metadata:
  version: "1.0.0"
  author: HyperCraft Core Team
  license: Apache-2.0
---

# Unified Exchange & Broker API Connectors

Production-grade exchange execution requires unified abstractions across crypto spot/perpetuals (via CCXT) and equities (via Alpaca), with resilient reconnect logic and precision sizing.

## Supported Architectures

1. **Crypto Exchanges (CCXT):** Binance, Bybit, OKX, Coinbase, Kraken, Gate.io.
2. **Equities & Fractional Crypto:** Alpaca Markets API.
3. **Execution Safety:**
   - Always enforce rate-limiting compliance to prevent HTTP 429 bans.
   - Idempotency keys on order creation to avoid duplicate executions.
   - Use Post-Only limit orders whenever possible to guarantee maker fee tiers.

---

## Production CCXT Connector Implementation

```python
import ccxt
from typing import Optional, Dict, Any

class HyperExchangeConnector:
    def __init__(self, exchange_id: str, api_key: str, api_secret: str, testnet: bool = True):
        exchange_class = getattr(ccxt, exchange_id)
        self.client = exchange_class({
            'apiKey': api_key,
            'secret': api_secret,
            'enableRateLimit': True,
            'options': {'defaultType': 'swap' if exchange_id in ['binance', 'bybit'] else 'spot'}
        })
        if testnet:
            self.client.set_sandbox_mode(True)
        self.client.load_markets()

    def get_ticker_price(self, symbol: str) -> float:
        ticker = self.client.fetch_ticker(symbol)
        return float(ticker['last'])

    def place_bracket_order(
        self,
        symbol: str,
        side: str,
        amount: float,
        entry_price: Optional[float] = None,
        stop_loss_price: Optional[float] = None,
        take_profit_price: Optional[float] = None
    ) -> Dict[str, Any]:
        order_type = 'limit' if entry_price else 'market'
        params = {}
        if stop_loss_price:
            params['stopLoss'] = {'price': stop_loss_price}
        if take_profit_price:
            params['takeProfit'] = {'price': take_profit_price}
            
        order = self.client.create_order(
            symbol=symbol,
            type=order_type,
            side=side,
            amount=amount,
            price=entry_price,
            params=params
        )
        return order

    def cancel_all_orders(self, symbol: str) -> list:
        return self.client.cancel_all_orders(symbol)
```
