from telethon.sync import TelegramClient
from config import api_id, api_hash, receiver, DELAY_BETWEEN_MESSAGES, DELAY_BETWEEN_LOOPS
from messages import messages
import time

client = TelegramClient('my_account', api_id, api_hash)
client.start()

print("\n\033[96m🚀 Started Nonstop Message Sender... Press CTRL+C to stop anytime.\033[0m\n")

try:
    while True:
        for i, msg in enumerate(messages, 1):
            try:
                client.send_message(receiver, msg)
                print(f"\033[92m✅ Sent message {i}: {msg}\033[0m")
                time.sleep(DELAY_BETWEEN_MESSAGES)
            except Exception as e:
                print(f"\033[91m❌ Error in message {i}: {e}\033[0m")

        print("\033[94m🔁 Restarting message loop after delay...\033[0m\n")
        time.sleep(DELAY_BETWEEN_LOOPS)

except KeyboardInterrupt:
    print("\n\033[91m🛑 Script stopped manually. Goodbye!\033[0m")

finally:
    client.disconnect()
