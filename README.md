# Anti-fungal-peptide-prediction

Regression forest machine learning model to predict Antifungal peptide 

Features used to train model :
1) Mass
2) Isoelectric Point of Amino Acid
3) Polarity of Amino Acid
4) Hydrophobicity of Amino Acid
5) Charge of Amino Acid

To run This file we need 2 input files :
1) Train.csv  = File containing 3 columns Id of protein sequence , label of that protein (1 if it is a AFP and -1 if it is not AFP) and protein sequence. Train.csv file is used to train our ml model
2) Test.Csv   = File containing 2 columns Id of protein and protein sequence . For these given protein we have to predict whether these proteins are AFP or not.

Output : Output will be stored in Sample.csv file with two columns : protein id and Label corresponding to that protein id

With this model I got 96% Accuracy on Kaggle

Competition - https://www.kaggle.com/c/iqb2020/overview

Leaderboard - https://www.kaggle.com/c/iqb2020/leaderboard     Team Name - (JAY)

