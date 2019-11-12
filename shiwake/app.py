import openpyxl
from openpyxl.styles.alignment import Alignment
from openpyxl.styles.borders import Border,Side
from . import dicdic

dic = {1:'通信費',2:'交通費',3:'消耗品費',4:'普通預金',5:'未払い金',6:'売上',
       7:'預け金',8:'売掛金',9:'事業主貸',10:'事業主借'}

wb = openpyxl.load_workbook('hina.xlsx') # サーバー上のファイルの場所
st = wb.get_sheet_by_name('Sheet')
month = dicdic.ddd['month']
day = dicdic.ddd['day']
tekiyou_kari = []
tekiyou_kariri = dicdic.ddd['tekiyou_kari'].split()
for i in range(len(tekiyou_kariri)):
      tekiyou_kari.append(dic[int(tekiyou_kariri[i])])
tekiyou_kasi = []
tekiyou_kasisi = dicdic.ddd['tekiyou_kasi'].split()
for i in range(len(tekiyou_kasisi)):
      tekiyou_kasi.append(dic[int(tekiyou_kasisi[i])])
tekiyou_com = dicdic.ddd['tekiyou_com']
amount_kari = [dicdic.ddd['amount_kari']]
amount_kasi = [dicdic.ddd['amount_kasi']]


a = []
for i in list(st.columns)[0]:
      a.append(i.value)
for i in range(len(a)):
      if not isinstance(a[i],str) and not isinstance(a[i],int):
            a[i] = 0
            continue
      if not str(a[i]).isdecimal():
            a[i] = 0
            continue
      a[i] = int(a[i])
aaa = []
for i in list(st.columns)[1]:
      aaa.append(i.value)
for i in range(len(aaa)):
      if not isinstance(aaa[i],str) and not isinstance(aaa[i],int):
            aaa[i] = 0
            continue
      if not str(aaa[i]).isdecimal():
            aaa[i] = 0
            continue
      aaa[i] = int(aaa[i])
if int(month) in a:
      for i in range(len(a)):
            if int(month) == a[i]:
                  b = i
                  break
      for i in range(len(a)):
            if int(month) < a[i]:
                  c = i
                  break
      try:
            c
            for i in range(b,c):
                  if int(day) < aaa[i]:
                        for j in range(3):
                              st.insert_rows(i + 1)
                        d = i + 1
                        break
            try:
                  d
            except:
                  for i in range(3):
                        st.insert_rows(c + 1)
                        d = c + 1
      except:
            for i in range(b,len(a)):
                  if int(day) < aaa[i]:
                        for j in range(3):
                              st.insert_rows(i + 1)
                        d = i + 1
                        break
            try:
                  d
            except:
                  d = len(a) + 1

elif int(month) > max(a):
      d = st.max_row + 1

else:
      aa = a
      aa.append(int(month))
      aa = list(set(aa))
      e = aa[aa.index(int(month)) - 1]
      for i in range(len(a)):
            if e < a[i]:
                  f = i
                  break
      for i in range(3):
                  st.insert_rows(f + 1)
                  d = f + 1

st.column_dimensions['C'].width = 50
st['A' + str(d)] = month
st['A' + str(d)].alignment = Alignment(horizontal = 'right')
st['B' + str(d)] = day
st['B' + str(d)]
if len(tekiyou_kari) == 1 and len(tekiyou_kasi) == 1:
      st['C' + str(d)] = '(' + tekiyou_kari[0] + ')'
      st['C' + str(d)].alignment = Alignment(horizontal = 'left',
                                             vertical = 'center')
      st['C' + str(d + 1)] = '(' + tekiyou_kasi[0] + ')'
      st['C' + str(d + 1)].alignment = Alignment(horizontal = 'right',
                                             vertical = 'center')
      st['D' + str(d)] = tekiyou_kariri[0]
      st['D' + str(d + 1)] = tekiyou_kasisi[0]
      st['E' + str(d)] = '{:,d}'.format(amount_kari[0])
      st['E' + str(d)].alignment = Alignment(horizontal = 'right')
      st['F' + str(d + 1)] = '{:,d}'.format(amount_kasi[0])
      st['F' + str(d + 1)].alignment = Alignment(horizontal = 'right')
      st['C' + str(d + 2)] = tekiyou_com
      st['C' + str(d + 2)].alignment = Alignment(wrapText = True)
      side = Side(style = 'thin',color = '000000')
      border = Border(bottom=side)
      st['C' + str(d + 2)].border = border
elif len(tekiyou_kari) == 2 and len(tekiyou_kasi) == 1:
      st.insert_rows(d)
      st['C' + str(d + 1)] = '(' + tekiyou_kari[0] + ')'
      st['C' + str(d + 1)].alignment = Alignment(horizontal = 'left',
                                             vertical = 'center')
      st['C' + str(d + 2)] = '(' + tekiyou_kari[1] + ')'
      st['C' + str(d + 2)].alignment = Alignment(horizontal = 'left',
                                             vertical = 'center')
      st['C' + str(d)] = '諸口　　　　　　' + '(' + tekiyou_kasi[0] + ')'
      st['C' + str(d)].alignment = Alignment(horizontal = 'right',
                                             vertical = 'center')
      st['D' + str(d + 1)] = tekiyou_kariri[0]
      st['D' + str(d + 2)] = tekiyou_kariri[1]
      st['D' + str(d)] = tekiyou_kasisi[0]
      st['E' + str(d + 1)] = '{:,d}'.format(amount_kari[0])
      st['E' + str(d + 1)].alignment = Alignment(horizontal = 'right')
      st['E' + str(d + 2)] = '{:,d}'.format(amount_kari[1])
      st['E' + str(d + 2)].alignment = Alignment(horizontal = 'right')
      st['F' + str(d)] = '{:,d}'.format(amount_kasi[0])
      st['F' + str(d)].alignment = Alignment(horizontal = 'right')
      st['C' + str(d + 3)] = tekiyou_com
      st['C' + str(d + 3)].alignment = Alignment(wrapText = True)
      side = Side(style = 'thin',color = '000000')
      border = Border(bottom=side)
      st['C' + str(d + 3)].border = border

wb.save('hina.xlsx')
