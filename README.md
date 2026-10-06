# 🤖 Multi-Agent Reinforcement Learning for Algorithmic Market Making

A research-oriented reinforcement learning project that explores how multiple autonomous agents can learn market-making strategies in a simulated financial market.

## 🎯 Objective

The goal is to investigate whether multi-agent reinforcement learning can be used to learn effective market-making strategies while managing:

- Inventory risk
- Bid-ask spread
- Market volatility
- Order flow
- Profit and loss
- Competition between market-making agents

## 🏗️ Project Architecture

```text
Market Environment
       │
       ▼
Order Book Simulation
       │
       ▼
┌──────────────────────────┐
│    Multiple RL Agents    │
│                          │
│  Market Maker Agent 1    │
│  Market Maker Agent 2    │
│  Market Maker Agent 3    │
└────────────┬─────────────┘
             │
             ▼
      Trading Decisions
             │
             ▼
     Reward Calculation
             │
             ▼
       Performance
        Evaluation
```

## 🧠 Key Components

- Market environment simulation
- Limit order book
- Multiple market-making agents
- Reinforcement learning algorithms
- Inventory management
- Reward engineering
- Training and evaluation pipeline
- Trading performance analysis

## 📊 Evaluation Metrics

The agents will be evaluated using:

- Profit & Loss (P&L)
- Sharpe Ratio
- Maximum Drawdown
- Inventory Risk
- Spread Capture
- Trading Volume
- Agent Performance

## 🛠️ Technologies

- Python
- NumPy
- Pandas
- PyTorch
- Gymnasium
- Matplotlib
- Jupyter Notebook

## 📁 Project Structure

```text
multi-agent-market-making-rl/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
├── src/
│   ├── environment/
│   ├── agents/
│   ├── models/
│   └── utils/
│
├── training/
├── evaluation/
├── notebooks/
└── results/
```

## 🚧 Project Status

Currently under development.

Future work will include implementing the simulated market environment, training multiple reinforcement learning agents, and comparing their performance under different market conditions.

## 📚 Research Direction

This project is intended as an experimental framework for studying the application of multi-agent reinforcement learning to algorithmic market making.

---

**Author:** Aniket
