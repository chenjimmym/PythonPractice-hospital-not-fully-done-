class patient(object):
    def __init__(self, idd, name, allergies):
        self.idd = idd
        self.name = name
        self.allergies = allergies
        self.bed = ''

class hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.bed = 1
    def admit(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            patient.bed = self.bed
            self.bed += 1
            print 'Patient admitted, bed number:', patient.bed, '- Capacity:', len(self.patients), '/', self.capacity
        else:
            print'Hospital is full.'
        return self
    def discharge(self, patient):
        for data in self.patients:
            if data.name == patient:
                self.patients.remove(data)
                
    def info(self):
        print 'Patients currently admitted:'
        for data in self.patients:
            print data.name,
        return self

patient1 = patient(123, 'One', 'candy')
patient2 = patient(321, 'Two', 'beans')
patient3 = patient(321, 'Three', 'beans')
hospital1 = hospital('The One Hospitalv', 2)
hospital1.admit(patient1).admit(patient2).admit(patient3)
hospital1.discharge('One')
hospital1.info()
