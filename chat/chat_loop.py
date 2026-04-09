from model.dummy_model import get_response

def start_chat():
	print("NanoChat started. Type 'exit' to quit.\n")

	while True:
		user_input=input("You: ")

		if user_input.lower() =="exit":
			print("Exiting NanoChat")
			break

		response=get_response(user_input)
		print(f"Bot: {response}")

