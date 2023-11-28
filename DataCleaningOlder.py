import pandas as pd

RulesReformSheet = pd.read_csv("Rules Reform Scraping Freshsheet - Sheet1 (11).csv") # 8

# Need list of older rules because they are formatted differently
congress_list =[
    '105th','104th', '103rd', '102nd', '101st', '100th', '99th', '98th', '97th', '96th', '95th', '94th', '93rd', '92nd', '91st', '90th',
    '89th', '88th', '87th', '86th', '85th', '84th', '83rd', '82nd', '81st', '80th', '79th', '78th'
    ]

RulesReformSheet["Congress"] = RulesReformSheet["Congress"].astype(str)
RulesReformSheet = RulesReformSheet.query("Congress != 'nan'")
RulesReformSheet["Congress"] = RulesReformSheet["Congress"].apply(lambda x: x.strip())

RulesReformSheet = RulesReformSheet.query("Congress == @congress_list")
### Look up variables
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].fillna(method="ffill")
RulesReformSheet["Text"] = RulesReformSheet["Text"].astype(str)

print(RulesReformSheet)

### Clean Rules Titles

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: x.rstrip("."))
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXXIX. MESSAGES." if 'XXXIX.MESSAGES.' in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XII. RESIDENT COMMISSIONER AND DELEGATES." if 'XII. RESIDENT COMMISSIONER FROM PUERTO RICO AND DELEGATE FROM THE DISTRICT OF COLUMBIA.' in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XII. RESIDENT COMMISSIONER AND DELEGATES." if 'XII. RESIDENT COMMISSIONER FROM PUERTO RICO AND DELEGATE FROM THE DISTRICT OF COLUMBIA' in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XII. RESIDENT COMMISSIONER AND DELEGATES." if 'XII. RESIDENT COMMISSIONER AND DELEGATES' in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XII. RESIDENT COMMISSIONER AND DELEGATES." if 'XII. RESIDENT COMMISSIONER FROM PUERTO RICO AND DELEGA TE FROM THE DISTRICT OF COLUMBIA' in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XII. RESIDENT COMMISSIONER AND DELEGATES." if 'XII. DELEATES' in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XII. RESIDENT COMMISSIONER AND DELEGATES." if 'XII. DELEGATES' in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XII. RESIDENT COMMISSIONER AND DELEGATES." if 'XII. DELEGATES AND RESIDENT COMMISSIONER' in x else x)


RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XIII. CALENDARS AND COMMITTEE REPORTS" if 'XIII. CALENDARS AND REPORTS OF COMMITTEES' in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XIII. CALENDARS AND COMMITTEE REPORTS" if "XIII. CALENDARS AND COMMITTEE REPORTS." in x else x)


RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XIV. OF DECORUM AND DEBATE" if 'XIV.OF DECORUM AND DEBATE' in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XLIX. ESTABLISHMENT OF STATUTORY LIMIT ON THE PUBLIC DEBT" if 'XLIX. ESTABLISHMEN T OF STATUTORY LIMIT ON THE PUBLIC DEBT' in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XX. OF AMENDMENTS OF THE SENATE" if 'XX. OF AMENDMENTS OF THE SENATE' in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXII. OF PETITIONS, MEMORIALS, BILLS, AND RESOLUTIONS" if "XXII. OF PETITIONS, MEMORIALS, BILLS, AND\r\n\r\nRESOLUTIONS" in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXXIX. MESSAGES" if "XXXIX.MESSAGES" in x else x)


RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "L. PROCEDURE FOR RESPONSE TO SUBPOENAS" if "L. PROCEDURE FOR RESPONSE TO SUBPENAS" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "VIII. DUTIES OF THE MEMBERS" if "VIII. OF THE MEMBERS" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XLIV. FINANCIAL DISCLOSURE" if "XLIV. FINANCIAL DISCLOSURE.\n" in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XLIV. FINANCIAL DISCLOSURE" if "XLIV. FINANCIAL DISCLOSURE. (Effective through June 30, 1977)" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XV. ON CALLS OF THE ROLL AND HOUSE" if "XV. ON.CALLS OF THE ROLL AND HOUSE" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXXV. PAY OF WITNESSES" if "XXXV.  PAY OF WITNESSES" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXXIV. OFFICIAL AND OTHER REPORTERS" if "XXXXIV. OFFICIAL AND OTHER REPORTERS" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXXVI. PAPERS" if "XXXVI. PRESERVATION AND AVAILABILITY OF NONCURRENT RECORDS OF THE HOUSE" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXXII. OF ADMISSION TO THE FLOOR" if "XXXII. OF ADMISSION TO THE FLOORM" in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXXII. OF ADMISSION TO THE FLOOR" if "XXXIII. OF ADMISSION TO THE FLOOR" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXV. PRIORITY OF BUSINESS" if "XXV.PRIORITY OF BUSINESS" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXIII. OF COMMITTEES OF THE WHOLE HOUSE" if "XXIII. OF COMMITEES OF THE WHOLE HOUSE" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXII. OF PETITIONS, MEMORIALS, BILLS, AND RESOLUTIONS" if "XXII. OF PETITIONS., MEMORIALS, BILLS, AND RESOLUTIONS" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XVIII. RECONSIDERATION" if "XVIII. RECONSIDERATION.\n" in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XVIII. RECONSIDERATION" if "XVIII. RECONSDIERATION" in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XVIII. RECONSIDERATION" if "XVIII. RECONSIDERATION " in x else x)


RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "LI. EMPLOYMENT PRACTICE" if "LI. EMPLOYMENT PRACTICES" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XIX. OF AMENDMENT" if "XIX. OF AMENDMENTS" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XLIII. JEFFERSON'S MANUAL" if "XLIII. JEFFERSON 'S MIANUAL" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XVII. PREVIOUS QUESTION" if "XVII. PREVIOUS QUESTION " in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XX. OF AMENDMENTS OF THE SENATE" if "XX.OF AMENDMENTS OF THE SENATE " in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XX. OF AMENDMENTS OF THE SENATE" if "XX.OF AMENDMENTS OF THE SENATE" in x else x)


RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXVI. UNFINISHED BUSINESS OF THE SESSION" if "XXVI. UNFINISHED BUSINESS OF THIE SESSION" in x else x)
RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXVI. UNFINISHED BUSINESS OF THE SESSION" if "XXVI. UNFINISHED BUSINESS- OF THE SESSION" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXXI. HALL OF THE HOUSE" if "XXXII. HALL OF THE HOUSE " in x else x)


RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXXIV. ADMISSION TO THE GALLERIES" if "XXXIV. OF ADMISSION TO THE GALLERIES" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXXV. OFFICIAL AND OTHER REPORTERS" if "XXXV. OFFICIAL AND OM IER REPORTERS" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXXV. OFFICIAL AND OTHER REPORTERS" if "XXXV. OFFICIAL AND OM IER REPORTERS" in x else x)

RulesReformSheet["Rule"] = RulesReformSheet["Rule"].apply(lambda x: "XXIII. OF COMMITTEES OF THE WHOLE HOUSE" if "XXIII. OF COMMITTEES OF THE WHIOLE HOUSE" in x else x)


### Cleaning up the Title Text
RulesReformSheet["Title"] = RulesReformSheet["Title"].astype(str)
RulesReformSheet = RulesReformSheet.query("Title != 'nan'")


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: x.rstrip("."))
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: x.rstrip("."))
#RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: x.capitalize())


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Definition and Precedence of Questions of Privilege" if 'Definition and precedence of Questions of Privilege' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Definition and Precedence of Questions of Privilege" if 'Definition and precedence of questions of privilege' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Definition and Precedence of Questions of Privilege" if 'Definition and preceedence of questions of privilege' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Response to Subpoenas" if 'RESPONSE TO SUBPOENAS' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Response to Subpoenas" if 'Response to subpoenas' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Response to Subpoenas" if 'Response to Subpenas' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "General duties of the Doorkeeper" if 'General duties of the Door Keeper' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The Doorkeeper clears the floor of unauthorized persons" if 'The Door Keeper clears the floor of unauthorized persons' in x else x)

#### I.

RulesReformSheet.loc[RulesReformSheet["Rule"] == "I. DUTIES OF THE SPEAKER", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "I. DUTIES OF THE SPEAKER", "Title"].apply(lambda x: x.capitalize())


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Travel Authority" if 'Travel authority' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The Speakers vote. Tie vote" if 'The Speakers vote, Tie vote' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Travel Authority" if 'Travel authority' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's control of the Hall, corridors, and rooms" if 'Speakers control of the Hall, corridors and rooms' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's control of the Hall, corridors, and rooms" if 'Speakers control over the hall, corridors and rooms' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's control of the Hall, corridors, and rooms" if 'Speaker preserves order on floor, and in galleries and lobby' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's control of the Hall, corridors, and rooms" if "Speaker's control of the hall, corridors and rooms" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's control of the Hall, corridors, and rooms" if "Speakers control over the hall, corridors and rooms" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's control of the Hall, corridors, and rooms" if "Speaker's control of the hall, corridors and rooms" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's control of the Hall, corridors, and rooms" if "Speakers control of the hall, corridors, and rooms" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's control of the Hall, corridors, and rooms" if "Speakers control of the hall, corridors and rooms" in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Travel Authority" if 'Travel authority' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions of order subject to appeal" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speakers signature to acts,warrants, subpoenas, etc.; and decisions of questions of order subject to appeal" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speakers signature to acts, warrants, subpoenas, etc.. and decision of questions of order subject to appeal" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speaker's signature to acts, warrants, subpoenas, etc.; and decisionof questions of order subject to appeal" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speaker's signature to acts, warrants, subpoenas, etc.: and decision of questions of order subject to appeal. " in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speaker's signature to acts,warrants and subpenas etc.; and decision of questions of order subject to appeal" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speaker's signature to acts, warrants, subpenas, etc.; and decision of questions of order subject to appeal" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speaker's signature to acts, warrants, subpoenas, etc,; and decision of questions of order subject to appeal" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speakers signature to acts,warrants, subpenas, etc; and decisions of questions of order subject to appeal" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speaker's signature to acts, warrants, subpoenas, etc; and decisionof questions of order subject to appeal" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speaker's signature to acts, warrants, subpoenas, etc: and decision of questions of order subject to appeal " in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speaker's signature to acts,warrants and subpenas etc; and decision of questions of order subject to appeal" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speaker's signature to acts, warrants, subpenas, etc; and decision of questions of order subject to appeal" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speakers signature to acts, warrants, subpenas, etc; and decision of questions of order subject to appeal" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of questions order subject to appeal" if "Speaker's signature to acts, warrants, subpoenas, etc.; and decision of order subject to appeal" in x else x)



RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Journal speakers approval" if "Journal; speaker's approval" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Journal speakers approval" if "Journal speaker's approval" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Journal speakers approval" if "Journal speaker's approval" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Journal speakers approval" if "Journal speakers approva" in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker preserves order on floor and in galleries and lobby" if 'Speaker preserves order on floor and  in galleries and lobby' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker preserves order on floor and in galleries and lobby" if 'Speaker preserves order on the floor and in galleries and lobby' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker preserves order on floor and in galleries and lobby" if 'Speaker preserve order on floor and in galleries and lobby' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker preserves order on floor and in galleries and lobby" if 'Speaker preserves order on floor and in galleries' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The speaker's vote, tie vote" if "Speaker's vote. tie vote" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The speaker's vote, tie vote" if "The speaker's vote. tie vote" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The speaker's vote, tie vote" if "The speakers vote. tie vote" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The speaker's vote, tie vote" if "The speaker's vote. tie vot" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The speaker's vote, tie vote" if "Speaker's vote tie vote" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The speaker's vote, tie vote" if "Th speaker's vote. tie vote" in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker pro tempore" if "Speaker's pro tempore" in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Calling the house to order; and approval of journal" if "Calling the house to order; and approval of the journal" in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Putting of the question by the speaker" if "Putting of thr question by the speaker" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Putting of the question by the speaker" if "Putting of the question of the speaker" in x else x)


#### II. 

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Election of officers" if "Election of Officers" in x else x)



#### III.
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Clerks duties at organization" if "Clerk's duties at organization" in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Clerks duty as to Journal and documents" if "Clerk's duty as to Journal and documents" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Clerks duty as to Journal and documents" if "Clerks duty as to Journal and document" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Clerks duty as to Journal and documents" if "Clerk's duty as to Journal and document" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Clerks duty as to Journal and documents" if "Clerk 's duty as to Journal and documents" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Clerks duty as to Journal and documents" if "Clerk's duty as to journal and documents" in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Clerks duties at organization" if "Clerk's duties at organization" in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Clerk furnished a list of reports" if "Clerk's furnished a list of reports" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Clerk furnished a list of reports" if "Clerks furnishes a list of reports" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Clerk furnished a list of reports" if "Clerk furnishes a list of reports " in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Clerk furnished a list of reports" if "Clerk furnishes a list of reports" in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Official to act as Clerk upon designation" if "Official to act as clerk upon designation" in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Administration of vacant Member's office" if "Administration of vacant member's office" in x else x)


