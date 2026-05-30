from model.dummy_model import get_response

def handle_command(input):
	if input=="/help":
		return"""
	Available commands:
	/help - Show available commands
	/exit - Exit NanoChat
	"""
	elif input=="/exit":
		return "EXIT_COMMAND"

	else:
		return f"""
	No command called {input}.
	Type /help to see available commands.
	"""

def start_chat():
	print("""
	Welcome to NanoChat!
	Type /help for available commands.\n""")

	while True:
		user_input=input("You: ")

		if user_input.lower().startswith('/'):
			response=handle_command(user_input.lower())

			if response=="EXIT_COMMAND":
				break
			print(response)
			continue

		response=get_response(user_input)
		print(f"Bot: {response}")
