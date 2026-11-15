---
name: trading-backtesting-engine
description: Quantitative backtesting engine and portfolio performance analytics with slippage modeling, Sharpe ratio, Max Drawdown, and walk-forward verification. Use when verifying trading strategies, assessing risk-adjusted returns, or preventing overfitting.
metadata:
  version: "1.0.0"
  author: HyperCraft Core Team
  license: Apache-2.0
---

# Quantitative Backtesting & Strategy Verification

A profitable strategy on historical data often fails in production due to three critical errors: **look-ahead bias**, **survivorship bias**, and **unrealistic execution assumptions** (ignoring fees and slippage).

## Essential Performance Metrics

1. **Sharpe Ratio (Annualized):**
   `Sharpe = ((R_p - R_f) / sigma_p) * sqrt(252)`
   - Benchmarks: > 1.0 (Acceptable), > 1.5 (Strong), > 2.0 (Elite).
2. **Sortino Ratio:** Penalizes only downside volatility.
3. **Maximum Drawdown (MDD):** Peak-to-trough decline in portfolio equity.
4. **Profit Factor:** Gross Profits / Gross Losses. (Must be > 1.30 for production).
5. **Win Rate & Payoff Ratio:**
   `Expectancy = (Win Rate * Avg Win) - (Loss Rate * Avg Loss)`

---

## Golden Rules for Robust Backtesting

- **Zero Look-Ahead Bias:** Signals generated at bar t execute at earliest on t+1 Open or t Close with realistic latency offset.
- **Explicit Fee & Slippage Modeling:** Always deduct round-trip exchange fees (e.g. 0.05% maker / 0.10% taker) plus dynamic slippage.
- **Walk-Forward Validation:** Optimize parameters on In-Sample (60%) data, then test strictly Out-of-Sample (40%). Never fit on the full dataset.

---

## Production Backtesting Script

```python
import numpy as np
import pandas as pd

class BacktestEngine:
    def __init__(self, initial_capital: float = 10000.0, fee_rate: float = 0.0006, slippage_bps: float = 5.0):
        self.initial_capital = initial_capital
        self.fee_rate = fee_rate
        self.slippage = slippage_bps / 10000.0

    def run(self, df: pd.DataFrame, signal_col: str = 'signal') -> dict:
        data = df.copy()
        data['position'] = data[signal_col].shift(1).fillna(0)
        data['market_return'] = data['close'].pct_change().fillna(0)
        data['strategy_return'] = data['position'] * data['market_return']
        
        trades = data['position'].diff().abs().fillna(0)
        costs = trades * (self.fee_rate + self.slippage)
        data['net_return'] = data['strategy_return'] - costs
        
        data['equity'] = self.initial_capital * (1 + data['net_return']).cumprod()
        data['peak'] = data['equity'].cummax()
        data['drawdown'] = (data['peak'] - data['equity']) / data['peak']
        
        total_return = (data['equity'].iloc[-1] - self.initial_capital) / self.initial_capital
        max_dd = data['drawdown'].max()
        daily_returns = data['net_return']
        
        std = daily_returns.std()
        sharpe = (daily_returns.mean() / (std + 1e-10)) * np.sqrt(252) if std > 0 else 0
        
        return {
            'final_equity': round(data['equity'].iloc[-1], 2),
            'total_return_pct': round(total_return * 100, 2),
            'max_drawdown_pct': round(max_dd * 100, 2),
            'annualized_sharpe': round(sharpe, 2),
            'total_trades': int(trades.sum())
        }
```
