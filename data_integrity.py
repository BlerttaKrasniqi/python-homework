accounts = [
    {"account_id": 1, "owner": "John", "balance": 500},
    {"account_id": 2, "owner": "", "balance": 300},
    {"account_id": 3, "owner": "Anna", "balance": -100},
    {"account_id": None, "owner": "Mike", "balance": 400}
]




def validate_data(accounts):
    invalid_records = []
    
    for account in accounts:
        issues = []
        if account.get("account_id") is None:
            issues.append("account_id is missing")
        if account.get("owner") == "":
            issues.append("owner is empty")
        if account.get("balance",0)<=0:
            issues.append("balance not positive")
        

        if issues:
            invalid_records.append({
                "record":account,"issue":issues
            })
    return invalid_records


if __name__ == "__main__":
    result = validate_data(accounts)
    for r in result:
        print(f"Issued record: {r['record']} -> "
              f"Issue: {r['issue']}")