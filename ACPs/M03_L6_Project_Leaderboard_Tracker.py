# Module 3 Lesson 6: After-Class Project
# Project Name: Real-Time Dynamic Global Gaming Score Leaderboard Matrix

class GlobalLeaderboardMatrix:
    def __init__(self, max_allowed_slots=5):
        self.slots_limit = max_allowed_slots
        self.board = [] # Structure: (Gamertag, TotalScore)

    def ingest_new_score_match(self, gamertag, matching_score):
        self.board.append((gamertag, matching_score))
        self.board.sort(key=lambda element: element[1], reverse=True)
        # Retain only the absolute highest ranking elements matching max slots rules
        self.board = self.board[:self.slots_limit]

if __name__ == "__main__":
    leaderboard = GlobalLeaderboardMatrix()
    leaderboard.ingest_new_score_match("Alpha_Hunter", 4500)
    leaderboard.ingest_new_score_match("IOI_Master", 9999)
    leaderboard.ingest_new_score_match("Cyber_Knight", 7800)
    print(f"Current Global High Score Standings Grid Matrix: {leaderboard.board}")