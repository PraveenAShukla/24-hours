import shap

def explain_credit_risk(model, input_data):
    # SHAP Explainer
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(input_data)
    
    # Return feature contributions
    contributions = {col: shap_values[1][0][i] for i, col in enumerate(input_data.columns)}
    return contributions
