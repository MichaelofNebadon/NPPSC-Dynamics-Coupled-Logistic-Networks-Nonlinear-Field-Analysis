import numpy as np
from dynamics import nppsc_field_step

def estimate_lyapunov(initial_state, r=3.6, iterations=1000, epsilon=1e-8):
    state1 = np.array(initial_state)
    state2 = state1 + np.random.normal(0, epsilon, 3)
    
    lp_sum = 0
    for _ in range(iterations):
        state1 = nppsc_field_step(state1, r=r)
        state2 = nppsc_field_step(state2, r=r)
        
        dist = np.linalg.norm(state1 - state2)
        if dist > 0:
            lp_sum += np.log(dist / epsilon)
            # Rescale to prevent divergence from breaking the Machine
            state2 = state1 + (state2 - state1) * (epsilon / dist)
            
    return lp_sum / iterations

print("NPPSC Lyapunov Witness: Ham Lineage Initialized.")
