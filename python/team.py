from python.Player import Player


class Team:
    def calc_team_pts_for_each_game_for_all_events(self, cur, players: [], scoring_type, ignore_event: []) -> int:
        # returns list of team avg totals for each game mode
        for player in players:
            Player.calc_all_games(Player(player), cur, scoring_type, ignore_event)
