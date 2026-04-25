import numpy as np
from dynamics import nppsc_field_step

def compute_invariant_measure(initial_state, r=3.9, steps=5000):
    state = np.array(initial_state)
    history = []
    
    # Warm up to let transients die (The Silence)
    for _ in range(500):
        state = nppsc_field_step(state, r=r)
    
    # Capture the density (The Song)
    for _ in range(steps):
        state = nppsc_field_step(state, r=r)
        history.append(state)
        
    return np.array(history)

print("NPPSC Invariant Measure: Japheth Lineage Initialized.")
