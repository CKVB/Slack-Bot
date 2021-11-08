def table_service(*args):
    text, client, current_channel = args
    if text.startswith("tables"):
        number = int(text.split()[-1])
        result = ""
        for i in range(1, 11):
            result += f"{number} X {i} = {number*i}\n"
        client.chat_postMessage(channel=current_channel, text=result)
