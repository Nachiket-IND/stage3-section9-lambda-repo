def lambda_handler(event, context):
    # Log input event
    print("Received event:", event)

    # Simple response
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
