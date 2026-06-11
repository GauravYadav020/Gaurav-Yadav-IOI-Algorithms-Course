# Module 8 Lesson 2: After-Class Project
# Project Name: Financial Matrix CSV Row Loader Exception Analyzer

class BankCsvIngestionEngine:
    def parse_mock_csv_stream(self, lines_list_stream):
        parsed_records = []
        for line_idx, raw_line in enumerate(lines_list_stream):
            try:
                tokens = [t.strip() for t in raw_line.split(",")]
                if len(tokens) < 3:
                    raise ValueError("Malformed layout schema dimension matching error.")
                
                txn_id = tokens[0]
                amount = float(tokens[1]) # Potential parsing error hazard line
                status = tokens[2]
                parsed_records.append({"TxnID": txn_id, "Value": amount, "Status": status})
            except (ValueError, IndexError) as parsing_anomaly:
                print(f"⚠️ Ingestion Row Warning skipped at Stream Line Index [{line_idx}]: {parsing_anomaly}")
        return parsed_records

if __name__ == "__main__":
    engine = BankCsvIngestionEngine()
    mock_csv = ["TXN001, 1450.50, APPROVED", "TXN002, BAD_DATA_TEXT, FAILED", "TXN003, 89.20"]
    print(f"Successfully Recovered Core Ingestion Matrix: {engine.parse_mock_csv_stream(mock_csv)}")