---
title: "Check Access to Task tasks.task.getaccess | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/tasks-task-get-access.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method `tasks.task.getaccess` checks the available actions for users on a task.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **taskId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Task identifier.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-add.html) or by using the [get task list method](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-list.html) |
| **users**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Array of user identifiers for which access needs to be checked.  By default, the current user is used.  The user identifier can be obtained using the [get user list method](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/user/user-get.html) |

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
-d '{"taskId":8017,"users":[503,547]}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.getaccess
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"taskId":8017,"users":[503,547],"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.task.getaccess
```

```javascript
try
{
    const response = await $b24.callMethod(
        'tasks.task.getaccess',
        {
            taskId: 8017,
            users: [503, 547],
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

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'tasks.task.getaccess',
            [
                'taskId' => 8017,
                'users' => [503, 547]
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
    'tasks.task.getaccess',
    {
        'taskId': 8017,
        'users': [503, 547]
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
    'tasks.task.getaccess',
    [
        'taskId' => 8017,
        'users' => [503, 547]
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
        "allowedActions": {
            "503": {
                "ACCEPT": false,
                "DECLINE": false,
                "COMPLETE": true,
                "APPROVE": false,
                "DISAPPROVE": false,
                "START": false,
                "PAUSE": true,
                "DELEGATE": true,
                "REMOVE": true,
                "EDIT": true,
                "DEFER": false,
                "RENEW": false,
                "CREATE": true,
                "CHANGE_DEADLINE": true,
                "CHECKLIST_ADD_ITEMS": true,
                "ADD_FAVORITE": false,
                "DELETE_FAVORITE": true,
                "RATE": true,
                "TAKE": false,
                "EDIT.ORIGINATOR": false,
                "CHECKLIST.REORDER": true,
                "ELAPSEDTIME.ADD": true,
                "DAYPLAN.TIMER.TOGGLE": true,
                "EDIT.PLAN": true,
                "CHECKLIST.ADD": true,
                "FAVORITE.ADD": false,
                "FAVORITE.DELETE": true
            },
            "547": {
                "ACCEPT": false,
                "DECLINE": false,
                "COMPLETE": false,
                "APPROVE": false,
                "DISAPPROVE": false,
                // ...
                "FAVORITE.DELETE": false
            }
        }
    },
    "time": {
        "start": 1758177122.815386,
        "finish": 1758177122.911002,
        "duration": 0.09561586380004883,
        "processing": 0.054609060287475586,
        "date_start": "2025-09-18T09:32:02+02:00",
        "date_finish": "2025-09-18T09:32:02+02:00",
        "operating_reset_at": 1758177722,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Root element of the response.  Contains an object with a description of available actions for each user |
| **allowedActions**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | An object where the key is the `user ID`, and the value is an object with [description of available actions](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/fields.html#action) on the task.  If the user executing the method does not have access to the task, an empty array `"allowedActions":[]` will be returned.  For non-existent users from the `users` parameter, the method will return a response with a value of `false` for all actions. |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html#time) | Information about the request execution time |

HTTP Status: **400**

```json
{
    "error":"100",
    "error_description":"Invalid value {} to match with parameter {users}. Should be value of type array."
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `0` | wrong task id | The value in the `taskId` parameter is of an incorrect type |
| `100` | Invalid value {} to match with parameter {users}. Should be value of type array. | An incorrect value was specified in the `users` parameter |
| `100` | CTaskItem All parameters in the constructor must have real class type | The required parameter `taskId` was not specified |

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