import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import streamlit as st

st.title('Normal distribution')

mu_in = st.slider('Mean', value=5, min_value=-10, max_value=10)
std_in = st.slider('Standard deviation', value=5.0, min_value=0.0, max_value=10.0)
size = st.slider('Number of samples', value=100, max_value=500)

def norm_dist(mu, std, size=100):
	"""Generate normal distribution."""
	return norm.rvs(mu, std, size=size)

data = norm_dist(mu_in, std_in, size=size)

# Fit the normal distribution
mu, std = norm.fit(data)

# Make some plots
...

st.pyplot(fig)