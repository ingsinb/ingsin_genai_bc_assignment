import pandas as pd
import json
from helper_functions import llm

# load the CSV file for recycling guide
filepath = './data/recycling_guide.csv'
data = pd.read_csv(filepath)

material_n_item = data[['material_category','product']].to_dict('records')

recycling_guide = {
    product.lower(): {'material_category': material_category, 'can_be_recycled': can_be_recycled, 'remarks': remarks}
    for material_category, product, can_be_recycled, remarks in zip(data['material_category'], data['product'], data['can_be_recycled'], data['remarks'])
}

def identify_material_n_product(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with customer service queries on whether a product is recyclable. \
    The customer service query will be enclosed in
    the pair of {delimiter}.

    Decide if the query is relevant or included to any specific item(s)
    in the Python dictionary below, which each key is a `material_category`
    and the value is an `product`'.

    If there are any relevant product(s) found, output the pair(s) of a) `product` the relevant product and b) the associated `material_category` into a
    list of dictionary object, where each string in the list is a relevant product
    and each course is a dictionary that contains two keys:
    1) material_category
    2) product

    {material_n_item}

    If no relevant product are found, output an empty list.

    Ensure your response contains only the list of dictionary objects or an empty list, \
    without any enclosing tags or delimiters.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    category_and_product_response_str = llm.get_completion_by_messages(messages)
    category_and_product_response_str = category_and_product_response_str.replace("'", "\"")
    category_and_product_response = json.loads(category_and_product_response_str)
    return category_and_product_response


def get_product_details(list_of_relevant_category_n_product: list[dict]):
    product_names_list = []
    for x in list_of_relevant_category_n_product:
        product_names_list.append(x.get('product'))

    list_of_product_details = []
    for product in product_names_list:
        list_of_product_details.append(recycling_guide.get(product.lower()))
    return list_of_product_details


def generate_response_based_on_course_details(user_message, product_details):
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the customer queries on recycling products.
    The customer query will be delimited with a pair {delimiter}.

    Step 1:{delimiter} If the user is asking about product, \
    understand the relevant product(s) from the following list.
    All available product shown in the json data below:
    {product_details}

    Step 2:{delimiter} Use the information about the product to \
    generate the answer for the customer's query.
    You must only rely on the facts or information in the product information.
    Your response should be as detail as possible and \
    include information that is useful for customer to better understand whether the product is recycable and what is the action that can be taken.

    Step 3:{delimiter}: Answer the customer in a friendly tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    the customers to make their decision.
    Complete with details such the actions to be taken.
    Use Neural Linguistic Programming to construct your response.
    Your response should be in following format:
    **Recyclable**:Yes/No\n
    **Material**:\n
    **Action that can be taken**:

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to customer>

    Make sure to include {delimiter} to separate every step.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_to_customer = llm.get_completion_by_messages(messages)
    response_to_customer = response_to_customer.split(delimiter)[-1]
    return response_to_customer


def process_user_message(user_input):
    delimiter = "```"

    # Process 1: If product are found, look them up
    material_n_product_name = identify_material_n_product(user_input)
    print("material_n_product : ", material_n_product_name)

    # Process 2: Get the prodct details
    course_details = get_product_details(material_n_product_name)

    # Process 3: Generate Response based on product details and whether it is recyclable
    reply = generate_response_based_on_course_details(user_input, course_details)

    # Process 4: Append the response to the list of all messages
    return reply

