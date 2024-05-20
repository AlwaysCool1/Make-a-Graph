import matplotlib.pyplot as plt
import pandas

filename = "Attendance.csv"
absent_df = pandas.read_csv(filename)[["Date", "Absent"]]

average_absent_per_year = absent_df.groupby("Date")["Absent"].mean().reset_index()
# average_absent_per_year = absent_df.groupby("Date").sum().reset_index()
average_absent_per_year['Date'] = average_absent_per_year['Date'].astype(str)
average_absent_per_year['Date'] = average_absent_per_year['Date'].astype('datetime64[ns]')

average_absent_per_year.plot(kind="line", x = "Date", y = "Absent")
plt.show()


# df["year"] = df["Date"].str.slice(stop=4)
# print (df[["Absent", "year"]])