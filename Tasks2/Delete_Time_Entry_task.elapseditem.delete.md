---
title: "Delete Time Entry task.elapseditem.delete | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/task-elapsed-item-delete.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

This method deletes a time entry.

Note

You can check the permission to delete using the special method [task.elapseditem.isactionallowed](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-is-action-allowed.html)

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **TASKID** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Task identifier.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/tasks-task-add.html) or by using the [getting task list method](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/tasks-task-list.html) |
| **ITEMID** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Time entry identifier.  It can be obtained when [creating a new entry](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-add.html) or by using the [getting time entry list method](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-get-list.html) |

Warning

It is mandatory to follow the specified order of parameters in the request as shown in the table. Otherwise, the request will execute with errors.

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

cURL (Webhook)

cURL (OAuth)

JS

PHP

BX24.js

PHP CRest

```
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASKID" : 691, "ITEMID": 5}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.elapseditem.delete
```

```
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASKID" : 691, "ITEMID": 5,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.elapseditem.delete
```

```js
try
{
    const response = await $b24.callMethod(
        'task.elapseditem.delete',
        {
            "TASKID": 691,
            "ITEMID": 5,
        }
    );
    
    const result = response.getData().result;
    console.info(result);
}
catch( error )
{
    console.error(error);
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'task.elapseditem.delete',
            [
                'TASKID' => 691,
                'ITEMID' => 5,
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    if ($result->error()) {
        error_log($result->error());
    } else {
        echo 'Success: ' . print_r($result->data(), true);
    }

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error deleting elapsed item: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.elapseditem.delete',
    {
        "TASKID": 691,
        "ITEMID": 5,
    },
    function(result) {
        if (result.error()) {
            console.error(result.error());
        } else {
            console.info(result.data());
        }
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'task.elapseditem.delete',
    [
        'TASKID' => 691,
        'ITEMID' => 5,
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```

## Response Handling

HTTP status: **200**

In case of successful request execution, the server will return `result:null`

```json
{
    "result": null,
    "time": {
        "start": 1712137817.343984,
        "finish": 1712137817.605804,
        "duration": 0.26182007789611816,
        "processing": 0.018325090408325195,
        "date_start": "2024-04-03T12:50:17+03:00",
        "date_finish": "2024-04-03T12:50:17+03:00"
    }
}
```

HTTP status: **400**

```json
{
    "error": "ERROR_CORE",
    "error_description": "ACTION_NOT_ALLOWED"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** |
| --- | --- |
| `0x000001` | Task not found |
| `0x100002` | Access denied |
| `0x000004` | Action not allowed |
| `0x000040` | Unknown error |

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

- [Time Tracking in Tasks: Overview of Methods](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/index.html)
- [Add Time Entry task.elapseditem.add](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-add.html)
- [Update Time Entry task.elapseditem.update](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-update.html)
- [Get elapsed time record by identifier task.elapseditem.get](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-get.html)
- [Get a list of time spent records task.elapseditem.getlist](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-get-list.html)
- [Check Action Permission for task.elapseditem.isactionallowed](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-is-action-allowed.html)
- [Get a list of methods and their descriptions task.elapseditem.getmanifest](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-get-manifest.html)