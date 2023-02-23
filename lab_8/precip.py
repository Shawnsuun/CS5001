def get_avgs(list_num):
	"""
    get the average number of a number list

    Keyword arguments:

    list_num -- a list with numbers

    """
    #return 0 when list_num is empty,
	if len(list_num) == 0: 
		return 0

	#type checking of argument, raise an error if type is not list
	if not isinstance (list_num, list):
		raise TypeError("Type error occurred in get_avg, argument is not a list")   

	#calculate average value
	total = 0.0
	for i in range(len(list_num)):
		total += float(list_num[i])
	return total / len(list_num)


def	print_avgs(rain_data, snow_data, city, starting_year, out_file):
	"""
    type checking of five arguments, raise an error if type is not right

    Keyword arguments:

    rain_data -- a list of lists, inner lists contain the rain data of a single year, 
    	outer list contain the lists of rain data in different years.

	snow_data -- a list of lists, inner lists contain the snow data of a single year, 
		outer list contain the lists of snow data in different years.

	city -- a string of city name

	starting_year -- an integer of starting year, range of 2010~2021

	out_file -- a string of output filename

    """

    #arguments type checking, raise a type error when the type of argument is not correct
	if not isinstance (rain_data, list):
		raise TypeError("First argument in print_avgs is not a list")
	if not isinstance (snow_data, list):
		raise TypeError("Second argument in print_avgs is not a list")
	if not isinstance (city, str):
		raise TypeError("Third argument in print_avgs is not a string")
	if not isinstance (starting_year, int):
		raise TypeError("Fourth argument in print_avgs is not an integer")
	if not isinstance (out_file, str):
		raise TypeError("Fifth argument in print_avgs is not a string")
	
	#starting_year value checking, raise an error if value is not between 2010 and 2021
	if starting_year > 2021 or starting_year < 2010:
		raise ValueError("Please enter a year between 2010~2021") 

	#index of the data list based on the starting year
	#add rainfall data
	index = starting_year - 2010
	content = ""
	content += f"{city.upper()} Average Rainfall:\n"
	for year_data in rain_data[index:]:
		avg_prcp = get_avgs(year_data)
		year = index + 2010
		content += f"{year}: {format(avg_prcp, '.3f')}\n"
		index += 1

	#add snow data	
	index = starting_year - 2010
	content += f"{city.upper()} Average SnowFall:\n"
	for year_data in snow_data[index:]:
		avg_snow = get_avgs(year_data)
		year = index + 2010
		content += f"{year}: {format(avg_snow, '.3f')}\n"
		index += 1	

	#write extracted content in the output file
	file = open(out_file, "w")
	file.write(content)
	print (f"Data successfully write to {out_file}")


def main():
	"""
    main function to read a csv file and extract rain and snow information based on user input

    """

    #keep main function running when error occur
	running = True
	while running:
		#protect the body of main function from different kinds of errors
		try:
			file_name = input("Please enter filename:")
			if not file_name.endswith('.csv'):
				raise ValueError("The file should end with '.csv'")
			file = open(file_name, "r")

			#initalize the rain and snow data list, line number and empty data number
			rain_data = [[],[],[],[],[],[],[],[],[],[],[],[]]
			snow_data = [[],[],[],[],[],[],[],[],[],[],[],[]]
			line_num = 0
			empty_data = 0

			#get user input of city/area name and starting year
			city = input("Please enter city/area(YARMOUTH, CUMBERLAND, PORTLAND...):")
			starting_year = input("Please enter starting year:")

			#parse user input starting_year, raise a type error if cannot parse into integer
			try:
				starting_year = int(starting_year)
			except ValueError:
				print("Not a valid year number.")
				continue

			#parse the content of file and get location, date, rainfall, and snowfall data
			location_found = False
			for line in file:
				#skip the first line
				line_num += 1
				if line_num > 1:
					info = line.split(",")
					location = info[1].strip('"')
					date = info[3]
					prcp = info[9]
					snow = info[10]
					
					if location.startswith(city.upper()):
						location_found = True
						#pre treatment to the raw data from the csv file, make sure they are available for functions
						#catch value error when empty data appears, record appearing times
						try:
							date = int(info[3][1:5])
							prcp = float(info[9].strip('"'))
							rain_data[date - 2010].append(prcp)
							snow = float(info[10].strip('"'))
							snow_data[date - 2010].append(snow)
						except ValueError:
							empty_data += 1	

			if location_found:
				print_avgs(rain_data, snow_data, city, starting_year, f"{city}.txt")
				print (f"{line_num} lines data has been read.")		
				print (f"{empty_data} empty data has been skipped.")
			#raise a value error if the user input area is not found
			else:
				raise ValueError("No data for this area.")
		
		#protect the body of main function from different kinds of errors
		except FileNotFoundError:
			print ("File not exist.")
		except TypeError as ex:
			print (ex)
		except ValueError as ex:
			print (ex)

#call main function
main()