#This code cannot replace "N" to "Q". Needs manually checking

import pandas as pd

# Load the CSV file
input_file = "/Users/Your file path.csv"  # Replace with the file path of your input file
output_file = "/Users/Your file path_modified.csv"    # Replace with the file path of your output file

df = pd.read_csv(input_file)

# Replace [], (), and ending symbol
# Remove '(' and ')' from column 'Glycan_structure', handling NaN values safely
df['Glycan_structure'] = df['Glycan_structure'].astype(str).str.replace(r'[()]', '', regex=True) # Replace with your column name

# Step 2: Replace '[' with '(' and ']' with ')'
df['Glycan_structure'] = df['Glycan_structure'].str.replace('[', '(', regex=False).str.replace(']', ')', regex=False) # Replace with your column name

# Step 3: Remove '-ol' at the sequence ending if there is any. 
df['Glycan_structure'] = df['Glycan_structure'].str.replace('-ol', '', regex=False)  # Replace with your column name

# Step 7: Replace "ＸＸＸ" with "OOO"
df['Glycan_structure'] = df['Glycan_structure'].str.replace('GlcNAc', 'GN', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('GalNAc', 'AN', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Neu5Ac', 'NN', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Neu5Gc', 'NG', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('KDN', 'K', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Kdo', 'W', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('GalA', 'L', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('ᴅ-IdoA', 'I', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Araf', 'R', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('GlcA', 'U', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('ᴅ-Api', 'P', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Fruf', 'E', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Rib-ol', 'T', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Rbo', 'T', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('NAc', 'N', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Pyr', 'PYR', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('-oic', 'CA', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('-amine', 'A', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('-amide', 'AO', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('-one', 'K', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Glc', 'G', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Gal', 'A', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Man', 'M', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Neu', 'N', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Rha', 'H', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Fuc', 'F', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Xyl', 'X', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Rib', 'B', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('All', 'O', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Asc', 'C', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Pe', 'PE', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('In', 'IN', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Me', 'ME', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Ac', 'T', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Pc', 'PC', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Sh', 'SH', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('Ep', 'EP', regex=False)
df['Glycan_structure'] = df['Glycan_structure'].str.replace('d', 'D', regex=False)
#df['Glycan_structure'] = df['Glycan_structure'].str.replace('', '', regex=False)
#df['Glycan_structure'] = df['Glycan_structure'].str.replace('', '', regex=False)

# Step 7: Remove "1-", "2-", "3-" from the linkage type in each cell
df['Glycan_structure'] = df['Glycan_structure'].str.replace('1-', '', regex=False)

df['Glycan_structure'] = df['Glycan_structure'].str.replace('2-', '', regex=False)

df['Glycan_structure'] = df['Glycan_structure'].str.replace('3-', '', regex=False)


# Save to a new CSV file
df.to_csv(output_file, index=False)

print(f"Modified file saved as {output_file}")
