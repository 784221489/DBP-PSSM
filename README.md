# DBP-PSSM
DNA-binding protein predicting
## DataSet
The raw sequences of PDB1075 and PDB186 datasets can be obtained from original data
## Feature extraction
you must use python3 version to extract features
### Local_DPP method
Using the PSI-BLAST to obtain the PSSM matrix and localdpp.py for extracting features.

python localdpp.py countpositive countnege lamudamax n

The countpositive(countnege) is the amount of positive(negative) samples.

The suggested values of lamudamax and n are 2 and 2.


When used Local_DPP method,you need to cite the following papers:

Wei, L., et al. (2017). "Local-DPP: An improved DNA-binding protein prediction method by exploring local evolutionary information." Information Sciences 384: 135-144.

Liu, X.-J., et al. (2018). "A Model Stacking Framework for Identifying DNA Binding Proteins by Orchestrating Multi-View Features and Classifiers." Genes 9(8): 394.

### PSSM-400 method
Using the PSI-BLAST to obtain the PSSM matrix and PSSM400.py for extracting features.

When used PSSM-400 method,you need to cite the following papers:

Kumar, M., et al. (2007). "Identification of DNA-binding proteins using support vector machines and evolutionary profiles." BMC bioinformatics 8(1): 463.

### Sliding window method
Using the PSI-BLAST to obtain the PSSM matrix and Sliding window.py for extracting features.
### aac method
Using the raw sequence and aac.py for extracting features.
## feature selection
mRMR algorithm you can download from http://penglab.janelia.org/proj/mRMR/#c++.

