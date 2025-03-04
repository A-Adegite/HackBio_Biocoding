# HackBio_Biocoding
This repository contains my coding tasks and projects for the HackBio internship, themed AI × BIO. Over four weeks, I will explore the intersection of AI and biological data analysis. Each week's assignments, scripts, and insights will be documented here, showcasing my bioinformatics and data science progress.
# Stage Zero Task
## Task Description 
This task involved organizing my team members' information and printing it out using Python data structures without using functions, loops or conditional statements.
## Task Approach and Explanation 
A variable name called team_info was created to hold a list of five dictionaries. Each dictionary contains information about a team members including their name, Slack username, email, hobby, country, discipline, and preferred programming language.

To access and print the details of each member individually, the syntax team_info[0] was used to retrieve the first member's information stored as a dictionary. To extract specific details, team_info[0]["Name"] was used to obtain the name. This process was repeated for each member by referencing their respective positions in the list.

using the print() statement, each team member's details were printed in a structured format. Each member's print() statements were repeated, showing their name, Slack username, email, hobby, country, discipline, and preferred programming language. To enhance readability, the print() statement with no arguments was used to create a blank line between team member's details.
# Stage One Task
## Task Description 
This stage involves implementing various bioinformatics functions related to DNA translation, population growth simulation, and string comparison.
## Task Details
* DNA to Protein Translation: A function that converts a given DNA sequence into its corresponding protein sequence using the standard genetic code.
*  Logistic Population Growth Simulation: A function that simulates a logistic growth curve with randomized lag and exponential phases, generating 100 different growth curves.
*   Time to 80% Carrying Capacity: A function determining the time required for a population to reach 80% of its maximum growth (carrying capacity).
Hamming Distance Calculation: A function that computes the Hamming distance between a Slack username and a Twitter/X handle, padding if necessary to match string lengths.
# Stage Two Task
This stage expands on bioinformatics tasks, incorporating microbiology, biochemistry, oncology, transcriptomics, and public health analyses.
## Task Details
# Task Code 2.1: Microbiology

- Look at the dataset provided.
- Plot all the growth curves of OD600 vs Time for different strains.
- For each strain, overlay the growth curves of the knock-out (-) and knock-in (+) strains.
- Using the function from Stage 1, determine the time to reach carrying capacity for each strain/mutant.
- Generate a scatter plot of the time taken to reach carrying capacity for the knock-out and knock-in strains.
- Generate a box plot of the time taken to reach carrying capacity for the knock-out and knock-in strains.
- Determine if there is a statistical difference in time to carrying capacity between knock-out and knock-in strains.
- Explain observations as comments in the code.

---

# Task Code 2.4: Biochemistry & Oncology

- Import both **SIFT** and **FoldX** datasets.
- Create a new column `specific_Protein_aa` by concatenating `Protein` and `Amino_acid` columns (e.g., `A5A607_E63D`).
- Merge **SIFT** and **FoldX** datasets using `specific_Protein_aa`.
- Identify mutations with:
  - **SIFT Score < 0.05** (functional impact)
  - **FoldX Score > 2 kcal/mol** (structural impact)
- Analyze amino acid substitution nomenclature.
- Identify the amino acid with the highest functional and structural impact.
- Generate a **frequency table** of amino acids.
- Visualize amino acid frequencies using a **bar plot** and **pie chart**.
- Briefly describe the amino acid with the highest impact.
- Discuss the structural and functional properties of amino acids with more than **100 occurrences**.

---

# Task Code 2.6: Transcriptomics

- Load and explore the RNA-seq dataset.
- Generate a **volcano plot**.
- Identify:
  - **Upregulated genes** (Log2FC > 1, p-value < 0.01)
  - **Downregulated genes** (Log2FC < -1, p-value < 0.01)
- Research the functions of the **top 5 upregulated** and **top 5 downregulated** genes using **GeneCards**.

---

# Task Code 2.7: Public Health

- Process all **NA values** (either by deletion or converting to zero).
- Visualize distributions of:
  - **BMI**
  - **Weight**
  - **Weight in pounds** (*weight × 2.2*)
  - **Age**  
  *(Use histograms)*
- Compute the **mean 60-second pulse rate**.
- Determine the **range of diastolic blood pressure values**.
- Compute **variance and standard deviation** for **income**.
- Visualize the **relationship between weight and height**.
  - **Color points by**: gender, diabetes status, and smoking status.
- Conduct **t-tests** between the following variables:
  - **Age and Gender**
  - **BMI and Diabetes**
  - **Alcohol Year and Relationship Status**
- Interpret the relationships based on **p-values**.