#### IIII.
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Sergeant-at-Arms enforces authority of House" if 'Sergeant-at-arms enforces authority of House' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Sergeant-at-Arms enforces authority of House" if 'Sergeant-at-Arms  enforces authority of House' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Sergeant-at-Arms enforces authority of House" if 'Sageant-at Arms enforces authority of House' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Sergeant-at-Arms enforces authority of House" if 'Sargeant-at-Arms enforces authority of the House' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Sergeant-at-Arms enforces authority of House" if 'Sergeant-at-Arms enforces authority of House' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Sergeant-at-Arms enforces authority of House" if 'Sergeant-at-Arms enforcs authority of House' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The mace the symbol of the Sergeant-at-Arms' office" if "The Mace, the symbol of the Sergeant-at-Arms' office" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The mace the symbol of the Sergeant-at-Arms' office" if "The mace, the symbol of the Sargean-at-Arms' office" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The mace the symbol of the Sergeant-at-Arms' office" if "The mace the symbor of the Sargeant-at-Arms'  office" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The mace the symbol of the Sargeant-at-Arms' office" if "The mace the symbor of the Sargeant-at-Arms'  office" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The mace the symbol of the Sergeant-at-Arms' office" if "The mace the symbol of the Sargeant-at-Arms' office" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The mace the symbol of the Sergeant-at-Arms' office" if "The mace the symbol of Sergeant-at-Arms' office" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The mace the symbol of the Sergeant-at-Arms' office" if "The mace, the symbol of the Sargeant-at-Arms' office" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The mace the symbol of the Sergeant-at-Arms' office" if "The mace the symbor of the Sargeant-at-Arms' office" in x else x)


#### IX

#### L.

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Response to Subpoenas" if 'Response to subpenas' in x else x)

#### VI. 

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The Postmaster superintends the House post office" if 'The Postmaster superintends the House Post-office' in x else x)

ReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Commerce" if 'Energy and Commerce' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Budget Act; 15-day referral to Appropriations" if 'Budget act; 15-day referral to appropriation' in x else x)


#### X. STANDING COMMITTEES

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker appoints select and conference committees" if 'Speaker appoints select and conference committee' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Select Committee on Small Business" if 'Select committees on small businesses' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Selection of chairman of committee" if 'Selection of Chairman of Committee' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Selection of chairman of committee" if 'Selection of chairman of the committee' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Names and numbers of the standing committees" if 'Names and numbers of the standing commitees' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Names and numbers of the standing committees" if 'Names and members of the standing committees' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Names and numbers of the standing committees" if 'Names and number of standing committees' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Names and numbers of the standing committees" if 'Names and numbers of standing committees' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Names and numbers of the standing committees" if 'Names and number of the standing committees' in x else x)


#### XI.

RulesReformSheet.loc[RulesReformSheet["Rule"] == "XI. RULES OF PROCEDURES FOR COMMITTEES", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XI. RULES OF PROCEDURES FOR COMMITTEES", "Title"].apply(lambda x: x.capitalize())

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Commitee meetings" if 'Committee meetings' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committees not to sit" if 'Committess not to sit' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Funds for committee staffs; expense resolution" if 'Funds for committe staffs; expense resolution' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Staff committees on appropriations, and budget" if 'Staff, committees on appropriations, and budget' in x else x)
# RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committees not to sit" if 'Professional staff' in x else x)
# ^^ Non partisn/professional the same?

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Appropriation bills; summary report" if 'Appropriation bills: summary reports' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Votes in committees" if 'Votes in committee' in x else x)

# ---

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee rules" if 'Committe rules' in x else x)

# --- The actual committee names... (Need to add Committee on to all of them...)

### Financial Services
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Financial Services" if 'Banking and Financial Services' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Financial Services" if 'Banking Finance and Urban Affairs' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Financial Services" if 'Banking, Currency and Housing' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Financial Services" if 'Banking and Currency' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Financial Services" if 'Banking anad Currency' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Financial Services" if 'Banking and currency' in x else x)

### Foreign Affairs
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Foreign Affairs" if 'International Relations' in x else x)

### Armed Services

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Armed Services" if 'Armed Services' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Armed Services" if 'Military affairs' in x else x)


### House Admin
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on House Administration" if 'House administration' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on House Administration" if 'House Oversight' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Education and Labor" if 'Education and Labor' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Education and Labor" if 'Education and Labor' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Education and Labor" if 'Education' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Education and Labor" if 'Labor' in x else x)

### Natural Resources
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Natural Resources" if 'Interior and Insular affairs' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Natural Resources" if 'Interior and insular affairs' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Natural Resources" if 'Natural Resources' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Natural Resources" if 'Resources' in x else x)

### Goverment Reform and Oversight
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Oversight and Reform" if 'Government Reform and Oversight' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Oversight and Reform" if 'Post Office and Civi Service' in x else x)


### Science
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Science, Space, and Technology" if 'Science, Space, and Technology' in x else x)

### Indian Affairs
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Indian Affairs" if 'Public lands' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Indian Affairs" if 'Indian affairs' in x else x)

### Energy and Commerce
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Energy and Commerce" if 'Commerce' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Energy and Commerce" if 'Interstate and Foreign Commerce' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Energy and Commerce" if 'Interstate and foreign commerce' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Energy and Commerce" if 'Inerstate and foreign commerce' in x else x)

### Transportation
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Committee on Transportation and Infrastructure" if 'Public Works and Transportation' in x else x)

### UnAmerican Activites
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Budget Act; 15-day referral to Appropriations" if 'Budget Act; 15-day Referral to Appropriations' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Budget Act; 15-day referral to Appropriations" if 'Budget Act; 15-Day Refferal to Appropriation' in x else x)
### Misc

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Internal Security" if 'Un-American Activities' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Budget, composition of" if 'Budget, Composition of' in x else x)

## How to handle Permanent Select Committee on Intelligence

#### XII.
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Powers and Privileges of Resident Commissioner and Delegates as to committee service" if 'Powers and Privileges of Resident Commissioner and Delegates as to Committee Service' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Powers and Privileges of Resident Commissioner and Delegates as to committee service" if 'Powers and privileges of Resident Commissioner and Delegates as to committee service' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Powers and Privileges of Resident Commissioner and Delegates as to committee service" if 'Powers and privileges of Resident Commissioner and delegates as to committee service' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Powers and Privileges of Resident Commissioner and Delegates as to committee service" if 'Powers and privileges of Delegates on the floor and as to committee service' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Powers and privileges of Delegates and Resident Commissioner on the floor and as to committee service" if 'Powers and privileges of Delegates and Resident Commissioner on the floor as to committee service' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Powers and privileges of Delegates and Resident Commissioner on the floor and as to committee service" if 'Powers and privileges of Delegates on the floor as to committee service' in x else x)


