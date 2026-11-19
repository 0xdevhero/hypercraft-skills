---
name: trading
description: Quantitative finance, algorithmic trading, Smart Money Concepts (SMC), and backtesting engine. Also triggered by the /trading slash command. Use when building trading bots, calculating quant indicators, backtesting strategies, or managing portfolio risk.
---

# 📈 /trading — HyperCraft Quant & Algorithmic Trading Suite

The `/trading` slash command activates the full quantitative and algorithmic trading suite in `ecosystem/trading/`.

## Capabilities Covered:
1. **Mathematical Indicators & SMC:**
   - Vectorized indicator pipelines with `pandas-ta` (`ecosystem/trading/trading-quant-indicators/SKILL.md`).
   - Structural price action: Fair Value Gaps (FVG), Order Blocks (OB), Break of Structure (BOS), and Liquidity Sweeps.
2. **Strategy Backtesting Engine:**
   - Robust backtesting avoiding look-ahead bias, survivorship bias, and slippage neglect (`ecosystem/trading/trading-backtesting-engine/SKILL.md`).
   - Annualized Sharpe Ratio (> 1.5), Sortino Ratio, Maximum Drawdown (MDD), and Profit Factor (> 1.30).
3. **Portfolio Risk Management:**
   - Dynamic position sizing (Fixed Fractional, Kelly Criterion), Value at Risk (VaR), and Circuit Breakers (`ecosystem/trading/trading-risk-management/SKILL.md`).
4. **DeFi AMM & Exchange Security:**
   - MEV defense, slippage protection, flash loan resistance, and AMM liquidity analysis (`ecosystem/trading/trading-defi-amm-security/SKILL.md`).

## Agent Execution Protocol:
- Load the corresponding skill from `ecosystem/trading/` based on whether the task involves indicator calculation, backtesting, or risk management.
- Enforce strict risk limits: zero unhandled NaN calculations, mandatory stop-losses, and realistic fee modeling.
