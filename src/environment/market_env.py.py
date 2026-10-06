import gymnasium as gym
import numpy as np
from gymnasium import spaces


class MarketMakingEnv(gym.Env):
    """
    Simple simulated market-making environment.

    The agent chooses:
        0 -> Tight spread
        1 -> Normal spread
        2 -> Wide spread

    The environment tracks:
        - cash
        - inventory
        - mid price
        - profit and loss
    """

    metadata = {"render_modes": ["human"]}

    def __init__(self, initial_price=100.0, max_steps=1000):
        super().__init__()

        self.initial_price = initial_price
        self.max_steps = max_steps

        # Actions:
        # 0 = tight spread
        # 1 = normal spread
        # 2 = wide spread
        self.action_space = spaces.Discrete(3)

        # Observation:
        # [mid_price, inventory, cash]
        self.observation_space = spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(3,),
            dtype=np.float32,
        )

        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.step_count = 0
        self.mid_price = self.initial_price
        self.inventory = 0
        self.cash = 0.0

        self.previous_pnl = 0.0

        return self._get_observation(), {}

    def step(self, action):
        self.step_count += 1

        # Simulate price movement
        price_change = self.np_random.normal(0, 0.5)
        self.mid_price += price_change

        # Determine quoted spread
        spreads = {
            0: 0.10,
            1: 0.25,
            2: 0.50,
        }

        spread = spreads[int(action)]

        bid_price = self.mid_price - spread / 2
        ask_price = self.mid_price + spread / 2

        # Simulate market interaction
        buy_probability = 0.30
        sell_probability = 0.30

        if self.np_random.random() < buy_probability:
            self.inventory -= 1
            self.cash += ask_price

        if self.np_random.random() < sell_probability:
            self.inventory += 1
            self.cash -= bid_price

        # Calculate current portfolio value
        portfolio_value = self.cash + self.inventory * self.mid_price

        pnl = portfolio_value

        reward = pnl - self.previous_pnl
        self.previous_pnl = pnl

        terminated = False
        truncated = self.step_count >= self.max_steps

        observation = self._get_observation()

        info = {
            "mid_price": self.mid_price,
            "inventory": self.inventory,
            "cash": self.cash,
            "pnl": pnl,
        }

        return observation, reward, terminated, truncated, info

    def _get_observation(self):
        return np.array(
            [
                self.mid_price,
                self.inventory,
                self.cash,
            ],
            dtype=np.float32,
        )

    def render(self):
        print(
            f"Step: {self.step_count} | "
            f"Price: {self.mid_price:.2f} | "
            f"Inventory: {self.inventory} | "
            f"Cash: {self.cash:.2f}"
        )
