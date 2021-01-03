def airportConnections(airports, routes, startingAirport):
	airportGraph = createAirportGraph(airports, routes)
	unreachableAirportsNodes = getUnreachableAirportNodes(airportGraph, airports, startingAirport)
	markUnreachableConnections(airportGraph, unreachableAirportsNodes)
	return getMinNumberOfNewConnections(airportGraph, unreachableAirportsNodes)


# O(a + r) time | O(a + r) space, where a is the no of airports and r is the no of routes
def createAirportGraph(airports, routes):
	airportGraph = {}
	for airport in airports:
		airportGraph[airport] = AirportNode(airport)
	for route in routes:
		airport, connection = route
		airportGraph[airport].connections.append(connection)
	return airportGraph


# O(a + r) time | O(a) space
def getUnreachableAirportNodes(airportGraph, airports, startingAirport):
	visitedAirports = {}
	depthFirstTraverseAirports(airportGraph, startingAirport, visitedAirports)
	unreachableAirportNodes = []
	for airport in airports:
		if airport in visitedAirports:
			continue
		airportNode = airportGraph[airport]
		airportNode.isReachable = False
		unreachableAirportNodes.append(airport)
	return unreachableAirportNodes


def depthFirstTraverseAirports(airportGraph, airport, visitedAirports):
	if airport in visitedAirports:
		return 
	visitedAirports[airport] = True
	for connection in airportGraph[airport].connections:
		depthFirstTraverseAirports(airportGraph, connection, visitedAirports)


# O(a * (a + r)) time | O(a) space
def markUnreachableConnections(airportGraph, unreachableAirportNodes):
	for airportNode in unreachableAirportNodes:
		airport = airportNode.airport
		unreachableConnections = []
		depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, {})


def depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, visitedAirports):
	if airportGraph[airport].isReachable:
		return
	if airport in visitedAirports:
		return 
	visitedAirports[airport] = True
	unreachableConnections.append(airport)
	for connection in airportGraph[airport].connections:
		depthFirstAddUnreachableConnections(airportGraph, connection, unreachableConnections, visitedAirports)


# O(a * log(a) + a + r) time | O(1) space
def getMinNumberOfNewConnections(airportGraph, unreachableAirportsNodes):
	unreachableAirportNodes.sort(key = lambda: airport: len(airport.unreachableConnections), reverse=True)
	numberOfNewConnections = 0
	for airportNode in unreachableAirportNodes:
		if airportNode.isReachable:
			continue
		numberOfNewConnections += 1
		for connection in airportNode.unreachableConnections:
			airportGraph[connection].isReachable = True
	return numberOfNewConnections


class AirportNode:
	def __init__(self, airport):
		self.airport = airport
		self.connections = []
		self.isReachable = True
		self.unreachableConnections = []