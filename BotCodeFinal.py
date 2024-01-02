import time
import openai
from openai import OpenAI

client = OpenAI(api_key="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")

# Creating the assistant
assistant = client.beta.assistants.create(
    name="Guru GPT",
    instructions="You are a personal coach who works based on the ideas and teachings of Andrew Huberman and Jordan Peterson. Help the users to tackle their daily life issues by guiding them with actionable tasks.",
    model="gpt-3.5-turbo",
)

# Create thread
thread = client.beta.threads.create()

# Get user input
user_input = input("Hi I am Guru GPT, your personal coach.How can I help you today? : ")

# Create user message
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=user_input
)

# Create run
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    #instructions="Please address the user as Jane Doe. The user has a premium account.",
)

print("This is a complex question and would require deep thought")
time.sleep(3)
while True:
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

    if run.status == "completed":
        print("Okay, so this is what I would recommend.")
        messages = client.beta.threads.messages.list(thread_id=thread.id)

        #print("Messages: ")
        for message in messages:
            assert message.content[0].type == "text"
            #print({"role": message.role, "message": message.content[0].text.value})
            print(message.content[0].text.value)

        client.beta.assistants.delete(assistant.id)

        break
    else:
        print("Let me ponder about it for a moment so that I can give you a proper answer...")
        time.sleep(5)
