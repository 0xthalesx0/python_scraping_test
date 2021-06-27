from User import User
import pandas as pd
import openpyxl


username = input('Username: ')
password = input('Password: ')
user = User(username, password)
html_result = user.access_website()

df = pd.read_html(html_result, match='Record high')[0]

df.drop(df.tail(1).index, inplace=True)

excel_name = input("Type the final file name: ")
df.to_excel(f'{excel_name}.xlsx')

print('Completed')
