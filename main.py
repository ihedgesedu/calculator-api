from fastapi import FastAPI, status, HTTPException

app = FastAPI()

# 1. Define allowed origins
# For testing, you can use ["*"], but in production, use your frontend URL
origins = ["*"]

# 2. Add the middleware to your app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a:str, b:str):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both a and b must be numeric")

    return {"result": a + b}


@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a: str, b: str):
    """
    Subtracts number a from number b.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both a and b must be numeric")

    return {"result": a - b}


@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a: str, b: str):
    """
    Multiplies number a by number b.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both a and b must be numeric")

    return {"result": a * b}


@app.get("/divide/{a}/{b}", status_code=200)
def divide(a: str, b: str):
    """
    Divides number a by number b.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both a and b must be numeric")
    
    try:
        return {"result": a / b}
    except ZeroDivisionError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Cannot divide by zero")


@app.get("/imperial-to-metric-height/{feet}/{inches}", status_code=200)
def imperialToMetricHeight(feet: str, inches: str):
    """
    Converts height in feet and inches to centimeters.
    
    Parameters:
    - feet: Number of feet in height
    - inches: Number of inches in height
    
    Returns:
    - JSON object with the result
    """
    try:
        feet = float(feet)
        inches = float(inches)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both feet and inches must be numeric")

    centimeters = (feet * 12 + inches) * 2.54

    return {"result": centimeters}


@app.get("/metric-to-imperial-height/{centimeters}", status_code=200)
def metricToImperialHeight(centimeters: str):
    """
    Converts height in centimeters to feet and inches.
    
    Parameters:
    - centimeters: Height in centimeters
    
    Returns:
    - JSON object with the result
    """
    try:
        centimeters = float(centimeters)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Centimeters must be numeric")

    feet = centimeters // 30.48
    inches = (centimeters % 30.48) // 2.54

    imperialHeight = {"feet": feet, "inches": inches}

    return {"result": imperialHeight}


@app.get("/square-root/{number}", status_code=200)
def squareRoot(number: str):
    """
    Calculates the square root of a number.

    Parameters:
    - number: Number to calculate the square root of
    
    Returns:
    - JSON object with the result
    """
    try:
        number = float(number)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Number must be numeric")

    if number < 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Number must be non-negative")

    try:
        return {"result": number ** 0.5}
    except ZeroDivisionError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Number must be greater than zero")
    

@app.get("/amortization/{months}/{principal}/{monthlyRate}", status_code=200)
def amortization(months: str, principal: str, monthlyRate: str):
    """
    Calculates the monthly payment for a loan based on term, principal (loan amount),
    and interest rate per period.

    Parameters
    - months: Length of loan in months
    - principal: Dollar value of loan after down payment
    - monthlyRate: Interest rate on loan on a monthly basis (APR/12). Must be entered as a decimal value (0.01 instead of 1%)

    Returns
    - JSON object with the result
    """

    try:
        months = float(months)
        principal = float(principal)
        monthlyRate = float(monthlyRate)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="All numbers must be numeric. Please review entries and submit numeric values")

    if (months < 1):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail = "Months must be greater than or equal to 1. Please enter a valid number of months")
    
    if (principal <= 0):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail = "Principal must be greater than 0. Please enter a new principal amount")

    if (monthlyRate < 0):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail = "Monthly rate must be greater than 0. Please enter a new monthly rate")   

    paymentAmount = principal * ((monthlyRate * (1+monthlyRate) ** months) / ((1 + monthlyRate) ** months - 1))
    
    return {'result': paymentAmount}