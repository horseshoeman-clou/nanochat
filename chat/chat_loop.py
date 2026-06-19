from model.llm_model import get_response
from utils.storage import save_chat,load_chat


def handle_command(command,history):
	if command=="/help":
		return"""
	Available commands:
	/help - Show available commands
	/exit - Exit NanoChat
	/history - Show chat history
	/save - Save chat history
	/clear - CLear saved history
	/load - Load saved history"""

	elif command=="/exit":
		return "EXIT_COMMAND"

	elif command=="/history":
		history_text="*** Chat History ***\n"
		if not history:
			history_text+="No conversation history yet. Type something to start chatting\n"

		for speaker,message in history:
			history_text+= f"{speaker}: {message}\n"

		return history_text

	elif command=='/clear':
			return 'CLEAR_HISTORY'

	elif command=='/save':
			return 'SAVE_HISTORY'

	elif command=='/load':
			return 'LOAD_HISTORY'

	else:
		return f"""
	No command called {command}.
	Type /help to see available commands.
	"""

def start_chat():

	history=[]

	print("""
	Welcome to NanoChat!
	Type /help for available commands.\n""")

	while True:
		user_input=input("You: ")

		if user_input.lower().startswith('/'):
			commandResponse=handle_command(user_input.lower(),history)
			if commandResponse=="EXIT_COMMAND":
				break

			elif commandResponse=='CLEAR_HISTORY':
				history.clear()
				print("Cleared history.")
				continue

			elif commandResponse=='SAVE_HISTORY':
				result=save_chat(history)

				if result:
					print("History saved successfully")
				else:
					print("Failed to save history")
				continue

			elif commandResponse=='LOAD_HISTORY':

				loaded_history=load_chat()

				if loaded_history is not None:
					history=loaded_history
					print("History loaded successfully.")

					for speaker,message in history:
						print(f"{speaker}:{message}")

				else:
					print("No saved history found.")
				continue

			print(commandResponse)
			continue
		history.append(("You",user_input))
		response=get_response(user_input)

		history.append(("Bot",response))
		print(f"Bot: {response}")

