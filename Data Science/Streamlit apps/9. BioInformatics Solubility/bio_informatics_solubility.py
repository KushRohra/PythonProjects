import numpy as np
import pandas as pd
import streamlit as st
import pickle
from PIL import Image
from rkdit import Chem
from rkdit.Chem import Descriptors

# Calculate Molecular Descriptors
def AromaticProportion(m):
    aromatic_atoms = [m.GetAtomWithIdx(i).GetIsAromatic() for i in range(m.GetNumAtoms())]
    aa_count = []
    for i in aromatic_atoms:
        if i == True:
            aa_count.append(1)
    AromaticAtom = sum(aa_count)
    HeavyAtom = Descriptors.HeavyAtomCount(m)
    AR = AromaticAtom/HeavyAtom
    return AR

def generate(smiles, verbose=False):
    moldata = []
    for elem in smiles:
        mol = Chem.MolFromSmiles(elem)
        moldata.append(mol)
    baseData = np.arrange(1)
    i = 0
    for mol in moldata:
        desc_MolLogP = Descriptors.MolLogP(mol)
        desc_MolWt = Descriptors.MolWt(mol)
        desc_NumRotateableBonds = Descriptors.NumRotateableBonds(mol)
        desc_AromaticProportion = AromaticProportion(mol)

        row = np.array([
            desc_MolLogP,
            desc_MolWt,
            desc_NumRotateableBonds,
            desc_AromaticProportion
        ])
        if i == 0:
            baseData = row
        else:
            baseData=np.vstack([baseData, row])
        i += 1

    columnNames=["MolLogP", "MolWt", "NumRotatableBonds", "AromaticProportion"]
    descriptors = pd.DataFrame(data=baseData, column=columnNames)

    return descriptors

# Page Title
image = Image.open('solubility-logo.jpg')
st.image(image, use_column_width=True)

st.wrtie("""
    # Molecular Stability Prediction Web App
    This app predicts the **Solubility (LogS)** values of molecules
""")

# Input Molecules
st.sidebar.header('User Input Features')

# Read SMILES input
SMILES_INPUT = "NCCC\nCCC\nCN"

SMILES = st.sidebar.text("SMILES Input", SMILES_INPUT)
SMILES = "C\n" + SMILES
SMILES = SMILES.split("\n")

st.header("Input SMILES")
SMILES[1:]

# Calculate Molecular Descriptors
st.header('Computed molecular descriptors')
X = generate(SMILES)
X[1:]

load_model = pickle.load(open('solubility_model.pkl', 'rb'))

# Apply Prediction
prediction = load_model.predict(X)

st.header('Predicted LogS Values')
prediction[1:]