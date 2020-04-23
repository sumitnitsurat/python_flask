import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('SmartFit.json', scope)
client = gspread.authorize(creds)

def fetchExcelFoodList():   
    sheet = client.open('foodlist').sheet1
    foodlist = sheet.get_all_records()
    return foodlist

