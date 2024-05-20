from bs4 import BeautifulSoup
import requests
import pandas as pd

with open("TestContent/abilitiesContent.html","r", encoding="utf-8") as f:
    htmlDoc = f.read()


soup = BeautifulSoup(htmlDoc, 'html5lib')

getUl = soup.find_all('ul', attrs = {'id' : None, 'class' : None})
# print(getUl)

agentNames = [agents.text.strip() for agents in getUl[0]]
# print(agentNames)

agentAbilities = [abilities.get_text(strip=True) for abilities in getUl[2:]]
# print(agentAbilities)


# Initialize empty lists to store agent data
agent_data = []


# Iterating to insert data
for name, abilities in zip(agentNames, agentAbilities):
    # Create a dictionary for each agent
    agent_dict = {
        'Agent Name': name,
        'Agent Abilities': abilities  # Join abilities
    }
    # Appending dictionary to the list
    agent_data.append(agent_dict)

# Creating DataFrame
df = pd.DataFrame(agent_data)

df.to_csv(r'D:\Valorant Dataset\Data\AgentAbilities.csv',index=False)