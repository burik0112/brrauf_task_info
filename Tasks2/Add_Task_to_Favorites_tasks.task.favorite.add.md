---
title: "Add Task to Favorites tasks.task.favorite.add | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/tasks-task-favorite-add.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user with read access to the task

The method `tasks.task.favorite.add` adds a task to Favorites.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **taskId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | The identifier of the task.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-add.html) or by using the [method to get the list of tasks](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-list.html) |

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

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
-d '{"taskId":119}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.favorite.add
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"taskId":119,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.task.favorite.add
```

```javascript
try
{
    const response = await $b24.callMethod(
        'tasks.task.favorite.add',
        {
            taskId: 119,
        }
    );
    
    const result = response.getData().result;
    console.log('Favorite added:', result);
    
    processResult(result);
}
catch( error )
{
    console.error('Error:', error);
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'tasks.task.favorite.add',
            [
                'taskId' => 119
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.task.favorite.add',
    {
        'taskId': 119
    },
    function(result){
        console.info(result.data());
        console.log(result);
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'tasks.task.favorite.add',
    [
        'taskId' => 119
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
    "result": true,
    "time": {
        "start": 1758015040.372338,
        "finish": 1758015040.421553,
        "duration": 0.049214839935302734,
        "processing": 0.015886783599853516,
        "date_start": "2025-09-16T12:30:40+02:00",
        "date_finish": "2025-09-16T12:30:40+02:00",
        "operating_reset_at": 1758015640,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Returns `true` if the task was successfully added to favorites |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html#time) | Information about the request execution time |

HTTP status: **400**

```json
{
    "error":"1",
    "error_description":"Task not found or not accessible"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `0` | wrong task id | The `taskId` parameter contains a value of an incorrect type |
| `1` | Task not found or not accessible | The task was not found or the user does not have access to the task |
| `100` | CTaskItem All parameters in the constructor must have real class type | The required parameter `taskId` is missing |

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

- [Tasks: Overview of Methods](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/index.html)
- [Remove Task from Favorites tasks.task.favorite.remove](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-favorite-remove.html)