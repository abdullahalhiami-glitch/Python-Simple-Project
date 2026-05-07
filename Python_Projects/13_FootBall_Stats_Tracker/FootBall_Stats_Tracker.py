# Football Stats Tracker

league = {}

def add_team(team_name):
    if team_name not in league:
        league[team_name] = {"points": 0, "goals_for": 0, "goals_against": 0}

def add_match_result(team_a, team_b, score_a, score_b):
    if team_a in league and team_b in league:
        league[team_a]["goals_for"] += score_a
        league[team_a]["goals_against"] += score_b
        league[team_b]["goals_for"] += score_b
        league[team_b]["goals_against"] += score_a
        if score_a > score_b:
            league[team_a]["points"] += 3
        elif score_a < score_b:
            league[team_b]["points"] += 3
        else:
            league[team_a]["points"] += 1
            league[team_b]["points"] += 1

def get_team_stats(team_name):
    if team_name in league:
        return league[team_name]["points"], league[team_name]["goals_for"], league[team_name]["goals_against"]
    return None

def calculate_goal_difference(team_name):
    if team_name in league:
        return league[team_name]["goals_for"] - league[team_name]["goals_against"]
    return None

def get_league_standings():
    return sorted(league.keys(), key=lambda t: league[t]["points"], reverse=True)

def get_top_scoring_team():
    if league:
        return max(league.keys(), key=lambda t: league[t]["goals_for"])
    return None

def get_best_defense_team():
    if league:
        return min(league.keys(), key=lambda t: league[t]["goals_against"])
    return None

def clear_league_data():
    league.clear()