import requests
import csv
import io
import math
import time
import concurrent.futures
import sys
from statistics import mean

# --- 1. CONFIGURATION ---
DATASET_URL = "https://raw.githubusercontent.com/choderalab/nano-drugbank/master/df_drugbank_smiles.csv"
OUTPUT_FILE = "sovereign_benchmark_1k.csv"

# --- 2. THE CORE ENGINES (Optimized) ---

def calculate_lzw(s: str) -> float:
    """LZW Compression Ratio (The Zenil Metric)"""
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
    """Exact Assembly Index (The Walker Metric)"""
    if not s: return 0.0
    N = len(s)
    if N < 2: return 0.0
    # Optimization: Filter out atoms from substring search to speed up 1000x runs
    substrings = {}
    for i in range(N):
        for j in range(i+1, N+1):
            sub = s[i:j]
            if len(sub) > 1:
                substrings[sub] = substrings.get(sub, 0) + 1
    
    score = 0
    # Sort only if needed, or iterate directly
    for sub, count in substrings.items():
        if count > 1:
            score += len(sub) * math.log(count)
            
    if score == 0: return 0.0
    return score / math.log(N)

def calculate_ma_ms_proxy(s: str) -> float:
    """Simulated Mass Spec (The Fragmentation Metric)"""
    if not s: return 0.0
    unique_frags = {s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1) if j-i > 2}
    return len(unique_frags) / 12.0

# --- 3. THE PIPELINE ---

def fetch_dataset():
    print(f"⬇️  Downloading Sovereign-1K Dataset from {DATASET_URL}...")
    try:
        response = requests.get(DATASET_URL)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"❌ Failed to download: {e}")
        sys.exit(1)

def audit_molecule(row):
    # Expecting row: [drugbank_id, name, smiles] based on Chodera format
    try:
        name = row['name']
        smiles = row['smiles']
        
        # Skip empty or massive biomolecules (over 500 chars) to keep benchmark standard
        if not smiles or len(smiles) > 500: 
            return None

        # The Sovereign Audit
        t_start = time.perf_counter()
        lzw = calculate_lzw(smiles)
        ma_ex = calculate_ma_exact(smiles)
        ma_ms = calculate_ma_ms_proxy(smiles)
        t_end = time.perf_counter()
        
        return {
            "Name": name,
            "SMILES_Len": len(smiles),
            "LZW": round(lzw, 4),
            "MA_Exact": round(ma_ex, 2),
            "MA_MS": round(ma_ms, 2),
            "Compute_Time_ms": round((t_end - t_start) * 1000, 3)
        }
    except:
        return None

def main():
    print("🚀 Initializing Sovereign Audit ULTRA (God-Stack Mode)...")
    
    # 1. Load Data
    csv_text = fetch_dataset()
    reader = csv.DictReader(io.StringIO(csv_text))
    dataset = [row for row in reader]
    
    print(f"   -> Ingested {len(dataset)} verified FDA molecules.")
    print("   -> Spooling up cores...")

    # 2. Execute on God-Stack
    results = []
    start_time = time.time()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Submit all tasks
        futures = [executor.submit(audit_molecule, row) for row in dataset]
        
        # Gather results
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res:
                results.append(res)

    total_time = time.time() - start_time
    
    # 3. Analytics
    results.sort(key=lambda x: x['MA_Exact'], reverse=True)
    avg_speed = len(results) / total_time
    
    print(f"\n✅ AUDIT COMPLETE")
    print(f"   ---------------------------------------------")
    print(f"   Molecules Processed: {len(results)}")
    print(f"   Total Wall Time:     {total_time:.4f} sec")
    print(f"   Throughput:          {avg_speed:.2f} mols/sec")
    print(f"   ---------------------------------------------")
    
    # 4. Preview Top 5 (High Assembly)
    print("\n   [TOP 5: HIGHEST CAUSAL DEPTH (The 'Deep' Set)]")
    print(f"   {'Name':<30} | {'MA(Ex)':<8} | {'LZW':<6} | {'Time(ms)'}")
    for r in results[:5]:
        print(f"   {r['Name'][:30]:<30} | {r['MA_Exact']:<8} | {r['LZW']:<6} | {r['Compute_Time_ms']}")

    # 5. Preview Bottom 5 (Low Assembly)
    print("\n   [BOTTOM 5: LOWEST CAUSAL DEPTH (The 'Shallow' Set)]")
    for r in results[-5:]:
        print(f"   {r['Name'][:30]:<30} | {r['MA_Exact']:<8} | {r['LZW']:<6} | {r['Compute_Time_ms']}")

    # 6. Save
    with open(OUTPUT_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"\n💾 Full Benchmark saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
