# Module 17 Lesson 2: After-Class Project
# Project Name: Timeline Deadlines Task Profit Optimization Engine

class TaskJob:
    def __init__(self, job_id, final_deadline, estimated_profit):
        self.id = job_id
        self.deadline = final_deadline
        self.profit = estimated_profit

def arrange_max_profit_sequence(jobs_list, horizon_limit_slots=100):
    jobs_list.sort(key=lambda job: job.profit, reverse=True)
    timeline_allocation_slots = [-1] * horizon_limit_slots
    total_yield_score = 0
    
    for job in jobs_list:
        for slot in range(min(horizon_limit_slots, job.deadline) - 1, -1, -1):
            if timeline_allocation_slots[slot] == -1:
                timeline_allocation_slots[slot] = job.id
                total_yield_score += job.profit
                break
    return total_yield_score

if __name__ == "__main__":
    tasks = [TaskJob('J1', 2, 100), TaskJob('J2', 1, 19), TaskJob('J3', 2, 27)]
    print(f"Maximum calculated cash flow throughput under constraints metric: {arrange_max_profit_sequence(tasks)}")