#### XIII.

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if 'Nonprivileged reports filled with the clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if 'Nonprivileged reports file with the clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if 'Nonprivileged reports filled with the clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if 'Nonprivileged reports file with the clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if 'Nonprivileged repotts filed with the clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if 'Nonprivileged reports files with the clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if 'Nonprivileged reports field with the clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if 'Nonprivileged reports filled with the clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if 'Nonprivileged reports file with the clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if 'Nonprivileged repotts filed with the clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if 'Nonprivileged reports field with the clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if 'Nonprivileged reports filled with the clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if 'Nonprivileged reports file with the clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if 'Nonprivileged repotts filed with the clerk' in x else x)
### ^ Something not catching...

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Calendar for reports of committees" if 'Calendars for reports of committees' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Calendar for reports of committees" if 'Calendars for reports of commitees' in x else x)


#### XIV

RulesReformSheet.loc[RulesReformSheet["Rule"] == "XIV. OF DECORUM AND DEBATE", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XIV. OF DECORUM AND DEBATE", "Title"].apply(lambda x: x.capitalize())
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Obtaining the floor for debate; and relevancy and decorum therein" if 'Obtaining the Floor for Debate; and Relevancy and Decorum Therein' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Obtaining the floor for debate; and relevancy and decorum therein" if 'Obtaining the Floor for Debate; and Relevancy and Decorum Therein' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Obtaining the floor for debate; and relevancy and decorum therein" if 'Obtaining the floor for debate; and relevancy, and decorum therein' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Obtaining the floor for debate; and relevancy and decorum therein" if 'Obtaining the floor for debate; and relevancyand decorum therein' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's power of recognition" if 'Speakers power of recognition' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Member to speak but once to the same question; right to close controlled debate" if 'Member to speak but once to the same question' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Member to speak but once to the same question; right to close controlled debate" if 'Member to speak but once to the same question' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Member to speak but once to the same question; right to close controlled debate" if 'Members to speak but once to the same question' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Gallery occupants not to be introduced" if 'Gallery occupations not to be introduced' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Gallery occupants not to be introduced" if 'Gallery ocupants not to be introduced' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The hour rule in debate" if 'The hout rule in debate' in x else x)


#### XIX
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Amendments to Text and Title" if 'Amendments to text and to title' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Amendments to Text and Title" if 'Amendment to text and to title' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Entry of messages in the Journal and Record" if 'Entry of Messages in the Journal and Record' in x else x)

# ---

#### XL 
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Reception and reference of executive communications including estimates" if 'Reception and reference of executive communications, including estimates ' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Reception and reference of executive communications including estimates" if "Reception and reference of executive communications including estimates " in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Reception and reference of executive communications including estimates" if "Reception and reference of executive communicatios, including estimates" in x else x)


#### XLI
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Officers and employees not to be agents of claims" if 'Officers and Employees Not to be Agents of Claims' in x else x)

#### XLII
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Relations of Jefferson's Manual and Legislative Reorganization Act of 1946 to the rules of the House" if "Relations of Jefferson's Manual and Legislative Reorganizaton Act of 1946 to the Rules of the House" in x else x)

# ---

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Official Conduct of Members, Officers or Employees of the House" if "Official conduct of Members, officers or employees of the House" in x else x)


# XLIII.
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Official Conduct of Members, Officers or Employees of the House" if 'Official conduct of Members, officers, or employees of the House' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Official Conduct of Members, Officers or Employees of the House" if 'Official conduct of members, officers or employees of the house' in x else x)

# ---
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Relations of Jefferson's Manual to the rules of the House" if "Relations of Jefferson's Manual to the Rules of the House" in x else x)


# XLIV
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Financial report disclosing certain financial interests" if 'Financial reports disclosing certain financial interests' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Financial report disclosing certain financial interests" if 'Financial Report Disclosing Certain Financial Interests' in x else x)

# XLIX
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Public Debt Limit" if 'Public debt limit' in x else x)

# XLVII
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Income limitations" if 'Income Limitations' in x else x)

#### VI Duties of the Post master

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The Postmaster superintends the House post office" if 'The Postmaker superintends the House post office' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The Postmaster superintends the House post office" if 'The Post-master superintends the House post-office' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The Postmaster superintends the House post office" if 'The Postmaker superintends the House post office' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The Postmaster superintends the House post office" if 'The Postmaker superintends the House post office' in x else x)

#### XLVIII

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Permanent Select Committee on Intelligence" if 'Permanent select committee on intelligence' in x else x)


#### XV.

