---
name: trading-risk-management
description: Capital preservation framework: Kelly Criterion position sizing, fixed fractional risk, portfolio heat, correlated asset exposure caps, and automated emergency kill switch. Use when calculating trade sizes, auditing portfolio risk, or setting hard stop levels.
metadata:
  version: "1.0.0"
  author: HyperCraft Core Team
  license: Apache-2.0
---

# Capital Preservation & Position Sizing Framework

Amateur traders focus on entries; professional quantitative systems focus on **position sizing** and **capital preservation**. The goal is never to maximize a single trade, but to maximize geometric portfolio growth while eliminating risk of ruin.

## Core Risk Rules

### 1. Fixed Fractional Risk (The 1% - 2% Rule)
Never risk more than 1% to 2% of total account equity on any single trade:
`Position Size = (Account Equity * Risk %) / abs(Entry Price - Stop Loss Price)`

### 2. The Kelly Criterion
Calculates mathematically optimal fraction of capital to risk:
`f* = (b * p - q) / b`
- p: Probability of winning.
- q = 1 - p: Probability of losing.
- b: Payoff ratio (Avg Win / Avg Loss).
- **Rule:** Never use Full Kelly. Always use **Quarter-Kelly** (f* / 4) or **Half-Kelly** (f* / 2).

### 3. Portfolio Heat & Correlation Caps
- **Max Portfolio Heat:** Sum of all active risks must never exceed 6% of total equity.
- **Correlation Cap:** Do not open simultaneous long positions on heavily correlated pairs exceeding 4% total combined risk.

### 4. Daily Hard Loss Cutoff (Kill Switch)
If the account suffers a net equity drawdown of 3% within a rolling 24-hour window, automatically:
1. Cancel all open limit orders.
2. Flatten market exposure or hedge open positions.
3. Lock trading activity until the next trading session.

---

## Production Risk Sizing Script

```python
class RiskManager:
    def __init__(self, account_equity: float, max_risk_pct: float = 0.015, daily_loss_limit_pct: float = 0.03):
        self.equity = account_equity
        self.max_risk_pct = max_risk_pct
        self.daily_loss_limit = daily_loss_limit_pct
        self.daily_pnl = 0.0

    def calculate_position_size(self, entry: float, stop_loss: float) -> dict:
        if self.daily_pnl <= -(self.equity * self.daily_loss_limit):
            raise PermissionError("Emergency Kill Switch Active: Daily loss threshold hit!")
            
        risk_amount = self.equity * self.max_risk_pct
        risk_per_unit = abs(entry - stop_loss)
        if risk_per_unit == 0:
            raise ValueError("Stop loss cannot equal entry price.")
            
        units = risk_amount / risk_per_unit
        notional_value = units * entry
        
        return {
            'risk_capital': round(risk_amount, 2),
            'units': round(units, 4),
            'notional_value': round(notional_value, 2),
            'risk_per_unit': round(risk_per_unit, 4)
        }
```
