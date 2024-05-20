from bs4 import BeautifulSoup
import pandas as pd

with open("TestContent/content.html","r", encoding="utf-8") as f:
    htmlDoc = f.read()

soup = BeautifulSoup(htmlDoc,"html.parser")
ulContent = soup.find_all("ul", class_ = None)[8]
getRoles = ulContent.find_all("a")
getImage = ulContent.find_all("img", class_ = "lazyload")
getRoleDetails = ulContent.find_all("li")

rolesData = [roles.text.strip() for roles in getRoles if roles.text.strip() != ""]
roleDetailsData = [roleDetails.text.strip().replace("\n", " ").replace("\t", "") for roleDetails in getRoleDetails]
iconLins = [icons.get("data-src") for icons in getImage]

rolesTable = {
    "Roles": rolesData,
    "Roles Description": roleDetailsData,
    "Roles Image Links": iconLins
}

df = pd.DataFrame(rolesTable)
df.to_csv(r'D:\Valorant Dataset\Data\Roles.csv',index=False)