import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Extract parameters from query string
    name = req.params.get('name')
    address = req.params.get('address')
    phone = req.params.get('phone')

    # If parameters are not found in query string, try to extract from request body
    if not name or not address or not phone:
        try:
            req_body = req.get_json()
            name = req_body.get('name', name)
            address = req_body.get('address', address)
            phone = req_body.get('phone', phone)
        except ValueError:
            pass

    # Prepare response based on available parameters
    if name and address and phone:
        response_message = (
            f"Hello, {name}. This HTTP triggered function executed successfully. "
            f"Address: {address}, Phone: {phone}."
        )
        return func.HttpResponse(response_message)
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass name, address, and phone in the query string or in the request body for a personalized response.",
            status_code=400
        )
 

 #new file for salary
@app.route(route = "http_trigger_salary")
def http_trigger_salary(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    salary = req.params.get('salary')

    if not salary:
        try:
            req_body = req.get_json()
            salary = req_body.get('salary',salary)
        except ValueError:
            pass


    if salary:
        response_message = (
            f"Salary is : {salary}"
        )
        return func.HttpResponse(response_message)
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully.Pass salary amount in the query string in the response body.",
            status_code=400
        )


