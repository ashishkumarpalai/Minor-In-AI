def evaluate(expression):
    # Dictionary to map human-readable operators to mathematical symbols
    replacements = {
        "plus": "+",
        "minus": "-",
        "times": "*",
        "divided by": "/"
    }
    
    # Replace the human-readable operators with mathematical symbols
    for word, symbol in replacements.items():
        expression = expression.replace(word, symbol)
    
    # Evaluate the mathematical expression
    result = eval(expression)+.0
    
    # Return the result formatted with 10 decimal places
    # return f"{result:.1f}"
    return(result)


