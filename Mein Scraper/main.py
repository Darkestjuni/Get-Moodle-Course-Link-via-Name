from scraper import scrape_page_metadata
import csv

#URL = input("Kursnamen oder -kürzel eingeben: ")
scrape = scrape_page_metadata

#data = pd.read_csv("Converter.csv", delimiter=";")

#if __name__ == '__main__':
#    scrape("https://ecampus.fh-potsdam.de/course/search.php?q="+data.Kursname[x]+"&areaids=core_course-course")

f1 = open ('Converter.csv', 'r')

if __name__ == '__main__':
    with open('Output.csv', 'w', encoding="UTF8", newline="") as f:
        writer = csv.writer(f, delimiter=';')
        with open ('Converter.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                links = scrape("https://ecampus.fh-potsdam.de/course/search.php?q="+str(row[0])+"&areaids=core_course-course")
                row[0] = f1.readline()
                writer.writerow(links)


#if __name__ == '__main__':
#    with open ('Converter.csv', 'r') as csvfile:
#        reader = csv.reader(csvfile, delimiter=';')
#        for row in reader:
#            links = scrape("https://ecampus.fh-potsdam.de/course/search.php?q="+row[0]+"&areaids=core_course-course")
