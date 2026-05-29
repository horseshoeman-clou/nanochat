def get_response(user_input):
	if 'hello' in user_input.lower():
		return "Hi there!"
	elif 'how are you' in user_input.lower():
		return "I am fine!"
	elif 'bye' in user_input.lower():
		return "Bye bye"

	return "I don't understand yet."
