# Module 5 Lesson 2: After-Class Project
# Project Name: Functional Pipeline Stream Processor Lambda Filtering Framework

class StreamLambdaProcessor:
    def __init__(self, numeric_data_stream):
        self.stream = numeric_data_stream

    def apply_functional_transformations(self, filtering_predicate_lambda, mapping_transform_lambda):
        # Implements modern functional high-order pipeline orchestration mapping steps
        filtered_sub_stream = filter(filtering_predicate_lambda, self.stream)
        transformed_final_stream = map(mapping_transform_lambda, filtered_sub_stream)
        return list(transformed_final_stream)

if __name__ == "__main__":
    raw_telemetry = [12, 45, 68, 23, 90, 104, 15]
    processor = StreamLambdaProcessor(raw_telemetry)
    # Filter for values over 40 and square them
    out = processor.apply_functional_transformations(lambda x: x > 40, lambda y: y ** 2)
    print(f"Functional Lambda Stream Mutation Array: {out}")