# MIT License
#
# Copyright (c) 2025 CODE6 Team
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# CREATE AN ORGANIZED SOCCER SCORE TABLE BASED ON MATCHES INFORMATION

from typing import List, Dict, Any

teams_input = [
    {
        "name": "Real Madrid",
        "matches": ["W","W","D","W","L","W","W","D","W","W","W","D","W","L","W","W","D","W","W","W","D","W","W","W","D","W","W","L","W","W","W","D","W","W","D","W","W","W"],
        "goals_for": 78,
        "goals_against": 26
    },
    {
        "name": "Barcelona",
        "matches": ["W","D","L","W","W","W","D","W","W","L","W","W","D","W","W","W","D","L","W","W","W","D","W","W","L","W","W","W","D","W","W","L","W","D","W","W","D","W"],
        "goals_for": 72,
        "goals_against": 34
    },
    {
        "name": "Atlético de Madrid",
        "matches": ["W","W","W","D","W","L","W","D","W","W","L","D","W","W","L","W","D","W","W","W","D","W","W","L","W","D","W","W","W","L","W","D","W","W","D","W","L","W"],
        "goals_for": 67,
        "goals_against": 39
    },
    {
        "name": "Girona",
        "matches": ["W","W","W","W","D","W","W","L","W","W","D","L","W","W","W","D","L","W","W","W","D","W","L","W","W","D","W","W","L","W","D","W","W","D","L","W","W","W"],
        "goals_for": 62,
        "goals_against": 42
    },
    {
        "name": "Athletic Club",
        "matches": ["W","D","W","W","W","D","L","W","W","W","D","W","W","L","W","D","W","W","D","W","W","W","L","D","W","W","W","D","L","W","W","D","W","D","W","W","W","D"],
        "goals_for": 59,
        "goals_against": 36
    },
    {
        "name": "Real Sociedad",
        "matches": ["D","W","W","D","W","W","L","W","D","W","D","W","L","W","W","D","D","W","L","W","D","W","W","L","W","D","W","D","L","W","W","W","D","L","W","W","D","W"],
        "goals_for": 51,
        "goals_against": 37
    },
    {
        "name": "Real Betis",
        "matches": ["W","W","D","L","W","W","D","L","W","W","D","W","W","L","D","W","D","W","L","W","D","W","W","D","L","W","W","D","W","L","W","D","W","W","D","L","W","D"],
        "goals_for": 48,
        "goals_against": 40
    },
    {
        "name": "Villarreal",
        "matches": ["L","W","D","W","D","W","W","L","W","D","W","W","D","W","L","D","W","W","L","W","D","L","W","W","D","W","W","D","L","W","D","W","W","D","W","L","W","D"],
        "goals_for": 52,
        "goals_against": 47
    },
    {
        "name": "Valencia",
        "matches": ["W","D","W","L","W","D","W","L","W","D","W","W","D","L","W","D","W","W","L","D","W","D","L","W","D","W","W","L","W","D","W","L","D","W","W","D","L","W"],
        "goals_for": 45,
        "goals_against": 43
    },
    {
        "name": "Osasuna",
        "matches": ["D","L","W","W","D","L","W","D","L","W","W","D","L","W","D","W","D","L","W","W","D","W","D","L","W","D","W","D","L","W","W","D","L","W","D","L","W","D"],
        "goals_for": 41,
        "goals_against": 45
    },
    {
        "name": "Getafe",
        "matches": ["D","W","L","D","W","W","D","L","W","D","W","D","W","L","W","D","W","L","D","W","L","W","W","D","L","D","W","W","D","L","W","D","W","L","D","W","W","L"],
        "goals_for": 38,
        "goals_against": 49
    },
    {
        "name": "Celta Vigo",
        "matches": ["L","D","W","L","W","D","L","W","D","L","W","D","L","W","D","W","D","L","D","W","L","D","W","L","D","W","L","D","L","W","D","W","L","W","D","L","D","W"],
        "goals_for": 36,
        "goals_against": 52
    },
    {
        "name": "Sevilla",
        "matches": ["L","W","D","L","D","W","D","W","L","D","W","D","L","W","D","L","W","W","D","L","W","D","W","L","D","W","D","L","W","L","D","W","D","L","W","D","L","W"],
        "goals_for": 42,
        "goals_against": 55
    },
    {
        "name": "Rayo Vallecano",
        "matches": ["D","D","L","W","D","L","W","D","W","D","L","W","D","W","D","L","W","D","L","D","W","D","L","W","D","L","D","W","D","L","W","D","W","D","L","D","W","D"],
        "goals_for": 32,
        "goals_against": 56
    },
    {
        "name": "Mallorca",
        "matches": ["D","L","D","W","L","W","D","L","D","W","L","D","W","D","L","W","D","L","D","W","L","W","D","W","D","L","W","D","L","W","D","L","D","W","L","D","W","D"],
        "goals_for": 31,
        "goals_against": 55
    },
    {
        "name": "Las Palmas",
        "matches": ["L","W","D","W","L","D","W","D","L","W","D","L","W","D","L","D","W","W","L","D","W","L","D","W","D","L","W","D","L","W","D","L","D","L","W","D","L","W"],
        "goals_for": 29,
        "goals_against": 59
    },
    {
        "name": "Granada",
        "matches": ["L","D","W","L","D","W","L","D","L","W","L","W","D","L","D","W","D","L","W","D","L","D","L","W","L","D","W","L","D","W","D","L","D","W","L","W","D","L"],
        "goals_for": 28,
        "goals_against": 65
    },
    {
        "name": "Cádiz",
        "matches": ["D","L","D","L","D","L","W","D","L","W","D","L","D","W","D","L","W","D","L","D","L","W","D","L","D","L","W","D","L","D","W","D","L","W","D","L","D","L"],
        "goals_for": 26,
        "goals_against": 61
    },
    {
        "name": "Almería",
        "matches": ["L","L","D","L","D","L","D","L","D","L","D","L","D","L","D","L","D","L","D","L","D","L","D","L","D","L","D","L","D","L","D","L","D","L","D","L","D","L"],
        "goals_for": 25,
        "goals_against": 73
    }
]


