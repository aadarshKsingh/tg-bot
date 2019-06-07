import os

from client import InteractiveTelegramClient

if __name__ == '__main__':
	SESSION = os.environ.get('TG_SESSION', 'bot')
	API_ID = os.environ.get('API_ID', '697645')
	API_HASH = os.environ.get('API_HASH', 'c704b8fb23f9364b5a14a07fe68fc625 ')
	client = InteractiveTelegramClient(SESSION, API_ID, API_HASH)
	client.run_until_disconnected()