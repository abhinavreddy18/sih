import pandas as pd
from openpyxl import load_workbook
writer=pd.ExcelWriter('D:\Abhinav\temp.xlsx',engine='openpyxl')
wb=writer.book
df1=pd.DataFrame([['a','b'],['c','d']],index=['row1','row2'],columns=['col1','col2'])
df1.to_excel(writer,index=False)
wb.save("D:\Abhinav\temp.xlsx")
             
