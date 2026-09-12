def analyze_incident(severity_indicator:str):
    
    severity = severity_indicator.lower()
    
    if severity in ["critical","high"]:
        return{
            "severity":"CRITICAL",
            "priority":"P0"
        } 
        
    elif severity == "medium":
        return{
            "severity":"MODERATE",
            "priority":"P1"
        }
        
    else:
        return{
            "severity":"LOW",
            "priority":"P2"
        }