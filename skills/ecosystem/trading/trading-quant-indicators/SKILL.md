---
name: trading-quant-indicators
description: Algorithmic technical indicators, mathematical oscillators, and Smart Money Concepts (SMC) including FVG, Order Blocks, and Liquidity Sweeps with pandas-ta. Use when designing trading signals, calculating indicators, or detecting market structure.
metadata:
  version: "1.0.0"
  author: HyperCraft Core Team
  license: Apache-2.0
---

# Trading Quant Indicators & Smart Money Concepts (SMC)

Algorithmic technical analysis combines statistical oscillators with structural price action. This skill provides vectorized indicator formulas, Smart Money Concepts (SMC) detection patterns, and robust calculation pipelines.

## Core Mathematical Indicators

### 1. Trend & Moving Averages
- **Exponential Moving Average (EMA):** Weight recent prices exponentially:
  `EMA_t = alpha * P_t + (1 - alpha) * EMA_{t-1}`, where `alpha = 2 / (N + 1)`
- Golden Cross (EMA 50 crossing above EMA 200) and Death Cross (EMA 50 crossing below EMA 200).
- Volume Weighted Average Price (VWAP) as institutional benchmark.

### 2. Momentum & Oscillators
- **Relative Strength Index (RSI - 14):**
  `RS = Avg Gain / Avg Loss`, `RSI = 100 - (100 / (1 + RS))`
  - Overbought (> 70), Oversold (< 30), Bearish/Bullish Divergences.
- **Moving Average Convergence Divergence (MACD):**
  - MACD Line = EMA(12) - EMA(26)
  - Signal Line = EMA(9) of MACD Line
  - Histogram = MACD Line - Signal Line

### 3. Volatility & Bands
- **Average True Range (ATR - 14):** Non-directional volatility measurement for dynamic stop-loss placement:
  `TR = max(High - Low, abs(High - Close_prev), abs(Low - Close_prev))`
- **Bollinger Bands (20, 2):** SMA(20) +/- 2 * std. Band squeeze indicates impending breakout.

---

## Smart Money Concepts (SMC) Detection

### 1. Fair Value Gap (FVG)
An FVG occurs when price expands rapidly leaving an imbalance where Candle 1 and Candle 3 do not overlap:
- **Bullish FVG:** Low of Candle 3 > High of Candle 1. Unfilled gap is `[High(Candle 1), Low(Candle 3)]`.
- **Bearish FVG:** High of Candle 3 < Low of Candle 1. Unfilled gap is `[High(Candle 3), Low(Candle 1)]`.

### 2. Order Blocks (OB)
- **Bullish Order Block:** The last down-close candle before an aggressive upward displacement that breaks prior swing high (BOS).
- **Bearish Order Block:** The last up-close candle before an aggressive downward displacement that breaks prior swing low.

### 3. Liquidity Sweeps
- Price pierces key swing high/low (taking out retail stop losses) but closes back inside the range within the same or subsequent bar.

---

## Production Python Implementation

```python
import pandas as pd
import numpy as np

def calculate_quant_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    # 1. EMAs
    df['ema_20'] = df['close'].ewm(span=20, adjust=False).mean()
    df['ema_50'] = df['close'].ewm(span=50, adjust=False).mean()
    df['ema_200'] = df['close'].ewm(span=200, adjust=False).mean()
    
    # 2. RSI (14)
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / (loss + 1e-10)
    df['rsi'] = 100 - (100 / (1 + rs))
    
    # 3. ATR (14)
    tr1 = df['high'] - df['low']
    tr2 = (df['high'] - df['close'].shift()).abs()
    tr3 = (df['low'] - df['close'].shift()).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    df['atr'] = tr.rolling(window=14).mean()
    
    # 4. Bollinger Bands (20, 2)
    sma_20 = df['close'].rolling(window=20).mean()
    std_20 = df['close'].rolling(window=20).std()
    df['bb_upper'] = sma_20 + (std_20 * 2)
    df['bb_lower'] = sma_20 - (std_20 * 2)
    
    return df

def detect_fair_value_gaps(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['bullish_fvg'] = False
    df['bearish_fvg'] = False
    df['fvg_top'] = np.nan
    df['fvg_bottom'] = np.nan
    
    bull_mask = df['low'] > df['high'].shift(2)
    df.loc[bull_mask, 'bullish_fvg'] = True
    df.loc[bull_mask, 'fvg_top'] = df['low']
    df.loc[bull_mask, 'fvg_bottom'] = df['high'].shift(2)
    
    bear_mask = df['high'] < df['low'].shift(2)
    df.loc[bear_mask, 'bearish_fvg'] = True
    df.loc[bear_mask, 'fvg_top'] = df['low'].shift(2)
    df.loc[bear_mask, 'fvg_bottom'] = df['high']
    
    return df
```
