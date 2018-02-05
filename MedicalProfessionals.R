data = read.csv('/Users/amandazulas/Downloads/Physician_Compare/Physician_Compare_National_Downloadable_File.csv')

length(unique(data$NPI))

length(unique(data$NPI[data$Gender=='M']))/length(unique(data$NPI[data$Gender=='F']))

for (c in unique(data$Credential)){
  print (c)
  print (length(unique(data$NPI[data$Gender=='F'&data$Credential==c]))/length(unique(data$NPI[data$Gender=='M'&data$Credential==c])))
}

facilityData = read.csv('/Users/amandazulas/Downloads/Physician_Compare/Physician_Compare_2015_Group_Public_Reporting_-_Patient_Experience.csv')

lessThanTen = 0
for (s in unique(facilityData$State)){
  print (s)
  numberOfFacilities = length(unique(facilityData$Organization.legal.name.or..doing.business.as..name[facilityData$State==s]))
  if (numberOfFacilities < 10) {
    lessThanTen=lessThanTen+1
  }
}
print(lessThanTen)

