[![DOI](https://zenodo.org/badge/286865245.svg)](https://zenodo.org/badge/latestdoi/286865245)

# EnzyPred: Enzyme-Substrate Interaction Prediction

![Graphical Abstract](https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/graphical_abstract.png)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tu_usuario/tu_repo/blob/main/notebooks/EnzyPrediction.ipynb)  
_Click the badge to run this project directly in Google Colab._

---

## Overview

Enzyme-substrate interaction (ESI) prediction is a critical challenge in **biocatalysis**, with applications in metabolic engineering and drug design. This prediction helps avoid costly and time-consuming experimental characterization.  

We present **EnzyPred**, an ESI prediction tool based on **Natural Language Processing (NLP)**, **Deep Learning (DL)**, **fine-tuning**, **Low-Rank Parallel Adapter (LoRA-P)**, and **prioritized retraining (PR)** techniques.  

The model integrates **Evolutionary Scale Modeling (ESM)** representations for enzymes and **Extended Connectivity Fingerprints (ECFP)** for substrates. Training used **32,833 positive enzyme-substrate pairs**, complemented by negative samples generated via clustering, molecular descriptors, and Tanimoto similarity.  

**Performance:** EnzyPred-MLP achieved an **average accuracy of 86.5%**, proving competitive with existing tools, and excelling in generalization, computational efficiency, and adaptability.  

**Experimental Validation:**  
- *Case 1*: Identification of the enzyme catalyzing the conversion of 4'-O-methylnorbelladine to N-desmethylnarwedine in *Amaryllidaceae*. Predictions were validated experimentally, advancing the elucidation of the **galantamine biosynthesis pathway** (Alzheimer’s drug).  
- *Case 2*: Virtual screening against **acetylcholinesterase (AChE)** from the ZINC22 database. Of 747 predicted active compounds, 9 were prioritized and experimentally validated — all showing activity.  

These results confirm EnzyPred’s ability to accelerate molecular interaction discovery and pathway design.

---

## Model Overview

### Enzyme and Substrate Coding
* **Substrates** → Encoded with **ECFP** fingerprints to capture chemical and structural information.  
* **Enzymes** → Encoded using **ESMC** (Protein Language Models), generating dense numerical embeddings of amino acid residues.

---

### Model Architecture  

The backbone combines:  
- **LSTM layers** → Extract sequential dependencies and contextual interactions of enzyme amino acid sequences from ESM embeddings.  
- **Dense layers** → Process substrate ECFP fingerprints into compact structural vectors.  
- **Fusion layer** → Concatenates enzyme and substrate representations.  
- **Sigmoid output layer** → Performs binary classification (interaction vs. non-interaction).  

Additional modules improve specificity and adaptability:  
1. **Fine-Tuning** – Retrains on reduced, similarity-based subsets of data.  
2. **LoRA-P (Low-Rank Adaptation Parallel)** – Efficient, parallel adaptation without losing generalization power.  

![Model Architecture](https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/model_architecture.png)

---

### Prioritized Retraining (PR)

EnzyPred introduces **prioritized retraining** to enhance predictions by dynamically focusing on biologically relevant data.  

Steps:  
1. Compute similarity scores using **Tanimoto (ECFP)** for substrates or **embedding similarity (ESM)** for enzymes.  
2. Rank and select the most relevant enzyme, substrate, or enzyme-substrate pairs.  
3. Retrain the model with LoRA-P or fine-tuning on these prioritized subsets.  

This approach increased classification accuracy on dissimilar pairs (79.2 → 81.5%).  

![Prioritized Retraining](https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/prioritized_retraining.png)

---

## Reproducing Results


### Prerequisites
To run the analysis, ensure you have the following:
- **Python**: Version 3.11
- **Conda**: For environment management
- **Hardware**: Multi-core CPU recommended (e.g., 40 cores for reasonable runtime)
- **Dependencies**: Listed in `requirements.txt`

### Environment Setup
Follow these steps to set up the environment:

1. Create a Conda environment:
   ```bash
   conda create -n enzypred python=3.11
   ```
2. Activate the environment:
   ```bash
   conda activate enzypred
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Results
To reproduce the enzyme identification and virtual screening results:
1. Navigate to the `notebooks/` directory.
2. Open the Jupyter notebook `EnzyPredAnalysis.ipynb`, which provides step-by-step instructions for generating the results.
3. Run the notebook in a Jupyter session:
   ```bash
   jupyter notebook
   ```
4. **Note**: Some steps are computationally intensive and may take several hours. For faster execution, use multiple CPU cores (tested with 40 cores).

### Additional Notes
- Ensure sufficient disk space for intermediate data processing (check `notebooks/EnzyPredAnalysis.ipynb` for details).

### Additional Dependencies
To install the R package `kebabs` for sequence analysis:
```bash
Rscript -e "if (!requireNamespace('BiocManager', quietly = TRUE)) install.packages('BiocManager')"
Rscript -e "BiocManager::install('kebabs')"
```

---
## Applying EnzyPred to Enzyme-Substrate Pairs
To predict interactions for any enzyme-substrate pair using the LoRAP8 model:
1. Navigate to the `notebooks/` directory.
2. Open the Jupyter notebook `EnzyPrediction.ipynb`, which contains a step-by-step guide for running predictions.
3. Start a Jupyter session:
   ```bash
   jupyter notebook
   ```
4. Follow the instructions in `EnzyPrediction.ipynb` to input your enzyme-substrate pair and generate predictions.