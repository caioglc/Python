# Imports

from rdkit import Chem
from rdkit.Chem.ChemUtils import SDFToCSV

# Transforming to csv file

with open("DBdrugbank.csv", "w") as file: 
  molecules = Chem.SDMolSupplier( '/content/drive/MyDrive/structures.sdf')
  SDFToCSV.Convert(molecules,file)
