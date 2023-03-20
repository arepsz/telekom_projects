import json
import time
import sys

with open(sys.argv[1], "r") as read_file:
    data = json.load(read_file)

endpoints = data["end-points"]
switches = data["switches"]
allLinks = data["links"]
circuits = data["possible-circuits"]

duration = data["simulation"]["duration"]
demands = data["simulation"]["demands"]

foglaltLinkek = []
foglaltRoutok = []
sikeres = []

#link minta
# {
# "points": ["S3", "C"],
# "capacity": 10.0
# }

def foglalhato(demand):
    allPossibleRoutes = []
    for route in circuits:
        if route[0] == demand["end-points"][0] and route[-1] == demand["end-points"][1]:
            allPossibleRoutes.append(route)

    foglaltCounter = 0
    for route in allPossibleRoutes:
        foglaltAVonal = False
        linksInDemand = getLinks(route)
        for link in linksInDemand:
            if foglaltLink(link):
                foglaltAVonal = True
        if foglaltAVonal == False:
            foglal(route)
            sikeres.append(demand)
            return True
        else:
            foglaltCounter += 1
    if foglaltCounter == len(allPossibleRoutes):
        return False

def foglal(route):
    foglaltRoutok.append(route)
    linksInDemand = getLinks(route)
    for links in linksInDemand:
        cap = getLinksCap(links)
        points = links
        foglaltLinkek.append(
        {
            "points": points,
            "capacity": cap
        }
        )

def felszabadit(demand):
    #next(i for i in xrange(100000) if i == 1000)
    #[i for i in xrange(100000) if i == 1000][0]
    route = [route for route in foglaltRoutok if (route[0] == demand["end-points"][0] and route[-1] == demand["end-points"][1])][0]
    allLinksToFree = getLinks(route)
    for links in foglaltLinkek:
        if links["points"] in allLinksToFree:
            foglaltLinkek.remove(links)


def getLinksCap(link):
    cap = 0
    for links in allLinks:
        if links["points"] == link:
            cap = links["capacity"]
    return cap


def foglaltLink(link):
    for links in foglaltLinkek:
        cap = getLinksCap(link)
        if link == links["points"] and cap >= links["capacity"]:
            return True
    return False

def getLinks(route):
    links = []
    for i in range(0,len(route)-1):
        links.append([route[i],route[i+1]])
    return links

esemeny = 0
for idoPont in range(1,duration):
    for demand in demands:
        if demand["start-time"] == idoPont:
            if(foglalhato(demand)):
                esemeny += 1
                print(f'{esemeny}. igény foglalás: {demand["end-points"][0]}<->{demand["end-points"][1]} st:{idoPont} - sikeres')
            else:
                esemeny += 1
                print(f'{esemeny}. igény foglalás: {demand["end-points"][0]}<->{demand["end-points"][1]} st:{idoPont} - sikertelen')
        if demand["end-time"] == idoPont:
            esemeny += 1
            if demand in sikeres:
                felszabadit(demand)
                print(f'{esemeny}. igény felszabadítás: {demand["end-points"][0]}<->{demand["end-points"][1]} st:{idoPont}')
