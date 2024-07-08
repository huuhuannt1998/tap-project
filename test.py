import os
import subprocess
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

os.environ['OPENAI_API_KEY'] = "sk-proj-X8BlGEVno3zXYif1aWYnT3BlbkFJyEnquRT47mcRIYzG0xR1"

def list_smartthings_devices():
    result = subprocess.run(['smartthings', 'devices'], capture_output=True, text=True)
    return result.stdout

# List the devices
devices_output = list_smartthings_devices()

prompt_template = ChatPromptTemplate.from_template(
    """You are a smart home assistant. The devices are in {devices_output}. 
    Your task is generating Trigger-Action Rules. After that, convert it to Linear Temporal Logic (LTL). 
    Use this as an example: G (motion_sensor_active -> F switch_on_Aeotec_Outlet_1)
    """
)

output_parser = StrOutputParser()
model = ChatOpenAI(model="gpt-4o")

chain = (
    prompt_template 
    | model 
    | output_parser
)

# Preparing the input data for the chain
input_data = {
    "devices_output": devices_output,
    "user_input": "Turn off all switch when motion sensor is inactivate"
}

# Merging devices_output and user input into a single prompt string
final_input = f"The devices are in {input_data['devices_output']}. {input_data['user_input']}"

# Invoking the chain with the final input
result = chain.invoke(final_input)

print(result)



