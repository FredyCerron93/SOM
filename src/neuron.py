import numpy as np

from distance import select_closest

def generate_network(size):

    return np.random.rand(size, 2)

def get_neighborhood(center, radix, domain):



    if radix < 1:
        radix = 1


    deltas = np.absolute(center - np.arange(domain))
    distances = np.minimum(deltas, domain - deltas)


    return np.exp(-(distances*distances) / (2*(radix*radix)))

def get_route(cities, network):

    cities['winner'] = cities[['x', 'y']].apply(
        lambda c: select_closest(network, c),
        axis=1, raw=True)

    return cities.sort_values('winner').index
