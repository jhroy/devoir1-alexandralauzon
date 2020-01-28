montrealcampus = "http://montrealcampus.ca?p="
n=0
for url in range(20000,30151):
    web = montrealcampus + str(url)
    n += 1
    print (n,web)
