# Module 4 Lesson 1: After-Class Project
# Project Name: High-Performance In-Memory Unique User Session Lookup Index

class UserSessionIndex:
    def __init__(self):
        self.active_sessions = {}

    def map_session(self, session_token, user_profile_metadata_dict):
        self.active_sessions[session_token] = user_profile_metadata_dict

    def kill_session(self, target_token):
        if target_token in self.active_sessions:
            del self.active_sessions[target_token]
            return True
        return False

if __name__ == "__main__":
    index = UserSessionIndex()
    index.map_session("TOK-9923x", {"Username": "alice", "PrivilegeLevel": "ROOT_ADMIN"})
    print(f"Active Session Context Verified Map: {index.active_sessions}")