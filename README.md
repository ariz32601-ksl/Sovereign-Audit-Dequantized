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