def analyze_team(team: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze one team.
    Counts wins, draws, losses, points, goal difference,
    and gets the last five matches.
    Returns a new dictionary with all the calculated data.
    """
    wins = 0
    draws = 0
    losses = 0
    for match in team["matches"]:
        if match == "W":
            wins += 1
        elif match == "D":
            draws += 1
        else:
            losses += 1

    points = wins * 3 + draws
    last_five = team["matches"][-5:]
    goal_difference = team["goals_for"] - team["goals_against"]

    return {
        "name": team["name"],
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "points": points,
        "goals_for": team["goals_for"],
        "goals_against": team["goals_against"],
        "goal_difference": goal_difference,
        "last_five": last_five,
        "competition": None
    }


def analyze_all_teams(teams: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Analyze all teams in the list.
    Calls analyze_team() for each team and returns
    a new list with all processed teams.
    """
    processed_list = []
    for team in teams:
        processed = analyze_team(team)
        processed_list.append(processed)
    return processed_list


def sort_and_assign_competitions(teams: List[Dict[str, Any]]) -> None:
    """
    Sorts all teams by points, then goal difference,
    then goals scored.
    After sorting, assigns competitions based on position:
    - Top 4: Champions League
    - 5th–6th: Europa League
    - 7th: Conference League
    - Bottom 2: Relegated
    """
    n = len(teams)

    # Bubble sort
    for i in range(n - 1):
        for j in range(n - i - 1):
            a = teams[j]
            b = teams[j + 1]

            if a["points"] < b["points"]:
                teams[j], teams[j + 1] = teams[j + 1], teams[j]
            elif a["points"] == b["points"]:
                if a["goal_difference"] < b["goal_difference"]:
                    teams[j], teams[j + 1] = teams[j + 1], teams[j]
                elif a["goal_difference"] == b["goal_difference"]:
                    if a["goals_for"] < b["goals_for"]:
                        teams[j], teams[j + 1] = teams[j + 1], teams[j]

    # Assign competitions
    for index, team in enumerate(teams):
        position = index + 1

        if position <= 4:
            team["competition"] = "Champions League"
        elif position <= 6:
            team["competition"] = "Europa League"
        elif position == 7:
            team["competition"] = "Conference League"
        elif position >= len(teams) - 2:
            team["competition"] = "Relegated"
        else:
            team["competition"] = None


def print_league_table(teams: List[Dict[str, Any]]) -> None:
    """
    Prints a formatted league table.
    Shows position, team name, points,
    goals scored, goals conceded, goal difference,
    last 5 matches, and assigned competition.
    """
    print("\n===================================================================================")
    print("                LA LIGA TABLE 2023/2024")
    print("===================================================================================")
    print("Pos | Team               | Pts | GF | GA |  GD  | Last 5        | Competition")
    print("-------------------------------------------------------------------------------")

    position = 1
    for t in teams:
        last5 = " ".join(t["last_five"])
        comp = t["competition"] if t["competition"] is not None else "-"

        print(
            f"{position:>3} | {t['name']:<18} | {t['points']:>3} | "
            f"{t['goals_for']:>2} | {t['goals_against']:>2} | "
            f"{t['goal_difference']:>4} | {last5:<13} | {comp}"
        )
        position += 1

    print("----------------------------------------------------------------------------------\n")


# Execution
processed = analyze_all_teams(teams_input)
sort_and_assign_competitions(processed)
print_league_table(processed)
