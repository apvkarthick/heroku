import gspread
from oauth2client.client import GoogleCredentials as GC
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from datetime import datetime
import pandas as pd
#gc = gspread.authorize(GC.get_application_default())
from oauth2client.service_account import ServiceAccountCredentials
from os import environ
#'O:\\downloads-nov-2018\\python-self-programs\\akarthick-sheets-api.json'

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(environ["GOOGLE_SHEETS_CREDS_JSON"] , scope)
gc = gspread.authorize(credentials)
master_sh=gc.open_by_key("1JTJlCdD1k96WUxkxuBq7OU7btBZqKxny9x8p9lo5IU0")
master_worksheet = master_sh.worksheet("Sheet2")
dfkeys = pd.DataFrame(master_worksheet.get_all_values()[1:11])
print(dfkeys.columns)