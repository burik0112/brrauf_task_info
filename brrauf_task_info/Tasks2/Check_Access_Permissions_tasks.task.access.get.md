---
title: "Check Access Permissions tasks.task.access.get | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/tasks-task-access-get.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method `tasks.task.access.get` checks the available actions a user can perform on a task.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **id** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html) | Task identifier.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/tasks-task-add.html) or through the old method of [getting the task list](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/tasks/tasks-task-list.html) |

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

The call to the new API differs by adding the `/api/` parameter in the request:

`https://{installation_address}/rest/api/{user_id}/{webhook_token}/tasks.task.access.get`

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
-d '{"id":8017}' \
https://**put_your_bitrix24_address**/rest/api/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.access.get
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"id":8017,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/api/tasks.task.access.get
```

The SDK does not yet support calls to the address /rest/api/. Use direct HTTP requests, for example, via curl or fetch.

```javascript
try
{
    const response = await $b24.callMethod(
        'tasks.task.access.get',
        {
            id: 8017,
        }
    );
    
    const result = response.getData().result;
    console.log('Access data:', result);
    
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
            'tasks.task.access.get',
            [
                'id' => 8017,
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error: ' . $e->getMessage();
}
```

The SDK does not yet support calls to the address /rest/api/. Use direct HTTP requests, for example, via curl or fetch.

```js
BX24.callMethod(
    'tasks.task.access.get',
    {
        id: 8017,
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
    'tasks.task.access.get',
    [
        'id' => 8017,
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```

## Response Handling

HTTP Status: **200**

```json
{
    "result": {
        "read": true,
        "watch": true,
        "mute": true,
        "createSubtask": true,
        "createResult": true,
        "edit": true,
        "remove": true,
        "complete": true,
        "approve": false,
        "disapprove": false,
        "start": false,
        "take": false,
        "delegate": true,
        "defer": false,
        "renew": false,
        "deadline": true,
        "datePlan": true,
        "changeDirector": false,
        "changeResponsible": true,
        "changeAccomplices": true,
        "pause": false,
        "timeTracking": false,
        "mark": true,
        "changeStatus": true,
        "reminder": true,
        "addAuditors": true,
        "elapsedTime": true,
        "favorite": true,
        "checklistAdd": true,
        "checklistEdit": true,
        "checklistSave": true,
        "checklistToggle": true,
        "automate": true,
        "resultEdit": false,
        "completeResult": true,
        "removeResult": false,
        "resultRead": false,
        "admin": true,
        "copy": true,
        "saveAsTemplate": true,
        "attachFile": true,
        "detachFile": true,
        "detachParent": true,
        "createGanttDependence": true,
        "sort": false
    },
    "time": {
        "start": 1764849882,
        "finish": 1764849882.731575,
        "duration": 0.7315750122070312,
        "processing": 0,
        "date_start": "2025-12-04T15:04:42+01:00",
        "date_finish": "2025-12-04T15:04:42+01:00",
        "operating_reset_at": 1764850482,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html) | The root element of the response. Contains an object with a description of the available actions for the current user |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/data-types.html#time) | Information about the request execution time |

HTTP Status: **400**

```json
{
    "error": {
        "code": "BITRIX_REST_V3_EXCEPTION_VALIDATION_REQUESTVALIDATIONEXCEPTION",
        "message": "Error during request object validation",
        "validation": [
            {
                "message": "Required field \`id\` is not specified",
                "field": "id"
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

Error Code: `BITRIX_REST_V3_EXCEPTION_VALIDATION_REQUESTVALIDATIONEXCEPTION`

| **Field** | **Error Description** | **How to Fix** |
| --- | --- | --- |
| `id` | Required field `id` is not specified | Add `id` to the request body |
| `id` | Field `id` requires data type `int` for this request | Ensure that the value is a number, not a string |

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

- [Update Task tasks.task.update](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/tasks-task-update.html)
- [Send Message to Task Chat tasks.task.chat.message.send](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/tasks-task-chat-message-send.html)
- [Delete Task tasks.task.delete](https://apidocs.bitrix24.com/api-reference/rest-v3/tasks/api-reference/rest-v3/tasks/tasks-task-delete.html)