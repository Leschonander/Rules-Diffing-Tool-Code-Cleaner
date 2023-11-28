import pandas as pd

RulesReformSheet = pd.read_csv("Rules Reform Scraping Freshsheet - Sheet1 (11).csv") # 8
congress_list = [
    '105th','104th', '103rd', '102nd', '101st', '100th', '99th', '98th', '97th', '96th', '95th', '94th', '93rd', '92nd', '91st', '90th',
    '89th', '88th', '87th', '86th', '85th', '84th', '83rd', '82nd', '81st', '80th', '79th', '78th'
    ]

RulesReformSheet["Congress"] = RulesReformSheet["Congress"].astype(str)
RulesReformSheet = RulesReformSheet.query("Congress != 'nan'")
RulesReformSheet["Congress"] = RulesReformSheet["Congress"].apply(lambda x: x.strip())

RulesReformSheet = RulesReformSheet.query("Congress != @congress_list")



### Look up variables
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].fillna(method="ffill")
#### Clean Rules Titles
# [t.replace("\n,", " ") for t in Titles]
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: x.replace("\r", ""))
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: x.replace("\n", " "))
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: x.strip())
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: x.upper())
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: x.replace("TIE", "THE"))
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: x.replace("TIIE", "THE"))

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "THE SPEAKER" if "THE SPEAKER." in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "THE SPEAKER" if "THE SPEAKER." in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "THE HALL OF THE HOUSE" if "THE HALL OF THE HOUSE." in x else x)


RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "FINANCIAL DISCLOSURE" if 'FINANCIAL DISCLOSURE' in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "STATUTORY LIMIT ON THE PUBLIC DEBT" if 'STATUTORY LIMIT ON PUBLIC DEBT' in x else x)


#### Cleaning up the Title Text
RulesReformSheet["Title"] = RulesReformSheet["Title"].astype(str)
RulesReformSheet = RulesReformSheet.query("Title != 'nan'")

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: x.replace("\n", " "))
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: x.replace("\r", ""))
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: x.strip())

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "STATUTORY LIMIT ON THE PUBLIC DEBT" if 'STATUTORY LIMIT ON PUBLIC DEBT' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: x.title() if x.isupper() else x)
# For those uppercase rules...


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Conference reports; amendments reported in disagreement" if 'reports; amendments reported' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Sergeant-at-Arms" if 'Sergeant at Arms' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Tax and tariff measures and amendments" if 'Tax and tariffTax and tariff measures and amendments' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Recess and Convening Authorities" if 'Recess and convening authorities' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Notice of Actions Taken to Comply with Ethics Agreements" if 'Notioe of Actions Taken to Comply with Ethics Agreements' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Limitations on use of official and unofficial accounts" if 'Limitations on use of official and Unofficial accounts' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Filing and printing of reports" if 'Filing and priLting of reports' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker preserves order on floor in galleries and lobby" if 'Speaker preserves order on floor in galleries and lobby.' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's control of the Hall, corridors, and rooms" if "Speaker's control of the Hall, corridors, and rooms." in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions of order subject to appeal" if "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions of order subject to appeal." in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Voting viva voce, by division, by electronic device" if "Voting viva voce, by division, by electronic device." in x else x)


#### Cleaning it up for committees
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Science, Space, and Technology" if 'Committee on Science and Technology' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Science, Space, and Technology" if 'Committee on Science' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Rules" if 'Committee on .Rules' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Financial Services" if 'Committee on Banking and Financial Service' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Foreign Affairs" if 'Committee on International Relations' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Foreign Affairs" if 'Committee on International Relations.' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Education and Labor" if 'Committee on Education and the Workforce' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Oversight and Reform" if 'Committee on Oversight and Government Reform' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Oversight and Reform" if 'Committee on Government Reform' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Natural Resources" if 'Committee on Resources' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Energy and Commerce" if 'Committee ou Energy and Commerce' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Energy and Commerce" if 'Committee on Commerce' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Armed Services" if 'Conunittee on Armed Services' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Armed Services" if 'Committee on National Security' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Veterans’ Affairs" if "Committee on Veterans' Affairs" in x else x)



RulesReformSheet["Text"] = RulesReformSheet["Text"].astype(str)
RulesReformSheet["Text"] =  RulesReformSheet["Text"].apply(lambda x: x.replace('\t', ''))

# This code combines the rules for a given congress to generate the full rule

grouped_Rules = RulesReformSheet.groupby(['Rule', 'Congress'])['Text'].agg(''.join).reset_index()
grouped_Rules["Title"] = grouped_Rules["Rule"]
grouped_Rules = grouped_Rules[["Rule", "Title", "Text", "Congress"]]
grouped_Rules["Title"] = grouped_Rules["Title"].apply(lambda x: "Full Rule for: " + x)
grouped_Rules["Link"] = ""

combined_df = pd.concat([RulesReformSheet, grouped_Rules])
print(combined_df)
combined_df = combined_df[combined_df['Title'].notna()]

# This creates the nested 

nested_rules = combined_df.drop_duplicates(subset=['Rule', "Title"])
nested_rules = dict(nested_rules.groupby('Rule')['Title'].apply(list))
print("---Nested Rules---")

print(nested_rules)

combined_df.to_csv("Rules Reform Scraping - Combined - Newer.csv")

# This code generates 2 things
# First JSON for the selects on the website
# Secondly it generates the code to merge the regular csv and the aggergated rules
