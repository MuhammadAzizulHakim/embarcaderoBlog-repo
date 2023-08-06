# Example 01:
import numpy as np
 
x = [1e-5, 1e-3, 1e-1]
y = np.arccos(np.cos(x))
np.testing.assert_allclose(x, y, rtol=1e-5, atol=0)

# Example 02:
import numpy as np
 
x = [1e-7, 1e-3, 1e-1]
y = np.arccos(np.cos(x))
np.testing.assert_allclose(x, y, rtol=1e-5, atol=0)