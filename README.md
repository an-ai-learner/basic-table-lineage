# Table Lineage Visualisation

This project helps you visualize table lineage from a CSV file.

## Features

1. **CSV to JSON Conversion**
   - Convert any `input.csv` file (with columns: `name`, `upstream`, `downstream`) to a JSON format suitable for visualization.
   - Usage:
     ```
     python src/table_lineage_csv_2_json.py input/input.csv output/output.json
     ```

2. **Table Lineage Rendering**
   - Use the generated JSON file to render an interactive lineage graph in your browser.
   - Open `src/testvis.html` and upload your JSON file to view and explore the lineage.

## CSV Structure

| name      | upstream      | downstream    |
|-----------|--------------|--------------|
| table_a   |              | table_b      |
| table_b   | table_a      | table_c      |
| table_c   | table_b      |              |

## Getting Started

1. Place your CSV file in the `input/` folder.
2. Run the conversion script to generate a JSON file.
3. Open `src/testvis.html` and upload your JSON file to visualize the lineage.
