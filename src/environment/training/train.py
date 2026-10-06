import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.environment.market_env import MarketMakingEnv


def run_random_agent():
    """
    Run a simple random agent to verify
    that the market-making environment works.
    """

    env = MarketMakingEnv()

    observation, info = env.reset()

    total_reward = 0.0

    for step in range(100):
        # Select a random action
        action = env.action_space.sample()

        observation, reward, terminated, truncated, info = env.step(action)

        total_reward += reward

        if terminated or truncated:
            break

    print("Simulation completed!")
    print(f"Steps: {step + 1}")
    print(f"Final P&L: {info['pnl']:.2f}")
    print(f"Final Inventory: {info['inventory']}")
    print(f"Total Reward: {total_reward:.2f}")


if __name__ == "__main__":
    run_random_agent()
