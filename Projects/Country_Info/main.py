from countryinfo import CountryInfo

country_name = input("Please Enter Country Name: ")
country = CountryInfo(country_name)

print("Country:", country_name)
print("Capital:", country.capital())
print("Population:", country.population())
print("Area:", country.area(), "km2")
print("Currencies:", country.currencies())
print("Languages:", country.languages())
print("Borders:", country.borders())
print("Sub Region:", country.subregion())
