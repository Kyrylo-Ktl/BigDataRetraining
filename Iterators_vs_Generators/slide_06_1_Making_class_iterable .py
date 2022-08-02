class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members


team = Team('buddies', ('John', 'Mike'))
for member in team:
    print(member)
