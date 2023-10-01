from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

load_dotenv()

def generate_pet_name(breed, pet_color):
    llm = OpenAI(temperature=0.7)

    prompt_template = PromptTemplate(
        input_variables=['breed', 'pet_color'],
        template='I am an owner of {breed} kennel. Suggest me five cool names for my {pet_color}-colored puppies.'
    )

    # name = llm()
    name_chain = LLMChain(llm=llm, prompt=prompt_template, output_key='pet_names')

    response = name_chain({
        'breed': breed,
        'pet_color': pet_color,
    })

    return response 

def langchain_agent():
    llm = OpenAI(temperature=0.5)
    tools = load_tools(['wikipedia', 'llm-math'], llm=llm)
    agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    result = agent.run(
        'What is the average age of a dog? Multiply the age by 3',
    )
    print(result)

if __name__ == '__main__':
    # load_dotenv()
    # print(generate_pet_name("chow-chow"))
    langchain_agent()