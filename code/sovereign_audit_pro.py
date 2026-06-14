import math
import concurrent.futures
import time
import csv
import sys
import os

# --- 1. CORE ALGORITHMS ---

def calculate_lzw(s: str) -> float:
    """Standard LZW Compression Ratio"""
    if not s: return 0.0
    dictionary = {chr(i): i for i in range(256)}
    dict_size = 256
    w = ""
    result = []
    for c in s:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    if w:
        result.append(dictionary[w])
    return len(result) / len(s)

def calculate_ma_exact(s: str) -> float:
    """Theoretical Assembly Index (Shortest Path via Reuse)"""
    if not s: return 0.0
    N = len(s)
    if N < 2: return 0.0
    substrings = {}
    for i in range(N):
        for j in range(i+1, N+1):
            sub = s[i:j]
            if len(sub) > 1:
                substrings[sub] = substrings.get(sub, 0) + 1
    
    score = 0
    sorted_subs = sorted(substrings.items(), key=lambda x: len(x[0]), reverse=True)
    for sub, count in sorted_subs:
        if count > 1:
            score += len(sub) * math.log(count) # Pathway weight
            
    if score == 0: return 0.0
    return score / math.log(N)

def calculate_ma_ms_proxy(s: str) -> float:
    """Experimental Proxy (Unique Fragment Count / Simulated Mass Spec)"""
    if not s: return 0.0
    N = len(s)
    unique_frags = set()
    for i in range(N):
        for j in range(i+1, N+1):
            sub = s[i:j]
            if len(sub) > 2: # MS detection limit
                unique_frags.add(sub)
    
    # Normalized against Taxol scale for readability
    return len(unique_frags) / 12.0

# --- 2. PIPELINE LOGIC ---

def process_row(row):
    name = row[0]
    seq = row[1]
    cat = row[2]
    source = row[3]
    
    return {
        "Name": name,
        "Category": cat,
        "Source": source,
        "LZW": round(calculate_lzw(seq), 3),
        "MA_Exact": round(calculate_ma_exact(seq), 2),
        "MA_MS": round(calculate_ma_ms_proxy(seq), 2)
    }

def main():
    print("🚀 Starting Sovereign Audit Pro (CSV Mode)...")
    input_file = "sovereign_molecules.csv"
    output_file = "sovereign_audit_final.csv"
    
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found. Run generate_csv.py first.")
        sys.exit(1)
        
    # Read Data
    dataset = []
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader) # Skip header
        for row in reader:
            if row: dataset.append(row)
            
    print(f"   -> Loaded {len(dataset)} entities from {input_file}")
    
    # Compute
    results = []
    start = time.time()
    
    # Utilize God-Stack Local Cores
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = {executor.submit(process_row, row): row for row in dataset}
        for f in concurrent.futures.as_completed(futures):
            results.append(f.result())
            
    # Sort by Experimental MA (MA_MS)
    results.sort(key=lambda x: x['MA_MS'], reverse=True)
    
    end = time.time()
    
    # Display
    print(f"\n   [AUDIT RESULTS - {end-start:.3f}s]")
    print(f"   {'Name':<18} | {'Source':<15} | {'LZW':<6} | {'MA(Ex)':<7} | {'MA(MS)'}")
    print("   " + "-"*70)
    for r in results:
        print(f"   {r['Name']:<18} | {r['Source']:<15} | {r['LZW']:<6} | {r['MA_Exact']:<7} | {r['MA_MS']}")

    # Save
    if results:
        keys = results[0].keys()
        with open(output_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(results)
        print(f"\n✅ Results saved to {output_file}")

if __name__ == "__main__":
    main()
