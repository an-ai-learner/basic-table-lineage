import pandas as pd
import json
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Convert table lineage CSV to JSON for vis.js")
parser.add_argument("input_csv", help="Input CSV filename (e.g., table_lineage.csv)")
parser.add_argument("output_json", help="Output JSON filename (e.g., table_lineage2.json)")
args = parser.parse_args()

# Read the CSV
df = pd.read_csv(args.input_csv)

# Build nodes and edges lists
nodes = []
edges = []

for name in df['name']:
    nodes.append({"id": name, "label": name})

for _, row in df.iterrows():
    downstreams = str(row['downstream']).replace('"', '').split(',')
    for downstream in downstreams:
        downstream = downstream.strip()
        if downstream and downstream.lower() != 'nan':
            edges.append({"from": row['name'], "to": downstream})

# Save as JSON
data = {"nodes": nodes, "edges": edges}
with open(args.output_json, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"Conversion complete! JSON saved to {args.output_json}")