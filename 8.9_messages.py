def show_messages(messages):
    for message in messages:
        msg = message.title()
        print(msg)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Message: {current_message.title()}")
        sent_messages.append(current_message)
    print(messages)
    print(sent_messages)

messages = ['hello', 'try again', 'good job', 'goodbye', 'you are wrong']
sent_messages = []

show_messages(messages)
send_messages(messages, sent_messages)