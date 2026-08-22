---
title: "Move a task from one stage to another task.stages.movetask | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/stages/task-stages-move-task.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/stages/api-reference/scopes/permissions.html)
> 
> Who can execute the method:
> 
> - any user for stages in "My Planner"
> - any user with access to the group for kanban stages

The method moves a task from one stage to another and allows changing the position of the task within the kanban of the group or "My Planner".

The method works as follows:

- If a group stage is provided, the movement occurs within the group's kanban.
- If "My Planner" stage is provided, the movement occurs within it.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **id** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/stages/api-reference/data-types.html) | Task identifier |
| **stageId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/stages/api-reference/data-types.html) | `ID` of the stage to which the task should be moved |
| **before**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/stages/api-reference/data-types.html) | `ID` of the task before which the task should be placed in the stage |
| **after**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/stages/api-reference/data-types.html) | `ID` of the task after which the task should be placed in the stage |

Note

The `before` and `after` parameters are mutually exclusive. You must specify either one or the other.

If both parameters are not filled, the task is added to the column of the stage according to the project settings or "My Planner".

## Code Examples

cURL (Webhook)

cURL (OAuth)

JS

PHP

BX24.js

PHP CRest

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
"id": 1,
"stageId": 2,
"before": 3,
"after": 4
}' \
https://your-domain.bitrix24.com/rest/_USER_ID_/_CODE_/task.stages.movetask
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: YOUR_ACCESS_TOKEN" \
-d '{
"id": 1,
"stageId": 2,
"before": 3,
"after": 4
}' \
https://your-domain.bitrix24.com/rest/task.stages.movetask
```

```js
try
{
    const response = await $b24.callMethod(
        'task.stages.movetask',
        {
            id: taskId,
            stageId: stageId,
            before: 3,
            after: 4
        }
    );
    
    const result = response.getData().result;
    console.log(result);
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
            'task.stages.movetask',
            [
                'id'     => $taskId,
                'stageId' => $stageId,
                'before' => 3,
                'after'  => 4
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    // Your logic for processing data
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error moving task stage: ' . $e->getMessage();
}
```

```js
const taskId = 1;
const stageId = 2;
BX24.callMethod(
    'task.stages.movetask',
    {
        id: taskId,
        stageId: stageId,
        before: 3,
        after: 4
    },
    function(res)
    {
        console.log(res);
    }
);
```

```php
require_once('crest.php'); // include CRest PHP SDK

$taskId = 1;
$stageId = 2;

// execute request to REST API
$result = CRest::call(
    'task.stages.movetask',
    [
        'id' => $taskId,
        'stageId' => $stageId,
        'before' => 3,
        'after' => 4
    ]
);

// Process response from Bitrix24
if ($result['error']) {
    echo 'Error: '.$result['error_description'];
} else {
    print_r($result['result']);
}
```

## Response Handling

HTTP Status: **200**

```json
{
    "result": true
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/stages/api-reference/data-types.html) | Returns `true` if the stage was successfully moved |

HTTP Status: **400**

```json
{
    "error": "ACCESS_DENIED_MOVE",
    "error_description": "You cannot move this task"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** |
| --- | --- |
| `ACCESS_DENIED_MOVE` | You cannot move this task |
| `TASK_NOT_FOUND` | Task not found or access to it is denied |
| `NOT_FOUND` | Stage not found |

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

- [Stages of Kanban and "My Planner": Overview of Methods](https://apidocs.bitrix24.com/api-reference/tasks/stages/api-reference/tasks/stages/index.html)
- [Add a Kanban or "My Planner" Stage task.stages.add](https://apidocs.bitrix24.com/api-reference/tasks/stages/api-reference/tasks/stages/task-stages-add.html)
- [Update the stage of the kanban or "My Planner" task.stages.update](https://apidocs.bitrix24.com/api-reference/tasks/stages/api-reference/tasks/stages/task-stages-update.html)
- [Get the list of Kanban stages or "My Planner" task.stages.get](https://apidocs.bitrix24.com/api-reference/tasks/stages/api-reference/tasks/stages/task-stages-get.html)
- [Check the ability to move a task task.stages.canmovetask](https://apidocs.bitrix24.com/api-reference/tasks/stages/api-reference/tasks/stages/task-stages-can-move-task.html)
- [Delete a Kanban or "My Planner" Stage task.stages.delete](https://apidocs.bitrix24.com/api-reference/tasks/stages/api-reference/tasks/stages/task-stages-delete.html)