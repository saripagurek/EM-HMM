# EM-HMM

Python program to generate and visualize a Hidden Markov Model from inputted eye tracking data. 

Dependencies:
- matplotlib $ pip install matplotlib
- seaborn $ pip install seaborn
- hmmlearn $ pip install hmmlearn

Input data must be a csv file with the format:
TRIAL_INDEX,	CURRENT_FIX_X,	CURRENT_FIX_Y,	TARGET_X_REAL,	TARGET_Y_REAL,	TARGET_X_EXPECTED,	TARGET_Y_EXPECTED
** Note that headings do not matter **

Program works by categorizing fixation data into specified regions of the screen. Change the screen size and number of desired regions in main.py (see To Run).

To Run:
- From project directory, edit 'input_file' in main.py to your chosen data set
- Alter the variables 'screen_width', 'screen_height', 'num_rows', 'num_cols' to match your data
- Run main.py $ python main.py
