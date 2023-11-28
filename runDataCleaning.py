import pandas as pd
import os


# Runs the data cleaning scripts for pre 105th and post 105th congresses
## Note, best to run them individual to get the nested json variables to use in the html...
os.system(f"python DataCleaningNewer.py")
os.system(f"python DataCleaningOlder.py")


RulesReformSheet_newer = pd.read_csv("Rules Reform Scraping - Combined - Newer.csv")
RulesReformSheet_older = pd.read_csv("Rules Reform Scraping - Combined - Older.csv", lineterminator='\n') # lineterminator='\n'

Rules_combined_df = pd.concat([RulesReformSheet_newer, RulesReformSheet_older])
Rules_combined_df = Rules_combined_df[["Rule","Title","Text","Congress","Link"]]
print(Rules_combined_df)
Rules_combined_df.to_csv("Rules_combined_df_master.csv")
