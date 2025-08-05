# src/change_point_model.py

import pymc3 as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import arviz as az

def run_change_point_analysis(df: pd.DataFrame, column='daily_return'):
    """
    Run Bayesian change point detection on a specified column using PyMC3.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing the time series data.
        column (str): Column to analyze for change points.

    Returns:
        trace (MultiTrace): PyMC3 trace object.
        model (pm.Model): The PyMC3 model.
    """
    data = df[column].dropna().values
    n = len(data)

    with pm.Model() as model:
        # Switch point prior
        tau = pm.DiscreteUniform('tau', lower=0, upper=n - 1)

        # Priors for mean before and after the change point
        mu1 = pm.Normal('mu1', mu=np.mean(data), sd=np.std(data))
        mu2 = pm.Normal('mu2', mu=np.mean(data), sd=np.std(data))

        # Common standard deviation
        sigma = pm.HalfNormal('sigma', sd=1)

        # Switching mean
        mu = pm.math.switch(tau >= np.arange(n), mu1, mu2)

        # Likelihood
        obs = pm.Normal('obs', mu=mu, sd=sigma, observed=data)

        # Sampling
        trace = pm.sample(2000, tune=2000, target_accept=0.95, return_inferencedata=True)

    return trace, model


def plot_trace(trace):
    """
    Plot trace diagnostics to check convergence.
    
    Parameters:
        trace (MultiTrace): PyMC3 trace object.
    """
    az.plot_trace(trace)
    plt.tight_layout()
    plt.show()


def summarize_results(trace):
    """
    Print summary statistics of the trace.
    
    Parameters:
        trace (MultiTrace): PyMC3 trace object.
    """
    summary = az.summary(trace, round_to=4)
    print(summary)
    return summary
