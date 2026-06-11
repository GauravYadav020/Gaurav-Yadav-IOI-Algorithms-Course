# Module 8 Lesson 4: After-Class Project
# Project Name: Microservice Cloud JSON Configuration Contract Structural Validator

import json

class MicroserviceContractValidator:
    def validate_json_string_schema(self, inbound_json_payload_string):
        try:
            # Parse target schema constraints string
            parsed_dict = json.loads(inbound_json_payload_string)
            required_contracts = ["service_id", "port_allocation", "auth_secret"]
            
            for parameter in required_contracts:
                if parameter not in parsed_dict:
                    return f"CONTRACT_VIOLATION_ERROR: Missing parameter field [{parameter}]"
            return "CONTRACT_VERIFIED_VALID_SUCCESS"
        except json.JSONDecodeError as json_malformed_exception:
            return f"MALFORMED_JSON_SYNTAX_CRASH: {json_malformed_exception}"

if __name__ == "__main__":
    validator = MicroserviceContractValidator()
    print(validator.validate_json_string_schema('{"service_id": "AUTH_POD", "port_allocation": 8080}'))