# Module 11 Lesson 1: After-Class Project
# Project Name: Stock Span Optimization Using Monotonic Stack Matrix Engine

class MonotonicStockSpanEngine:
    def calculate_spans(self, daily_quotes_list):
        spans_output = [0] * len(daily_quotes_list)
        index_stack = []
        
        for idx in range(len(daily_quotes_list)):
            while index_stack and daily_quotes_list[index_stack[-1]] <= daily_quotes_list[idx]:
                index_stack.pop()
            spans_output[idx] = idx + 1 if not index_stack else idx - index_stack[-1]
            index_stack.append(idx)
        return spans_output

if __name__ == "__main__":
    engine = MonotonicStockSpanEngine()
    print(f"Calculated Financial Monotonic Spans: {engine.calculate_spans([100, 80, 60, 70, 60, 75, 85])}")