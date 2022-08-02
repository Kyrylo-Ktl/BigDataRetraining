class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def __iter__(self):
        return iter(self.members)


team = Team('buddies', ('John', 'Mike'))
for member in team:
    print(member)
