# Module 4 Lesson 6: After-Class Project
# Project Name: Enterprise Role-Based Access Control Set Matrix Security Validator

class SecurityRBACValidator:
    def evaluate_clearance(self, identity_roles_set, resource_required_privileges_set):
        # Security criteria rule matching step: Check if role profiles overlap target resources
        authorized_matches = identity_roles_set.intersection(resource_required_privileges_set)
        return len(authorized_matches) > 0

if __name__ == "__main__":
    validator = SecurityRBACValidator()
    user_roles = {"BILLING_VIEWER", "REGIONAL_MANAGER"}
    secure_vault_rules = {"ROOT_ADMIN", "REGIONAL_MANAGER"}
    print(f"Is security clearance authorized for transaction entry? {validator.evaluate_clearance(user_roles, secure_vault_rules)}")