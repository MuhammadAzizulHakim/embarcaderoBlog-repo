# Import profiling tools
import cProfile as profile
import pstats
# Manually search perceptron hyperparameters for binary classification
from numpy import mean
from numpy.random import randn
from numpy.random import rand
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.linear_model import Perceptron

# Objective function
def objective(X, y, cfg):
    # Unpack config
    eta, alpha = cfg
    # Define model
    model = Perceptron(penalty='elasticnet', alpha=alpha, eta0=eta)
    # Define evaluation procedure
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    # Evaluate model
    scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1)
    # Calculate mean accuracy
    result = mean(scores)
    return result

# Take a step in the search space
def step(cfg, step_size):
    # Unpack the configuration
    eta, alpha = cfg
    # Step eta
    new_eta = eta + randn() * step_size
    # Check the bounds of eta
    if new_eta <= 0.0:
        new_eta = 1e-8
    if new_eta > 1.0:
        new_eta = 1.0
    # Step alpha
    new_alpha = alpha + randn() * step_size
    # Check the bounds of alpha
    if new_alpha < 0.0:
        new_alpha = 0.0
    # Return the new configuration
    return [new_eta, new_alpha]

# Hill climbing local search algorithm
def hillclimbing(X, y, objective, n_iter, step_size):
    # Starting point for the search
    solution = [rand(), rand()]
    # Evaluate the initial point
    solution_eval = objective(X, y, solution)
    # Run the hill climb
    for i in range(n_iter):
        # Take a step
        candidate = step(solution, step_size)
        # Evaluate candidate point
        candidate_eval = objective(X, y, candidate)
        # Check if we should keep the new point
        if candidate_eval >= solution_eval:
            # Store the new point
            solution, solution_eval = candidate, candidate_eval
            # Report progress
            print('>%d, cfg=%s %.5f' % (i, solution, solution_eval))
    return [solution, solution_eval]

# Define dataset
X, y = make_classification(n_samples=1000, n_features=5, n_informative=2, n_redundant=1, random_state=1)
# Define the total iterations
n_iter = 100
# Step size in the search space
step_size = 0.1
# Perform the hill climbing search with profiling
prof = profile.Profile()
prof.enable()
cfg, score = hillclimbing(X, y, objective, n_iter, step_size)
prof.disable()
# Print program output
print('Done!')
print('cfg=%s: Mean Accuracy: %f' % (cfg, score))
# Print profiling output
stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
stats.print_stats(10) # Print only top 10 rows