import numpy as np

class CardioNeuralODESolver:
    """
    Coupled Differential Equation Solver for Cardio-Neural Axis Simulation.
    Simulates interaction between vascular perfusion (P) and neural action potentials (N).
    """
    def __init__(self, alpha: float = 0.05, beta: float = 0.02, gamma: float = 0.1, delta: float = 0.01):
        self.alpha = alpha  # Vascular-neural coupling
        self.beta = beta    # Vascular dampening
        self.gamma = gamma  # Cardiac output feedback
        self.delta = delta  # Synaptic decay rate

    def system_derivatives(self, state: np.ndarray, t: float) -> np.ndarray:
        P, N = state
        dP_dt = -self.beta * P + self.alpha * N
        dN_dt = self.gamma * P - self.delta * (N**2)
        return np.array([dP_dt, dN_dt])

    def rk4_integration_step(self, state: np.ndarray, t: float, dt: float) -> np.ndarray:
        """4th Order Runge-Kutta integration for zero-latency execution."""
        k1 = self.system_derivatives(state, t)
        k2 = self.system_derivatives(state + 0.5 * dt * k1, t + 0.5 * dt)
        k3 = self.system_derivatives(state + 0.5 * dt * k2, t + 0.5 * dt)
        k4 = self.system_derivatives(state + dt * k3, t + dt)
        return state + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

    def execute_brain_heart_eye_pipeline(self, initial_state: list = [120.0, 75.0], steps: int = 100, dt: float = 0.01) -> np.ndarray:
        state = np.array(initial_state, dtype=float)
        trajectory = [state.copy()]
        t = 0.0
        for _ in range(steps):
            state = self.rk4_integration_step(state, t, dt)
            t += dt
            trajectory.append(state.copy())
        return np.array(trajectory)
