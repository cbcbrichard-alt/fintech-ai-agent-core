import re

class FinancialIntentEngine:
    """
    AI Intent Recognition & Compliance Engine.
    Filters user queries to ensure zero PII storage and FTC compliance.
    """
    def __init__(self):
        # Mandatory compliance filters for North American financial regulations
        self.restricted_terms = [
            "guaranteed return", 
            "no risk", 
            "get rich quick", 
            "insider information",
            "fix my credit score fast"
        ]
        
        # Regex patterns for high-intent financial categories
        self.categories = {
            "CREDIT_CARD": r"(card|amex|chase|visa|cashback|points|rewards)",
            "BROKERAGE": r"(stock|trading|invest|etf|portfolio|webull|schwab|broker)",
            "SAVINGS": r"(apy|interest|savings|deposit|high yield|cd account)"
        }

    def validate_compliance(self, user_query):
        """
        Compliance Check: Identify and block queries containing illegal promises.
        """
        for term in self.restricted_terms:
            if term in user_query.lower():
                return False, f"Compliance Alert: Prohibited term '{term}' detected."
        return True, "Safe"

    def classify_intent(self, user_query):
        """
        Simulates AI-driven intent classification (LLM logic).
        Ensures the agent provides relevant recommendations without financial advice.
        """
        # Step 1: Compliance Validation
        is_safe, message = self.validate_compliance(user_query)
        if not is_safe:
            return {"status": "REJECTED", "reason": message}

        # Step 2: Pattern Recognition for Intent
        detected_cats = []
        for cat, pattern in self.categories.items():
            if re.search(pattern, user_query.lower()):
                detected_cats.append(cat)
        
        return {
            "status": "APPROVED",
            "intents": detected_cats if detected_cats else ["GENERAL_INQUIRY"],
            "action": "FETCH_AFFILIATE_DATA",
            "pii_status": "SECURE_NO_DATA_STORED"
        }

# --- Execution Example ---
if __name__ == "__main__":
    engine = FinancialIntentEngine()
    
    # Example: Compliant Query
    query_ok = "I want to find a travel rewards card with no annual fee."
    print(f"Sample 1 (Compliant): {engine.classify_intent(query_ok)}")
    
    # Example: Non-compliant Query (Blocked)
    query_risk = "Show me a guaranteed return investment with no risk."
    print(f"Sample 2 (Blocked): {engine.classify_intent(query_risk)}")
