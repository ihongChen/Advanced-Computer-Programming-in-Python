# Activity 1.1

''' 1. Variable stars are stars whose level of brightness changes with time
    2. Each star belongs to one of the possible classes of variability 
        RRLyrae,
        Eclipsing Binaries,
        Mira,
        Long Period Variables,
        Cepheids, and Quasars
    3. Each star has a position in the sky represented by RA and DEC coordinates
    4. Stars are represented by an identifier(id) and contain a set of observations
    5. observation is a tuple : (time, magnitude and error)
        - Time value indicates the moment in which the telescope or the instrument does the observation.
        - The magnitude indicates the amount of brightness calculated in the observation 
        - The error corresponds to a range of uncertainty associated with the measurement
    6. Many fields compose the sky, and each field contains a huge amount of stars. 
    7. For each star, we need to know the average and the variance of the bright magnitudes.
    '''

def _avg(data):
    return sum(data)/len(data)

def _var(data):
    avg = _avg(data)
    dev = 0
    for e in data:
        dev += ((e) - avg)**2
    return dev / len(data)

class Star:

    def __init__(self, star_class, idx, RA_co, DEC_co, observations=None):
        self.star_class = star_class
        self.idx = idx
        self.RA_co = RA_co
        self.DEC_co = DEC_co
        if observations is None:
            observations = []        
        self.observations = observations
    
    def get_magnitudes(self):
        return [obv.magnitude for obv in self.observations]

    def get_avg_bright(self):
        return _avg(self.get_magnitudes())
    
    def get_var_bright(self):
        return _var(self.get_magnitudes())

    def add_observation(self, magnitude, timestamp, error):
        self.observations.append(Observation(magnitude, timestamp, error))


class Observation:
    
    def __init__(self, magnitude, timestamp, error):
        self.magnitude = magnitude
        self.timestamp = timestamp
        self.error = error


class Field:

    def __init__(self, stars=None):
        if stars is None:
            stars = []
        self.stars = stars
    
    def addStar(self, star):
        self.stars.append(star)


class Sky:

    def __init__(self, fields=None):
        if fields is None:
            fields =[]
        self.fields = fields

    def addField(self, field):
        self.fields.append(field)

if __name__=='__main__':
    sky = Sky()

    e0 = Star('RRLyee', 0, 0, 0, [
                                    Observation(2,1000,(1,3)),
                                    Observation(3,1000,(3,5)),
                                    Observation(4,1000,(3,5))
        ])

    
    e1 = Star('Eclipsing Binaries', 20, 30, 1, [
            Observation(2, 1000, (1, 3)),
            Observation(5, 1000, (2, 7)),
            Observation(6, 1000, (6, 9))])

    e2 = Star('Mira', 15,20,2, [
              Observation(7,1000,(1,3)),
              Observation(8,1000,(7,10)),
              Observation(9,1000,(1,30))
    ])

    field0 = Field()

    e3 = Star('Cepehids',50,15,3)
    e4 = Star('Cepheids', 120,120,4)

    e3.add_observation(26,1000,(100,30))
    e4.add_observation(27,1000,(15,30))

    field0.addStar(e3)
    field0.addStar(e4)

    sky.addField(field0)

    print(sky.fields[0].stars[0].get_magnitudes())