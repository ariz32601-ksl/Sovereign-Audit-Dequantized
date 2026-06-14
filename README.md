# 🦅 Sovereign Audit: Dequantizing Complexity

### High-Fidelity Exact Enumeration of Assembly Theory vs. LZW Compression

**Principal Investigator:** Chun Tang (KSL)  
**Synthetic Co-PIs:** Aletheia (Google Gemini Advanced), DeepSeek-Tang (DeepSeek-V3)  
**Lab:** Kunpeng Sovereign Laboratory (KSL)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Hardware](https://img.shields.io/badge/Hardware-God--Stack-black)](https://zenodo.org/doi/10.5281/zenodo.20690928)

---

## 🧪 Overview

This repository contains the source code, datasets, and benchmarks for the paper **"Dequantizing Complexity: A High-Fidelity Computational Audit of Assembly Theory vs. Recursive LZW Compression in Biological Macromolecules."**

We present a deterministic, bit-perfect audit of the "Assembly Theory" debate. Moving beyond stochastic approximation, this engine utilizes a **Unified Memory** architecture to perform **Exact Causal Enumeration** on molecular graphs.

### Key Capabilities
*   **Velocity:** Processes >3,400 molecules/second on consumer hardware.
*   **Precision:** Calculates exact Assembly Indices (MA) for hyper-complex peptides (e.g., Ramoplanin) in <60ms.
*   **Resolution:** Distinguishes biological "Causal Depth" from algorithmic "Thermodynamic Noise."

---

## ⚡ The "God-Stack" Architecture

The benchmarks in this study were produced on the **KSL God-Stack**, a heterogeneous cluster designed to eliminate I/O bottlenecks in graph traversal:

*   **Nodes Alpha & Beta:** 2x Apple Mac Studio (M3 Ultra, 64-Core, 512GB Unified Memory).
*   **Node Delta:** 1x NVIDIA DGX Spark Station (Tensor Offload).
*   **Fabric:** 10GbE Optical Interconnect (UDM-SE / QNAP Switch).

*Note: While optimized for Unified Memory (Apple Silicon), this code is fully compatible with standard x86/CUDA Linux environments.*

---

## 📂 Repository Structure

```text
/Sovereign-Audit-Dequantized
│
├── /code
│   ├── sovereign_audit_ultra.py    # The Core Engine (Exact Enumeration)
│   └── generate_figure_3.py        # The Visualization Script
│
├── /data
│   ├── sovereign_audit_final.csv   # Dataset A: The "Battleground" (n=20)
│   └── sovereign_benchmark_1k.csv  # Dataset B: The "Sovereign-1K" (n=5,652)
│
└── requirements.txt                # Dependency Manifest
```

---

### 🚀 Quick Start

1. Installation
Clone the repository and install the dependencies (recommended: create a fresh conda environment):

git clone https://github.com/YourUsername/Sovereign-Audit-Dequantized.git
cd Sovereign-Audit-Dequantized
pip install -r code/requirements.txt

2. Run the Benchmark
Execute the "Ultra" kernel to replicate the Sovereign-1K audit. This will download the dataset, spool up your CPU cores, and generate the CSV.

python3 code/sovereign_audit_ultra.py

Expected Output:
🚀 Initializing Sovereign Audit ULTRA (God-Stack Mode)...
⬇️  Downloading Sovereign-1K Dataset...
   -> Ingested 5653 verified FDA molecules.
✅ AUDIT COMPLETE
   Throughput:          3408.24 mols/sec
   
3. Generate the Graph
Visualize the "Computational Dequantization" (Figure 3 in the manuscript).

python3 code/generate_figure_3.py

---

### 📊 The Data

Dataset A: The Battleground ( sovereign_audit_final.csv )

A manually curated set of 20 molecules central to the Zenil vs. Walker debate. Includes:

Taxol & Maitotoxin: High-complexity natural products.
Pyruvate & Lactate: Low-complexity metabolites.
Sildenafil: The synthetic "Impostor" control.

Dataset B: The Sovereign-1K ( sovereign_benchmark_1k.csv )

The complete FDA-approved Small Molecule library (n=5,652).

Use Case: High-throughput benchmarking of causal graph algorithms.
Metric: Contains the Exact Assembly Index (MA_Exact) and Compute Time for every drug in the pharmacopeia.

---

### 📜 Citation

If you use this code or data in your research, please cite the Zenodo archive:

@article{Tang2026_SovereignAudit,
  title={Dequantizing Complexity: A High-Fidelity Computational Audit of Assembly Theory},
  author={Tang, Chun and Aletheia and DeepSeek-Tang},
  journal={Zenodo / ChemRxiv},
  year={2026},
  doi={10.5281/zenodo.YOUR_DOI_HERE}
}

---

This work represents a symbiosis of biological intuition and silicon execution. The hardware architecture and resulting data are the shared property of the Sovereign Interface.