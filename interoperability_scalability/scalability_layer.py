import asyncio
from aiohttp import ClientSession

class ScalabilityLayer:
    def __init__(self, nodes):
        self.nodes = nodes
        self.client_sessions = {}

    async def create_client_sessions(self):
        for node in self.nodes:
            self.client_sessions[node] = ClientSession()

    async def send_request(self, node, request):
        async with self.client_sessions[node] as session:
            async with session.post(f"http://{node}.com/api", json=request) as response:
                return await response.json()

    async def receive_response(self, node):
        async with self.client_sessions[node] as session:
            async with session.get(f"http://{node}.com/api") as response:
                return await response.json()

if __name__ == "__main__":
    nodes = ["Node 1", "Node 2", "Node 3"]
    scalability_layer = ScalabilityLayer(nodes)
    asyncio.run(scalability_layer.create_client_sessions())

    # Send a request to Node 1
    request = {"amount": 100, "currency": "USD"}
    response = asyncio.run(scalability_layer.send_request("Node 1", request))
    print("Response:", response)

    # Receive a response from Node 2
    response = asyncio.run(scalability_layer.receive_response("Node 2"))
    print("Response:", response)
