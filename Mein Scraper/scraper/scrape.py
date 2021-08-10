def get_kurslink(html):
    kurslink = None
    if html.find("a", class_="coursebox odd first"):
        kurslink = html.find("a", class_="aalink").get('href')
    elif html.find("div", class_="coursebox clearfix odd first"):
        kurslink = html.find("div", class_="coursebox clearfix odd first").get('data-courseid')
    elif html.find("div", class_="coursebox clearfix odd first last"):
        kurslink = html.find("div", class_="coursebox clearfix odd first last").get('data-courseid')
    elif html.find("div", class_="coursebox clearfix event"):
        kurslink = html.find("div", class_="coursebox clearfix even").get('data-courseid')
    elif html.find("div", class_="coursebox clearfix even last"):
        kurslink = html.find("div", class_="coursebox clearfix even last").get('data-courseid')
    return kurslink
