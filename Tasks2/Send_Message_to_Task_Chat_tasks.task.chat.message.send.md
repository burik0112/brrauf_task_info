---
title: "Send Message to Task Chat tasks.task.chat.message.send | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/tasks-task-chat-message-send.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user with read access permission for the task or higher

The method `tasks.task.chat.message.send` sends a new message to the task chat.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **fields** \*   [`object`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html) | Object with [message parameters](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/tasks-task-chat-message-send.html#fields) |

### Parameter fields

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **taskId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html) | Identifier of the task to which the message should be sent.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/tasks-task-add.html) or by the old method of [getting the task list](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/tasks/tasks-task-list.html) |
| **text** \*   [`string`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html) | Message text |

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

The new API call differs by the addition of the `/api/` parameter in the request:

`https://{installation_address}/rest/api/{user_id}/{webhook_token}/tasks.task.chat.message.send`

cURL (Webhook)

cURL (OAuth)

JS

PHP

BX24.js

PHP CRest

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"fields":{"taskId":51,"text":"Message from external system"}}' \
https://**put_your_bitrix24_address**/rest/api/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.chat.message.send
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"fields":{"taskId":51,"text":"Message from external system"},"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/api/tasks.task.chat.message.send
```

The SDK does not yet support calls to the address /rest/api/. Use direct HTTP requests, for example, via curl or fetch.

```javascript
try
{
    const response = await $b24.callMethod(
        'tasks.task.chat.message.send',
        {
            fields: {
                taskId: 51,
                text: 'Message from external system',
            }
        }
    );
    
    const result = response.getData().result;
    console.log('Message sent with ID:', result);
    
    processResult(result);
}
catch( error )
{
    console.error('Error:', error);
}
```

The SDK does not yet support calls to the address /rest/api/. Use direct HTTP requests, for example, via curl or fetch.

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'tasks.task.chat.message.send',
            [
                'fields' =>
                [
                    'taskId' => 51,
                    'text' => 'Message from external system'
                ]
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error sending chat message: ' . $e->getMessage();
}
```

The SDK does not yet support calls to the address /rest/api/. Use direct HTTP requests, for example, via curl or fetch.

```js
BX24.callMethod(
    'tasks.task.chat.message.send',
    {
        'fields': {
            'taskId': 51,
            'text': 'Message from external system'
        }
    },
    function(result){
        console.info(result.data());
        console.log(result);
    }
);
```

The SDK does not yet support calls to the address /rest/api/. Use direct HTTP requests, for example, via curl or fetch.

```php
require_once('crest.php');

$result = CRest::call(
    'tasks.task.chat.message.send',
    [
        'fields' =>
        [
            'taskId' => 51,
            'text' => 'Message from external system'
        ]
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```

## Response Handling

HTTP status: **200**

```json
{
    "result": {
        "result": true
    },
    "time": {
        "start": 1762257254,
        "finish": 1762257254.211513,
        "duration": 0.21151304244995117,
        "processing": 0,
        "date_start": "2025-11-04T15:54:14+01:00",
        "date_finish": "2025-11-04T15:54:14+01:00",
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html) | Root element of the response.  Contains an object with the key `result` and the value `true` if the message was sent successfully |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html#time) | Information about the execution time of the request |

HTTP status: **400**

```json
{
    "error": {
        "code": "BITRIX_REST_V3_EXCEPTION_VALIDATION_DTOVALIDATIONEXCEPTION",
        "message": "Error during object validation",
        "validation": [
            {
                "message": "The required field \u0022taskId\u0022 is not filled",
                "field": "taskId"
            }
        ]
    }
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error.code**   `string` | String error code. Use it to identify the type of exception |
| **error.message**   `string` | Text description of the error |
| **error.validation**   `array` | Array with error details. Present only in data validation errors `BITRIX_REST_V3_EXCEPTION_VALIDATION_REQUESTVALIDATIONEXCEPTION` |
| **error.validation\[\].field**   `string` | Name of the field where the validation error occurred |
| **error.validation\[\].message**   `string` | Description of the error related to the specified field |

Error code: `BITRIX_REST_V3_EXCEPTION_VALIDATION_REQUESTVALIDATIONEXCEPTION`

| **Field** | **Error Description** | **How to Fix** |
| --- | --- | --- |
| `taskId`   `fields`   `text` | Required field `#FIELD#` is not specified | Add the specified field to the request body |
| `#FIELD#` | Field `#FIELD#` requires data type `#TYPE#` for this request | Ensure that the passed value is of the correct type |

Error code: `BITRIX_REST_V3_EXCEPTION_ACCESSDENIEDEXCEPTION`

| **Field** | **Error Description** | **How to Fix** |
| --- | --- | --- |
| `taskId` | Access denied | No access to the task |

HTTP Status: **20x**, **40x**, **50x**

The errors described below may occur when calling any method.

| **Status** | **Code**   **Error Message** | **Description** |
| --- | --- | --- |
| `500` | `INTERNAL_SERVER_ERROR`   Internal server error | An internal server error has occurred, please contact the server administrator or [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `500` | `ERROR_UNEXPECTED_ANSWER`   Server returned an unexpected response | An internal server error has occurred, please contact the server administrator or [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `503` | `QUERY_LIMIT_EXCEEDED`   Too many requests | The [request intensity limit](https://apidocs.bitrix24.com/limits.html) has been exceeded |
| `405` | `ERROR_BATCH_METHOD_NOT_ALLOWED`   Method is not allowed for batch usage | The current method is not allowed to be called using [batch](https://apidocs.bitrix24.com/settings/how-to-call-rest-api/batch.html) |
| `400` | `ERROR_BATCH_LENGTH_EXCEEDED`   Max batch length exceeded | The maximum length of parameters passed to the [batch](https://apidocs.bitrix24.com/settings/how-to-call-rest-api/batch.html) method has been exceeded |
| `401` | `NO_AUTH_FOUND`   Wrong authorization data | Invalid [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) or [webhook code](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) |
| `400` | `INVALID_REQUEST`   Https required | The methods must be called using the HTTPS protocol |
| `503` | `OVERLOAD_LIMIT`   REST API is blocked due to overload | The REST API is blocked due to overload. This is a manual individual block, to remove it you need to contact [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `403` | `ACCESS_DENIED`   REST API is available only on commercial plans | The REST API is available only on commercial plans |
| `403` | `INVALID_CREDENTIALS`   Invalid request credentials | The user whose [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) or [webhook](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) was used to call the method lacks permissions |
| `404` | `ERROR_MANIFEST_IS_NOT_AVAILABLE`   Manifest is not available | The manifest is not available |
| `403` | `insufficient_scope`   The request requires higher privileges than provided by the webhook token | The request requires higher privileges than those provided by the [webhook](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) token |
| `401` | `expired_token`   The access token provided has expired | The provided [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) has expired |
| `403` | `user_access_error`   The user does not have access to the application | The user does not have access to the application. This means that the application is installed, but the account administrator has allowed access to this application only for specific users |
| `500` | `PORTAL_DELETED`   Portal was deleted | The public part of the site is closed. To open the public part of the site on an on-premise installation, disable the option "Temporary closure of the public part of the site". Path to the setting: *Desktop > Settings > Product Settings > Module Settings > Main Module > Temporary closure of the public part of the site* |

## Continue Learning

- [Add Task tasks.task.add](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/tasks-task-add.html)
- [Update Task tasks.task.update](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/tasks-task-update.html)
- [New Task Card: Overview of Changes](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/tasks/tasks-new.html)