import pandas as pd
import re


with open('PR_TF_20220101_20220822', 'r', encoding="utf-8") as f:

    text = f.read()

    # list to pandas dataframe

    ##################################
    # Step 1. to series              #
    ##################################

    WM_VIEWSUBJECTS = pd.Series(re.findall(r"(?<=WM_VIEWSUBJECTS:  請購單號:).*", text))
    # print(WM_VIEWSUBJECTS)

    WM_SHOWINFO_S = pd.Series(re.findall(r"(?<=WM_SHOWINFO_S:).*", text))
    # print(WM_SHOWINFO_S)

    JobStartedOS = pd.Series(re.findall(r"(?<=JobStartedOS:).*", text))
    # print(JobStartedOS)

    nREASON = pd.Series(re.findall(r"(?<=nREASON:).*|(?<=nNOTE:).*", text))
    # print(nREASON)

    ##################################
    # Step 2. to dataframe           #
    ##################################

    df = pd.concat([WM_VIEWSUBJECTS, WM_SHOWINFO_S, JobStartedOS, nREASON], axis=1)
    df.columns = ['WM_VIEWSUBJECTS', 'WM_SHOWINFO_S', 'JobStartedOS', 'nREASON']
    print(df.head())

    ##################################
    # Step 3. to csv file            #
    ##################################

    df.to_csv("PR_TF_20220101_20220822.csv", encoding='UTF-8-Sig', index=False)



