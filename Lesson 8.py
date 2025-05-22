import datetime
import os
import shutil

# d = datetime.datetime(2025, 5, 22, 16, 39)
# print(d)
#
# dn = datetime.datetime.now()
# print(dn)
#
# print(dn.date())
# print(dn.time())
#
# dd = datetime.date(2022, 2, 24)
# dt = datetime.time(4,31)
# d_war = datetime.datetime.combine(dd, dt)
# print(d_war)
#
# td = dn - d_war
# print(td)
#
# n = 4906
# td = datetime.timedelta(n)
# ddd = dn.date() - td
# print(ddd)
#
# print(ddd.weekday())
# print(ddd.isoweekday())

# path = "C:\\Users\\gololobov\\Downloads\\Logo\\Python.jpg"
# ct = os.path.getctime(path)
# print(ct)
# dct = datetime.datetime.fromtimestamp(ct)
# print(dct)
#
# print(dct.strftime("%d.%m.%Y, %H:%M, %A, %U"))
# print(dct.strftime("%d %B %Y"))

path = "C:\\Users\\gololobov\\Downloads\\Logo"
res_path = "C:\\Users\\gololobov\\Downloads\\Logo\\Test"


def catalog(path, res_path):
    path = os.path.normpath(path)
    res_path = os.path.normpath(res_path)
    for path, dirnames, filenames in os.walk(path):
        for file in filenames:
            date_file = os.path.getctime(f"{path}\\{file}")
            date_normal = datetime.datetime.fromtimestamp(date_file)
            str_date = date_normal.strftime("%d.%m.%Y")

            if not os.path.isdir(f"{res_path}\\{str_date}"):
                os.mkdir(f"{res_path}\\{str_date}")
            shutil.copy(f"{path}\\{file}", f"{res_path}\\{str_date}\\{file}")


catalog(path, res_path)
