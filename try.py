# # import openai

# # openai.api_key = 'sk-proj-wUyed3Ao0Fvy9WVGwwaUT3BlbkFJqUZt1Jywu1so3wT73rMl'

# # completion = openai.ChatCompletion.create(
# #   model="gpt-3.5-turbo",
# #   messages=[
# #     {"role": "system", "content": "You are a helpful assistant."},
# #     {"role": "user", "content": "Hello!"}
# #   ]
# # )

# # print(completion.choices[0].message)


# # if needed, install and/or upgrade to the latest version of the OpenAI Python library
# %pip install --upgrade openai
# # import the OpenAI Python library for calling the OpenAI API
# from openai import OpenAI
# import os

# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>"))