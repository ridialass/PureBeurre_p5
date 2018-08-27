import json

class Agent:

    def __init__(self, **agent_attributes):
        for attr_name, attr_value in agent_attributes.items():
            #print(attr_name)
            setattr(self, attr_name, attr_value)

for agent_attribute in json.load(open("agents-100k.json")):
    agent = Agent(**agent_attribute)
    print(agent.age, agent.agreeableness, agent.conscientiousness, agent.country_name)
