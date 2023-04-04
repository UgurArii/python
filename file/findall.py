import re
print("\nFine-Tuning String Extraction\n")
mystr="From ossama.embarak@hct.ac.ae Sat Jun 5 08:14:16 2018" 
Extract = re.findall('\S+@\S+',mystr)
print(Extract)
E_xtracted = re.findall('^From.*? (\S+@\S+)', mystr)
print(E_xtracted)
print(E_xtracted[0])

CoursesData = """101 COM Computers
                                 205 MAT  Mathematics
                                 189 ENG  English"""
Course_numbers = re.findall('[0-9]+',CoursesData)
print(Course_numbers)

Course_codes = re.findall('[A-Z]{3}',CoursesData)
print(Course_codes)
Course_names = re.findall('[A-Za-z]{4,}',CoursesData)
print(Course_names)

course_pattern = '([0-9]+)\s*([A-Z]{3})\s*[A-Za-z]{4,}'
print(re.findall(course_pattern, CoursesData))
print(re.findall('[a-zA-Z]+', CoursesData))
print(re.findall('[0-9]+', CoursesData))

print(re.findall('\d{4}', CoursesData))
print(re.findall('\d{2,4}', CoursesData))

