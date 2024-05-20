import requests

def saveContent(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

def saveContentForAbilities(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)


saveContent("https://valorant.fandom.com/wiki/Agents","TestContent/content.html") 
saveContentForAbilities("https://beebom.com/valorant-characters-agents-abilities/","TestContent/abilitiesContent.html")
