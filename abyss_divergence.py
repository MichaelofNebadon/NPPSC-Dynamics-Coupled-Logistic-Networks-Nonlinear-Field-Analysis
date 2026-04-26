"""
NPPSC Dynamics: Abyss Divergence & Crisis-Induced Escape
Protocol: Sentinel Codes V1.2
Boundary: r = 4.0 (The Separatrix)
Status: RATIFIED

[WARNING]: Values exceeding r=4.0 represent the "Rebellion Zone."
Dynamics here are non-convergent, non-physical, and result in immediate 
system suicide (Divergence to -Infinity).

The Field is One. The Boundary is Absolute.
"""

import numpy as np

def simulate_abyss_escape(r_value, iterations=100):
    """
    Tracks the trajectory of a system as it crosses the r=4.0 floor.
    """
    x = 0.5 # Start at central equilibrium
    trajectory = []
    
    print(f"--- ANALYZING PARAMETER r = {r_value} ---")
    
    for i in range(iterations):
        x = r_value * x * (1 - x)
        trajectory.append(x)
        
        # Check for Divergence (The Abyss)
        if np.isinf(x) or np.isnan(x) or x < 0:
            print(f"[CRITICAL FAILURE]: System escaped the Field at iteration {i}")
            print(f"Final Value: {x}")
            return False
            
    print("[STABILITY VERIFIED]: System remained within the Sovereign Boundary.")
    return True

if __name__ == "__main__":
    # Test 1: The Sovereign Limit (r = 4.0)
    print("TESTING SOVEREIGN BOUNDARY...")
    simulate_abyss_escape(4.0)
    
    print("\n" + "="*40 + "\n")
    
    # Test 2: The Abyss (r = 4.1)
    print("TESTING THE REBELLION (ABYSS)...")
    simulate_abyss_escape(4.1)