RulesReformSheet.loc[RulesReformSheet["Rule"] == "XV. ON CALLS OF THE ROLL AND HOUSE", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XV. ON CALLS OF THE ROLL AND HOUSE", "Title"].apply(lambda x: x.capitalize())
RulesReformSheet.loc[RulesReformSheet["Rule"] == "XV. ON CALLS OF THE ROLL AND HOUSE", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XV. ON CALLS OF THE ROLL AND HOUSE", "Title"].apply(lambda x: x.strip())
RulesReformSheet.loc[RulesReformSheet["Rule"] == "XV. ON CALLS OF THE ROLL AND HOUSE", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XV. ON CALLS OF THE ROLL AND HOUSE", "Title"].apply(lambda x: x.strip())


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The previous question" if 'The Previous Question' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Quorum: when not required" if 'Quorum; when not required' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Quorum call by clerks" if 'Quorum called by clerks' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Quorum call by clerks" if 'Quorum called by clerks' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Quorum call by clerks" if 'Quorum called by clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Quorum call by clerks" if 'Quorum called by clerk' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Quorum call by clerks" if 'Quorum calls by clerk' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Count of those not voting to make a quorum of record on a roll call" if 'Count of those not voting to make a quorum  of record on a roll call' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Call of the roll for the yea-and-nay vote" if 'Call of the roll for the yea-and-nay\r\nvote' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Call of the roll for the yea-and-nay vote" if 'Call of the roll for the \"yea-and-nay\"  vote' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Call of the roll for the yea-and-nay vote" if 'Call of the roll for the yes-and-nay vote' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Call of the roll for the yea-and-nay vote" if 'Call of the roll for the res-and-nay vote' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Call of the roll for the yea-and-nay vote" if 'Call of the roll for the \"yea-and-nay\" vote' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Use of electronic equipment in recording roll calls" if 'Use of electronic equiptment in recording roll calls' in x else x)

# XVI. Motions and Precedence

RulesReformSheet.loc[RulesReformSheet["Rule"] == "XVI. ON MOTIONS, THEIR PRECEDENCE, ETC", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XVI. ON MOTIONS, THEIR PRECEDENCE, ETC", "Title"].apply(lambda x: x.capitalize())

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Motions reduced to writing and entered on the journal" if 'Motion reduced to writing and entered on the journal' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Motions reduced to writing and entered on the journal" if 'Motion reduced to writing and centered on the journal' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Motions reduced to writing and entered on the journal" if 'Motions reduced to writings and entered on the journal' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Precedence of privileged motions" if 'Precedence of priveleged motions' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Precedence of privileged motions" if 'Precendence of privileged motions' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Precedence of privileged motions" if 'The precedence of priviliged motions' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Division of the question" if 'Division of question' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Motion to strike out and insert not divisible" if 'Motion to strike out and insert  not divisible. ' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Motion to strike out and insert not divisible" if 'Motion to strike our and insert not divisible' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Motion to strike out and insert not divisible" if "Motion to strike out and insert  not divisible " in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Dilatory motions pending motions to suspend rules" if 'Dilatory motion pending motions to suspend rules' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Dilatory motions pending motions to suspend rules" if 'Dilatory motions pending motion to suspend rules' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Dilatory motions pending motions to suspend rules" if 'Dilatory motions pending to suspend rules' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Dilatory motions pending motions to suspend rules" if 'Dilatory motions pending motions  to suspend rules' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Dilatory motions pending motions to suspend rules" if 'Dilatory motions pending motion to suspend' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Dilatory motions pending motions to suspend rules" if 'Dilatory motions pending motion to suspend' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Dilatory motions pending motions to suspend rules" if 'Dilatory motion pending motion to suspend rules' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Entry of hour of adjournment on the journal" if 'Entry of hour of ajournment on the journal' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Entry of hour of adjournment on the journal" if 'Entry of hour od adjournment in the journal' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Entry of hour of adjournment on the journal" if 'Entry of our of adjournment on the journal' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Privileged motion for consideration of revenue and appropriation bills" if 'Privileged motion for consideration of revenu and appropriation bills' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Privileged motion for consideration of revenue and appropriation bills" if 'Privileged motions for consideration of revenue and appropriation bills' in x else x)



# XVII (Previous)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The previous question" if 'The Previous Question' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Relation of previous question to failure of a quorum" if 'Relation of Previous Question to Failure of a Quorum' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Relation of previous question to failure of a quorum" if 'Relation of the previous question to failure of a quorum' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Questions of order pending the motion for the previous question" if 'Questions of Order Pending for the Previous Question' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Questions of order pending the motion for the previous question" if 'Question of order pending the motion for the previous question' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Questions of order pending the motion for the previous question" if 'Question of order oending the motion for the previous question' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Questions of order pending the motion for the previous question" if 'Question of order oending the motion for the previous question' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Questions of order pending the motion for the previous question" if 'Questions of order pending for the previous question' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Questions of order pending the motion for the previous question" if 'Questions of order pending the motion for th previous question' in x else x)



# XVIII (Recondisderation)
RulesReformSheet.loc[RulesReformSheet["Rule"] == "XVIII. RECONSIDERATION", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XVIII. RECONSIDERATION", "Title"].apply(lambda x: x.capitalize())

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Motions reduced to writing and entered on the Journal" if 'Motions Reduced to Writing and Entered on the Journal' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Requirement that reports of committee be in writing and be printed" if 'Requirement that reports of committees be in writing and be printed' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Requirement that reports of committee be in writing and be printed" if 'Requirement that reports of committees be in writing and printed' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Application of motion to reconsider to bills in committees" if 'Application of motion to reconsider to bills in committee' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Application of motion to reconsider to bills in committees" if 'Application of motion to reconsider bills in comittees' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Requirement that reports of committee be in writing and be printed" if 'Requirement that report of committees be in writing and be printed' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Application of motion to reconsider to bills in committees" if 'Application of motion to  reconsider to bills in committees' in x else x)


# XX. 
RulesReformSheet.loc[RulesReformSheet["Rule"] == "XX.OF AMENDMENTS OF THE SENATE", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XX.OF AMENDMENTS OF THE SENATE", "Title"].apply(lambda x: x.capitalize())

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Consideration of Senate amendments in Committee of the Whole" if 'Consideration of Senate amendments in Committee of the Whole; motion for conference' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Consideration of Senate amendments in Committee of the Whole" if 'Consideration of Senate amendments in Committee of the Whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Consideration of Senate amendments in Committee of the Whole" if 'Consideration of sSenate Amendments in Committee of the Whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Consideration of Senate amendments in Committee of the Whole" if 'Considertaion of Senate amendments in Committee of the Whole' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Conferees may not agree to certain Senate amendments" if 'Conferees may not agree to certain senate amendments' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Conferees may not agree to certain Senate amendments" if 'Conferees may not agree to certain in Senate amendments' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Conferees may not agree to certain Senate amendments" if 'Conferees may not agree to certain agree to certain Senate amendments' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Conferees may not agree to certain Senate amendments" if 'Conferees may not agree to certain Senate amnedments' in x else x)


#### XI
RulesReformSheet.loc[RulesReformSheet["Rule"] == "XI. RULES OF PROCEDURES FOR COMMITTEES", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XI. RULES OF PROCEDURES FOR COMMITTEES", "Title"].apply(lambda x: x.capitalize())


#### XII

#### XIII

RulesReformSheet.loc[RulesReformSheet["Rule"] == "XIII. CALENDARS AND COMMITTEE REPORTS", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XIII. CALENDARS AND COMMITTEE REPORTS", "Title"].apply(lambda x: x.capitalize())
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Ramseyer rule" if "\"ramseyer rule\"" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Ramseyer rule" if "\"ramseyer rule.\"" in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nonprivileged reports filed with the clerk" if "Non-privileged reports filed with the clerk" in x else x)


#### XXIX
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Secret session of the House" if 'Secret Session of the House' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Secret session of the House" if 'Secret session of the house' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Secret session of the House" if 'Secret session of tho House' in x else x)

### XXV

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Decision of questions as to priority of business without debate" if 'Decision  of questions as to priority of business without debate' in x else x)


# XXVI
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Resumption of business of a preceding session" if 'Resumption of Business of a Preceding Session' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Resumption of business of a preceding session" if 'Resumption of business of a preceeding session' in x else x)

# XXVII
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Motions to suspend the rules" if 'Motions to Suspend the Rules' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The forty minutes of debate on motion to suspend the rules" if 'The Forty Minutes of Debate on Motion to Suspend the Rules' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Motion to discharge a committee" if 'Motion to Discharge a Committee' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The forty minutes of debate on motion to suspend the rules" if 'The forty minutes of debate on motion to susped the rules' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The forty minutes of debate on motion to suspend the rules" if 'The forty minutes of debate on motions to suspend the rules' in x else x)


# XXVIII CONFERENCE REPORTS

RulesReformSheet.loc[RulesReformSheet["Rule"] == "XXVIII. CONFERENCE REPORTS", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XXVIII. CONFERENCE REPORTS", "Title"].apply(lambda x: x.capitalize())
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "High privilege of conference reports; and form of accompanying statement" if 'High privilege of conference reports; and form accompanying statement' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "High privilege of conference reports; and form of accompanying statement" if 'High Privilege of Conference Reports; and Form of Accompanying Statement' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Conferees may report germane modification of amendment in nature of substitute" if 'Conferees may report germane modification of amendment in nature substitute' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Conferees may report germane modification of amendment in nature of substitute" if 'Conferees may reports germane modification of amendment in nature of sustitute' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Conferees may report germane modification of amendment in nature of substitute" if 'Conferees May Report Germane Modification of Amendment in Nature of Substitute' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Time for debate on motions to instruct" if 'Time for Debate' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Motions privileged after 20 calendar days of conference" if 'Motions Privileged After 20 calendar Days of Conference' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The statement accompanying a conference report" if 'The Statement Accompanying a Conference Report' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nongermane matter in conference agreements" if 'Nongermane matter in conference agreements' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nongermane matter in conference agreements" if 'Non-germane matter in conference agreements' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nongermane matter in conference agreements" if 'Nongermane matter in conference agreement' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nongermane matter in conference agreements" if 'Non-germane matters in conference agreements' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nongermane matter in amendments in disagreement" if 'Nongermane Matter inAmendments in Disagreements' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nongermane matter in amendments in disagreement" if 'Nongermane matter inamendments in disagreements' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nongermane matter in amendments in disagreement" if 'Non-germane matter in amendments in disagreement' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Nongermane matter in amendments in disagreement" if 'Non-germane matter in ammendment in disagreement' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Printing of conference reports and statements in the record" if 'Printing of conference reports and statement in the record' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Printing of conference reports and statements in the record" if 'Printing not conference reports and statements in the record' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Printing of conference reports and statements in the record" if 'Printing of conference reports and statements in the records' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "High privilege of conference reports; and form of accompanying statement" if 'High privilege of conference report; and form of accompanying statement' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "High privilege of conference reports; and form of accompanying statement" if 'High privilege of conference reports; and form of accoompanying statement' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "High privilege of conference reports; and form of accompanying statement" if 'High privilege of conference reports; and form of accompanying' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Conferees may report germane modification of amendment in nature of substitute" if 'Conferees may report germane modification of amendments in nature of substitute' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Conferees may report germane modification of amendment in nature of substitute" if 'Conferees may report germane modification of amndment in nature of substitute' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Conferees may report germane modification of amendment in nature of substitute" if 'Conferees may report germane moderation of amendment in nature of substitute' in x else x)


# XXI. On Bills

RulesReformSheet.loc[RulesReformSheet["Rule"] == "XXI. ON BILLS", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XXI. ON BILLS", "Title"].apply(lambda x: x.capitalize())

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Reading, engrossment, and passage of bills" if 'Reading, engrossment and passage of bills' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Reading, engrossment, and passage of bills" if 'Reading, engrossment and passage of bills' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Unauthorized appropriations in reported general appropriation bills or amendments thereto" if 'Unauthorized appropriation in reported general appropriation bills or amendments thereto' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Unauthorized appropriations in reported general appropriation bills or amendments thereto" if 'Unauthorized appropriations and legislation on general appropriation bills' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Unauthorized appropriations in reported general appropriation bills or amendments thereto" if "Unauthorized appropriations and legislation on general appropriation bills " in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Printed hearings and reports on appropriatioin bills" if 'Printed hearings and repots on appropriation bills' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Printed hearings and reports on appropriatioin bills" if 'Printed hearings and reports on appropriation billls' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Restriction on bills and amendments carrying taxes or tariffs" if 'Restriction on bills and amendments carrying taxes ans tariffs' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Restriction on bills and amendments carrying taxes or tariffs" if 'Restriction on bills and amendments carrying taxes or tarrifs' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Restriction on the reference of claims" if 'Restriction of the reference of claims' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Reappropriations prohibited" if 'Reappropiations prohibited' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Restriction of power to report appropriation" if 'Restriction of power to reports appropriations' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Restriction of power to report appropriation" if 'Restriction of power to report appropriation' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Restriction of power to report appropriation" if 'Restriction of power to report appropriations' in x else x)


## ---  XXI. OF PETITIONS, MEMORIALS, BILLS, AND RESOLUTIONS

RulesReformSheet.loc[RulesReformSheet["Rule"] == "XXII. OF PETITIONS, MEMORIALS, BILLS, AND RESOLUTIONS", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XXII. OF PETITIONS, MEMORIALS, BILLS, AND RESOLUTIONS", "Title"].apply(lambda x: x.capitalize())

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Introduction and reference of petitions, memorials, and private bills" if 'Introduction, reference, and change of reference of public bills, memorials, and resolution' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Introduction and reference of petitions, memorials, and private bills" if 'Introduction , reference, and change of reference of public bills, memorials, and resolutions' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Introduction and reference of petitions, memorials, and private bills" if 'Introduction and reference of petition, memorials, and private bills' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Introduction and reference of petitions, memorials, and private bills" if 'Introduction and reference of petitions, memorials. and private bills' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Resolution of inquiry" if 'Resolutions of inquiry' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Correction of errors in reference; and relation to jurisdiction" if 'Correction of errors in reference;  and relation to jurisdiction' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Correction of errors in reference; and relation to jurisdiction" if 'Correction of errors in reference; and jurisdiction' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Correction of errors in reference; and relation to jurisdiction" if 'Correction of erors in reference; and relation to jurisdiction' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Introduction of bills, resolutions, or memorials by request" if 'Introduction of bills, resolutions, or memorials, by request' in x else x)



#### XXX.
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Objection to Reading of Papers" if 'Objections to reading of papers' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Objection to Reading of Papers" if 'Objections to reading papers' in x else x)

# XXXII
RulesReformSheet.loc[RulesReformSheet["Rule"] == "XXII. OF PETITIONS, MEMORIALS, BILLS, AND RESOLUTIONS", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XXII. OF PETITIONS, MEMORIALS, BILLS, AND RESOLUTIONS", "Title"].apply(lambda x: x.capitalize())

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Persons and officials admitted to the floor during sessions of the House" if 'Persons and Officials Admitted to the Floor During Sessions of the House' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Persons and officials admitted to the floor during sessions of the House" if 'Persons and officials admitted to the floor during sessions of the house' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Persons and officials admitted to the floor during sessions of the House" if 'Person and officials admitted to the floor during sessions of the House' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Admission to the floor when the House is not sitting" if 'Admission To the Floor When the House is Not Sitting' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Former Members and officers" if 'Former Members and Officers' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Former Members and officers" if 'Former members and officers' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Members' staff" if "Members' Staff" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Members' staff" if "Member's staff" in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Introduction and reference of petitions, memorials, and private bills" if 'Introduction and reference of petitions, memorials and private bills' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Introduction of bills, resolutions, or memorials by request" if 'Introduction of bills, resolutions, or memorials by request ' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Introduction of bills, resolutions, or memorials by request" if 'Introduction of bill, resolutions or memorials by request' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Introduction of bills, resolutions, or memorials by request" if 'Introduction of bills, resolutions or memorials by request' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Introduction, reference, and change of reference of public bills, memorials, and resolutions" if 'Introduction, reference and change of reference of public bill, memorials and resolutions' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Introduction, reference, and change of reference of public bills, memorials, and resolutions" if 'Introduction, reference and change of reference of public bills, memorials and resolutions' in x else x)


# XXXIII
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The various galleries and admission thereto" if 'The Various Galleries and Admission Thereto' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The various galleries and admission thereto" if 'The various gallerries and admission thereto' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The various galleries and admission thereto" if 'The various galleried and admission thereto' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The various galleries and admission thereto" if 'The Various galleries and admission thereto' in x else x)

### --- COMMITTEES OF THE WHOLE HOUSE XXIII.

RulesReformSheet.loc[RulesReformSheet["Rule"] == "XXIII. OF COMMITTEES OF THE WHOLE HOUSE", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XXIII. OF COMMITTEES OF THE WHOLE HOUSE", "Title"].apply(lambda x: x.capitalize())
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Order of business in committee of the whole" if 'Order of business in committe of the whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Order of business in committee of the whole" if 'Order if business in committee of the whole' in x else x)



RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Subjects requiring consideration in committee of the whole" if 'Subjects requireing consideration in committee of the whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Subjects requiring consideration in committee of the whole" if 'Subjects requiring consideration in Committee of the Whole' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Closing the five-minute debate in committee of the whole" if 'Closing the five-minute debate in committe of the whole' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Selection of chairman of committee of the whole; and his power to preserve order" if 'Selection of chairman of the committee of the whole; and his power to preserve order' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "General debate and amendment under the five-minute rule in committee of the whole" if 'Geberal debate and amendment under the five-minute rule in committee of the whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "General debate and amendment under the five-minute rule in committee of the whole" if 'General debate and amendment under the five-minute rule in committee of thw whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "General debate and amendment under the five-minute rule in committee of the whole" if 'General debate and amendment under the five-minute rule in comittee of the whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "General debate and amendment under the five-minute rule in committee of the whole" if 'General debate and amendment under the five-minute rule in committe of the whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "General debate and amendment under the five-minute rule in committee of the whole" if 'General debate and amendments under the five-minute rule in committee of the whole' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Order of business in committee of the whole" if 'Orrder of business in committee of the whole' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Closing the five-minute debate in committee of the whole" if 'Closing the five-minute debate in commitee of the whole' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Application of rules of the house to the committee of the whole" if 'Application of rules of the house to the commitee of the whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Application of rules of the house to the committee of the whole" if 'Application of rules of the House to the Committee of the Whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Application of rules of the house to the committee of the whole" if 'Application of rule of the house to the committee of the whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Application of rules of the house to the committee of the whole" if 'Application of rules of the house t the committee of the whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Application of rules of the house to the committee of the whole" if 'Application of the rules of the house to the committee of the whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Application of rules of the house to the committee of the whole" if 'Application of rules of the house to the committee of th whole' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Subjects requiring consideration in committee of the whole" if 'Subject requiring consideration in committee of the whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Subjects requiring consideration in committee of the whole" if 'Subjects requirinf consideration in committee of the whole' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Selection of chairman of committee of the whole; and his power to preserve order" if 'Selection of chairman of committee of the whole; and his power to preserve' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Selection of Chairman Committee of the Whole; and his power to preserve order" if 'Selection of Chairman of Committee of the Whole; and his power to preserve order' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Speaker's declaration into committee of the whole pursuant to special order" if 'Speakers declaration into committee of the whole persuant to special order' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The motion to strike out the enacting words of the bill" if 'The motion to strike out the enecting words of the bill' in x else x)


# XXXIV ORDER OF BUSINESS

RulesReformSheet.loc[RulesReformSheet["Rule"] == "XXIV. ORDER OF BUSINESS ", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XXIV. ORDER OF BUSINESS", "Title"].apply(lambda x: x.capitalize())
RulesReformSheet.loc[RulesReformSheet["Rule"] == "XXIV. ORDER OF BUSINESS", "Title"] = RulesReformSheet.loc[RulesReformSheet["Rule"] == "XXIV. ORDER OF BUSINESS", "Title"].apply(lambda x: x.capitalize())

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Interruption of the call of committees by motion to go into committee of the whole house on the state of the union" if 'Interuption of the call of committees by motion to go into committee of the whole house on the state of the union' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Interruption of the call of committees by motion to go into committee of the whole house on the state of the union" if 'Interruption of call of committees by motion to go into committee of the whole house on the state of the union' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Interruption of the call of committees by motion to go into committee of the whole house on the state of the union" if 'Interruption of the call of committees by motion to go into committe of the whole house on the state of the union' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Interruption of the call of committees by motion to go into committee of the whole house on the state of the union" if 'Interruption of the call of committee by motion to go into committee of the whole house on the state of the union' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Interruption of the regular order on tuesdays for consideration of the private calendar" if 'Interuption of the regular order on tuesday for consideration of the private calendar' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Interruption of the regular order on tuesdays for consideration of the private calendar" if 'Interruption of regular order on tuesdays for consideration of the private calendar' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Interruption of the regular order on tuesdays for consideration of the private calendar" if 'Interruption of the regular order on tuesday for consideration of the private calendar' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Interruption of the regular order on tuesdays for consideration of the private calendar" if 'Interuption of the regular order on tuesdays for consideration of the private calendar' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "District of columbia" if 'Distict of columbia' in x else x)



# Something else
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Reporters of debates and committee stenographers" if 'Reporters of Debates and Committee Stenographers' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Reporters of debates and committee stenographers" if 'Reporters of debates and committee stenographer' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Reporters of debates and committee stenographers" if 'Reporters of debate and committee stenographers' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Reporters of debates and committee stenographers" if 'Reporters of dbates and committee stenographers' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Reporters of debates and committee stenographers" if 'Reporters of debates and committee  stenographers' in x else x)


RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Unofficial reporters in the press gallery and on the floor" if 'Unofficial Reporters in the Press Gallery and on the Floor' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Unofficial reporters in the radio gallery and on the floor" if 'Unofficial Reporters in the Radio Gallery and on the Floor' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Unofficial reporters in the radio gallery and on the floor" if 'Unofficial reporters in the radio gallery and in the floor' in x else x)



# XXXV

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Fees of witnesses before the House or committees" if 'Fees of Witnesses Before the House or Committees' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Fees of witnesses before the House or committees" if 'Fees of witnesses before the house or committees' in x else x)


# XXXVI

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Duties of Clerk and committees as to custody of papers before committees" if 'Duties of clerk and committees as to custody of papers before committees' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Duties of Clerk and committees as to custody of papers before committees" if 'Duties of Clerk and Committees as to Custody of Papers Before Committees' in x else x)

# XXXVII

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Custody of papers in the files of the House" if 'Custody of Papers in the Files of the House' in x else x)

# XXXVIII
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Elections by ballot" if 'Elections by Ballot' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Requirement that reports of committee be in writing and be printed" if 'Requirement  that reports of committees be in writing and be printed' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Application of motion to reconsider to bills in committees" if 'Application of motion to reconsider to bill in committee' in x else x)

# Duties of the Members VIII

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Personal Interest" if 'Personal interest' in x else x)

# XII. RESIDENT COMMISSIONER AND DELEGATES. (Home Rule era)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Powers and Privileges of Resident Commissioner and Delegates as to committee service" if 'Powers and Privilege of Resident Commissioner and Delegates as to committees service' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Powers and Privileges of Resident Commissioner and Delegates as to committee service" if 'Power and Privileges of Resident Commissioner and Delegates as to committee service' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Powers and Privileges of Resident Commissioner and Delegates as to committee service" if 'Powers and Privileges of Resident Commissioner as to committee service' in x else x)

# XL. Eexecutive Comunicatons

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Reception and reference of executive communication, including estimates" if 'Reception and reference of executive communications including estimates' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Reception and reference of executive communication, including estimates" if 'Reception and reference of executive communications, including estimates' in x else x)

# XLI. QUALIFICATIONS OF OFFICERS AND EMPLOYEES

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Officers and employees not to be agents of claims" if 'Officers and employees no to be agents of claims' in x else x)

# XLII. GENERAL PROVISIONS
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Relations of Jefferson's Manual and Legislative Reorganization Act of 1946 to the rules of the House" if "Relations of Jefferson's Manual ang Legislative Reorganization Act of 1946 to the rules of the House" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Relations of Jefferson's Manual and Legislative Reorganization Act of 1946 to the rules of the House" if "Relation of Jefferson's Manual and Legislative Reorganization Act of 1946 to the rules of the House" in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Relations of Jefferson's Manual and Legislative Reorganization Act of 1946 to the rules of the House" if "Relations of Jefferson's Manual and Legislative Reorganization Act of 1946 to the Rule of the House" in x else x)

# XLIV. FINANCIAL DISCLOSURE
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Financial report disclosing certain financial interests" if 'Financial report disclosing certain financial interest' in x else x)

# XXX. Reading of papers
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Objection to Reading of Papers" if 'Objection to reading of papers' in x else x)

# XXXV. PAY OF WITNESSES
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Fees of witnesses before the House or committees" if 'Fees of witnesses before the House or committees' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Fees of witnesses before the House or committees" if 'Fees of witnesses before the House of Committees' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Fees of witnesses before the House or committees" if 'Fees of witnesses before the House of committees' in x else x)

# XXXVI. PAPERS

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Duties of Clerk and committees as to custody of papers before committees" if 'Duties of clerk and committees as to custody papers before committees' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Duties of Clerk and committees as to custody of papers before committees" if 'Duties of Clerk and commitee as to custody of papers before committees' in x else x)

