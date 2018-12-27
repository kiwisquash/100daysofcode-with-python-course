import itertools

def friends_teams(friend_list,team_size=2,order_does_matter=False):
    '''Takes a list of friends,
    a team_size (type int, default=2),
    order_does_matter (type bool, default False),
    returns all possible teams'''
    if order_does_matter:
        return list(itertools.permutations(friend_list, team_size))
    else:
        return list(itertools.combinations(friend_list, team_size))

if __name__ == "__main__":
    for team in friends_teams(['Yugi','Joey','Tea','Tristen']):
        print(team)
