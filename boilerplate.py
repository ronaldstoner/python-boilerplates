#!/usr/bin/env python3
import argparse
import asyncio
import json
import time
import websockets
from tqdm import tqdm
from colorama import Fore, Style

# Define command line arguments using argparse
parser = argparse.ArgumentParser(description='Example script')
parser.add_argument('-m', '--mock', action='store_true', help='Use mock data instead of making a websocket call')
parser.add_argument('-a', '--age', type=int, required=True, help='Your age')

# Parse command line arguments
args = parser.parse_args()

def tqdm_bar():
    # Use tqdm to display a progress bar
    for i in tqdm(range(100)):
        time.sleep(0.01)

def print_age():
    # Use colorama to change text color
    print(Fore.GREEN + 'You are ' + str(args.age) + ' years old.' + Style.RESET_ALL)

async def ws_test():
    # Use websockets to send and receive messages
    async def get_response(websocket):
        response = await websocket.recv()
        response_data = json.loads(response)
        print(Fore.GREEN + 'Response: ' + str(response_data) + Style.RESET_ALL)

    if args.mock:
        mock_response = {'mocked': True, 'age': args.age}
        print(Fore.YELLOW + 'Using mock data: ' + str(mock_response) + Style.RESET_ALL)
    else:
        try:
            async with websockets.connect('ws://localhost:8765') as websocket:
                await websocket.send(json.dumps({'age': args.age}))
                await get_response(websocket)
        except websockets.exceptions.ConnectionClosedError as e:
            print(Fore.RED + 'Error: ' + str(e) + Style.RESET_ALL)

if __name__ == '__main__':
    tqdm_bar()
    print_age()
    asyncio.run(ws_test())
