# Module 3 Lesson 5: After-Class Project
# Project Name: Industrial IoT Grid Multi-Dimensional Sensor Moving Average

class IoTGridTelemetryProcessor:
    def compute_moving_averages(self, input_sensor_stream, window_size=3):
        computed_output_stream = []
        for i in range(len(input_sensor_stream) - window_size + 1):
            sub_window = input_sensor_stream[i : i + window_size]
            window_mean = sum(sub_window) / window_size
            computed_output_stream.append(round(window_mean, 3))
        return computed_output_stream

if __name__ == "__main__":
    processor = IoTGridTelemetryProcessor()
    raw_telemetry = [22.4, 22.8, 23.5, 24.1, 23.9, 22.1]
    print(f"Computed High Precision Telemetry Moving Stream: {processor.compute_moving_averages(raw_telemetry)}")