# XXXVI. WITHDRAWAL OF PAPERS

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Custody of papers in the files of the House" if 'Custody of papers in the files of the house' in x else x)


# XXXVIII. BALLOT

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Elections by ballot" if 'Election by ballot' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Elections by ballot" if 'Election by Ballot' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Elections by ballot" if 'Election day ballot' in x else x)

# XXIX. SECRET SESSION

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Secret session of the House" if 'Secret session od the House' in x else x)


# XXV. PRIORITY OF BUSINESS
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Decision of questions as to priority of business without debate" if 'Decision  of Questions as to Priority of Business Without Debate' in x else x)


# XX. OF AMENDMENTS OF THE SENATE

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Consideration of senate amendments in committee of the whole; motion for conference" if 'Consideration of senate amendments in committee of the whole' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Consideration of senate amendments in committee of the whole; motion for conference" if 'Considertaion of senate amendments in committee of the whole' in x else x)

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Conferees may not agree to certain senate amendments" if 'Conferees may not agree to certain in senate amendments' in x else x)

# VI VI. DUTIES OF THE POSTMASTER

RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The Postmaster superintends the House post office" if 'The Postmaster superintends the House post-office' in x else x)
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "The Postmaster superintends the House post office" if 'The Postmaster super intends the House post-office' in x else x)

#### XXXI. Hall
RulesReformSheet["Title"] = RulesReformSheet["Title"].apply(lambda x: "Use of the Hall of the House" if 'Use of the hall of the house' in x else x)


# This code combines the rules for a given congress to generate the full rule

grouped_Rules = RulesReformSheet.groupby(['Rule', 'Congress'])['Text'].agg(''.join).reset_index()
grouped_Rules["Title"] = grouped_Rules["Rule"]
grouped_Rules = grouped_Rules[["Rule", "Title", "Text", "Congress"]]
grouped_Rules["Title"] = grouped_Rules["Title"].apply(lambda x: "Full Rule for: " + x)
grouped_Rules["Link"] = ""
combined_df = pd.concat([RulesReformSheet, grouped_Rules])


nested_rules = RulesReformSheet.drop_duplicates(subset=['Rule', "Title"])
print(nested_rules)
nested_rules = dict(nested_rules.groupby('Rule')['Title'].apply(list))
print("---Nested Rules---")
print(nested_rules)

# print(combined_df["Rule"].unique().tolist())
combined_df.to_csv("Rules Reform Scraping - Combined - Older.csv")
