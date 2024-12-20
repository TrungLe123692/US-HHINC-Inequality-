# -*- coding: utf-8 -*-
"""3DGraph.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/112ZAiWw_sJ0i9DV2U50GNUX2kPffYea8

# VISUALIZING INCOME DISTRIBUTION
This colab notebook has been shared with you so that you can visualize US income data by state.

Click ***File*** and select ***Save a copy in Drive*** so that you have this file in your own Google drive folder.

After creating a copy, close this file (click the x on the browser tab) and continue working on your copied version by following the steps below.

There are FIVE steps to create a 3D chart of income deciles by state, reflecting population size:

1) Run the cell below to import the visualize function.
"""

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/sangttruong/incomevis.git
# %cd incomevis

import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)
from incomevis.vis import *

"""2) Upload a prepared CSV file. Click the Table of Contents icon (top left), then click the file folder icon (bottom one), and then click the upload file icon. Navigate to the appropriate folder and upload the CSV file.

You can double-click the CSV file to see what is in it.

3) Edit the visualize function in the cell below so that the input_path is correct.

4) Run the visualize function in the cell below.

5) Take a screenshot or click the download icon (down arrow in top right of the output screen).

You can copy-and-paste the visualize command cell repeatedly to run more visualizations.

For detailed documentation:
https://incomevis.readthedocs.io/en/latest/source/incomevis.vis.html#module-incomevis.vis.visualize
"""

visualize(k = 'decile', input_path = '/content/3D Graph template state price.csv', max_income = 400000)