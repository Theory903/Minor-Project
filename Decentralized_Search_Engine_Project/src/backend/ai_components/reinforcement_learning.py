import numpy as np
import random

class ReinforcementLearning:
    def __init__(self, num_states, num_actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.num_states = num_states
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_table = np.zeros((num_states, num_actions))

    def choose_action(self, state):
        if random.uniform(0, 1) < self.exploration_rate:
            # Explore: choose a random action
            return random.randint(0, self.num_actions - 1)
        else:
            # Exploit: choose the action with the highest Q-value
            return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.discount_factor * self.q_table[next_state][best_next_action]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.learning_rate * td_error

# Example usage:
if __name__ == "__main__":
    # Create an environment with 5 states and 3 actions
    num_states = 5
    num_actions = 3
    
    # Initialize reinforcement learning agent
    rl_agent = ReinforcementLearning(num_states, num_actions)

    # Example training loop
    num_episodes = 1000
    for episode in range(num_episodes):
        # Reset environment to initial state
        state = 0
        done = False

        while not done:
            # Choose action
            action = rl_agent.choose_action(state)

            # Take action and observe next state and reward
            next_state = (state + action) % num_states
            reward = 1 if next_state == num_states - 1 else 0

            # Update Q-table
            rl_agent.update_q_table(state, action, reward, next_state)

            # Update state
            state = next_state

            # Check if episode is done
            if next_state == num_states - 1:
                done = True

    # Print the learned Q-table
    print("Learned Q-table:")
    print(rl_agent.q_table)
