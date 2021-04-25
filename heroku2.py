import gspread
from oauth2client.client import GoogleCredentials as GC
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from datetime import datetime
import pandas as pd
#gc = gspread.authorize(GC.get_application_default())
from oauth2client.service_account import ServiceAccountCredentials
from os import environ
from flask import Flask, request, abort
#'O:\\downloads-nov-2018\\python-self-programs\\akarthick-sheets-api.json'

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(environ["GOOGLE_SHEETS_CREDS_JSON"] , scope)
def retrievesheet():
     gc = gspread.authorize(credentials)
     master_sh=gc.open_by_key("1JTJlCdD1k96WUxkxuBq7OU7btBZqKxny9x8p9lo5IU0")
     master_worksheet = master_sh.worksheet("Sheet2")
     dfkeys = pd.DataFrame(master_worksheet.get_all_values()[1:11])
     print(dfkeys.columns)


app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    retrievesheet()
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    else:
        abort(400)
#57e0107c5767cc545a3e6d9480cbf411f57fe48a31cabe06f2bbb5250869
if __name__ == '__main__':
    app.run()
