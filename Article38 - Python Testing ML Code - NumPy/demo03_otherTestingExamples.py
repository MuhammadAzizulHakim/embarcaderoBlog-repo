# Example 01:
import numpy as np
 
x = np.array([1., 1e-10, 1e-20])
eps = np.finfo(x.dtype).eps
np.testing.assert_array_almost_equal_nulp(x, x*eps/2 + x)

# Example 02:
import numpy as np
 
x = np.array([1., 1e-10, 1e-20])
eps = np.finfo(x.dtype).eps
np.testing.assert_array_almost_equal_nulp(x, x*eps + x)

# Example 03:
import numpy as np
 
np.testing.run_module_suite(file_to_run="numpy/tests/test_numpy_version.py")
