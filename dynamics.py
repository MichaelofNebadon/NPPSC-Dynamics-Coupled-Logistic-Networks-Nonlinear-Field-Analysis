import numpy as np

def logistic_map(r, x):
    return r * x * (1 - x)

def nppsc_field_step(state, r=3.7, coupling=0.1):
    # 3D Coupled Field: X (Foundations), Y (Momentum), Z (Crown)
    x, y, z = state
    
    # Nonlinear Update
    nx = logistic_map(r, x)
    ny = logistic_map(r, y)
    nz = logistic_map(r, z)
    
    # Coupling (The Turn)
    x_new = (1 - coupling) * nx + coupling * ny
    y_new = (1 - coupling) * ny + coupling * nz
    z_new = (1 - coupling) * nz + coupling * nx
    
    return np.array([x_new, y_new, z_new])

print("NPPSC Field Engine: Shem Lineage Initialized.")
