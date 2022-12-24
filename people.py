class Person:
    def __init__(self, enter, exit, weight=60, type=0, age=32):
        self.weight = weight
        self.type = type
        self.age = age

        self.present_floor = enter
        self.enter = enter
        self.exit = exit

    def __str__(self):
        return "[Enter: %d, Exit: %d]"%(self.enter, self.exit)

class People:
    def __init__(self, people_list=[]):
        self.people = people_list

    def __iter__(self):
        return self.people.__iter__()

    def __len__(self):
        return len(self.people) 

    def __str__(self):
        st = ""
        for p in self.people:
            st = st + str(p) + "\n"
        return st

    def join(self, new):
        self.people.extend(new.people)

    def get_weight(self):
        weight = 0
        for p in self.people:
            weight = weight + p.weight
        return weight

    def add_person(self, p):
        self.people.append(p)

    def get_enter_floor(self, floor_nb):
        new_group = People([])
        for p in self.people:
            if p.enter_floor == floor_nb:
                new_group.add_person(p)
        return new_group

    def get_exit_floor(self, floor_nb):
        new_group = People([])
        for p in self.people:
            # print("p: %d = floor: %d"% (p.exit_floor,floor_nb))
            if p.exit_floor == floor_nb:
                new_group.add_person(p)
        return new_group

    def remove_sub_group(self, sub_group):
        lst = []
        for p in self.people:
            if p not in sub_group.people:
                lst.append(p)
        self.people = lst

    def remove_all(self):
        self.people = []

    def get_nb(self):
        return len(self.people)

    # @classmethod
    # def join(cls, group1, group2):
    #     return  PeopleGroup(group1.people.extend(group2.people))

