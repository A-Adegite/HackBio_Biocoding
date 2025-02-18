import numpy as np
import pandas as pd

codon_chart = {
    "F" : ("TTT","TTC"),
    "L" : ("TTA","TTG","CTT","CTC","CTA","CTG"),
    "S" : ("TCT","TCC","TCA","TCG","AGT","AGC"),
    "Y" : ("TAT","TAC"),
    "C" : ("TGT","TGC"),
    "W" : ("TGG",),
    "P" : ("CCT","CCC","CCA","CCG"),
    "H" : ("CAT","CAC"),
    "Q" : ("CAA","CAG"),
    "R" : ("CGT","CGC","CGA","CGG","AGA","AGG"),
    "M" : ("ATG"),
    "I" : ("ATT","ATC","ATA"),
    "T" : ("ACT","ACC","ACA","ACG"),
    "N" : ("AAT","AAC"),
    "K" : ("AAA","AAG"),
    "V" : ("GTT","GTC","GTA","GTG"),
    "A" : ("GCT","GCC","GCA","GCG"),
    "D" : ("GAT","GAC"),
    "E" : ("GAA","GAG"),
    "G" : ("GGT","GGC","GGA","GGG")
}

# DNA Sequence Translator
def Sequence_Translator(seq):
  seq = seq.upper().strip()
  polypeptide = list()
  for i in range(0,len(seq),3):
    codon = seq[i:i+3]
    if codon in ("TAG","TGA","TAA"):
      polypeptide.append("*")
      break
    for aa,cdn in codon_chart.items():
      if codon in cdn:
        polypeptide.append(aa)
  return "".join(polypeptide)

seq = input("Enter a Nucleotide Sequence: ")
Sequence_Translator(seq)

# logistic population growth curve function
def generate_growth_curve(time_points, lag_duration, exp_phase_length, P0=1, K=100):
    """
    Simulates a logistic growth curve with adjustable lag and exponential phases.
    
    Parameters:
        time_points: Time points for simulation
        lag_duration: Duration of lag phase
        exp_phase_length: Duration of exponential phase
        P0: Initial population (default=1)
        K: Carrying capacity (default=100)
    """
    C = (K - P0) / P0
    r = -np.log(0.25 / C) / exp_phase_length  # Calculate growth rate
    adjusted_t = np.maximum(time_points - lag_duration, 0)
    population = K / (1 + C * np.exp(-r * adjusted_t))
    return population

time_points = np.arange(0, 50, 0.1) # Generate time points (0 to 50 hours, 0.1 increments)
df = pd.DataFrame({'Time': time_points})
# Generate 100 curves with randomized parameters
np.random.seed(42)  # For reproducibility
for i in range(100):
    lag = np.random.uniform(0, 10)   # Random lag between 0-10
    exp = np.random.uniform(5, 20)   # Random exponential phase 5-20
    df[f'Curve_{i+1}'] = generate_growth_curve(time_points, lag, exp)

# Function for determining time to reach 80% of max growth
def time_to_80(population_curve, time_points):
    """
    Finds the first time a curve reaches 80% of carrying capacity.
    """
    above_80 = np.where(population_curve >= 80)[0]
    return time_points[above_80[0]] if len(above_80) > 0 else None

# Calculate times for all curves
results = []
for col in df.columns[1:]:  
    curve = df[col].values
    results.append(time_to_80(curve, df['Time'].values))

result_df = pd.DataFrame({
    'Curve': df.columns[1:],
    'Time_to_80': results
})
print(result_df).head()

# Hamming Distance Calculator
def Hamming_Distance(slack_handle,x_handle):
  ham_dist = list()
  for i in range(len(slack_handle)):
    if slack_handle[i] == x_handle[i]:
      ham_dist.append(0)
    elif slack_handle[i] != x_handle[i]:
      ham_dist.append(1)
  return sum(ham_dist)

Hamming_Distance("a_adegite","a_adegite")
