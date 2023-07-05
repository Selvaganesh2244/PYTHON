years = ["January 2023","February 2024", "March 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
for i in range(len(years)):
    if years[i][-4:]!="2023":
        years[i]=years[i][:-4]+"2023"
print(years)
