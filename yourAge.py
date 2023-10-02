import datetime
nowDate = datetime.date.today()
todayYear = nowDate.year
while True:
   Year=input("Enter your date of birth in the format of (YYYY-MM-DD) : ")
   if Year=="yo":
    break
   st = datetime.datetime.strptime(Year,"%Y-%m-%d")
   print("Your Age is:",todayYear-st.year,"Years")
print("By By")

