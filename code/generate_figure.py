import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_graph():
    # 1. Load Data
    try:
        df = pd.read_csv("sovereign_benchmark_1k.csv")
    except FileNotFoundError:
        print("❌ CSV not found. Please run the benchmark script first.")
        return

    # 2. Setup the "Publication Look"
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6), dpi=300) # High Res for Paper

    # 3. The Scatter Plot
    # X: SMILES Length (Proxy for Molecular Size)
    # Y: Compute Time (ms)
    # Hue: Log of MA_Exact (Color code by Complexity)
    
    # Add a small constant to MA_Exact to avoid log(0)
    df['Log_MA'] = df['MA_Exact'].apply(lambda x: x if x > 1 else 1)
    
    scatter = sns.scatterplot(
        data=df, 
        x="SMILES_Len", 
        y="Compute_Time_ms",
        hue="Log_MA",
        palette="viridis", 
        size="MA_Exact",
        sizes=(10, 200),
        alpha=0.6,
        edgecolor=None
    )

    # 4. The "Flex" Lines
    plt.axhline(y=100, color='r', linestyle='--', linewidth=1, alpha=0.8)
    plt.text(500, 105, 'Real-Time Threshold (100ms)', color='red', fontsize=9, va='bottom')

    # 5. Annotate The Outliers (Ramoplanin / Top Complexity)
    # Find the point with Max Time
    max_time_row = df.loc[df['Compute_Time_ms'].idxmax()]
    plt.annotate(f"{max_time_row['Name']}\n({max_time_row['Compute_Time_ms']}ms)", 
                 xy=(max_time_row['SMILES_Len'], max_time_row['Compute_Time_ms']), 
                 xytext=(max_time_row['SMILES_Len']-150, max_time_row['Compute_Time_ms']+5),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                 fontsize=8, fontweight='bold')

    # 6. Formatting
    plt.title("Figure 3: Computational De-quantization of the Pharmacopeia (n=5,652)", fontsize=12, fontweight='bold', pad=20)
    plt.xlabel("Molecular Sequence Length (SMILES Characters)", fontsize=10)
    plt.ylabel("Processing Time (milliseconds)", fontsize=10)
    plt.legend(title="Complexity (MA)", loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()

    # 7. Save
    output_file = "figure_3_performance.png"
    plt.savefig(output_file)
    print(f"✅ Graph generated: {output_file}")

if __name__ == "__main__":
    generate_graph()
