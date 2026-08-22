---
title: "Get Task by ID tasks.task.get | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/tasks-task-get.html"
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

The method `tasks.task.get` returns information about a task by its ID.

Access to the data depends on permissions:

- administrators see all tasks,
- managers see their employees' tasks,
- others see only the tasks available to them.

## Method Parameters

| **Name**   `type` | **Description** |
| --- | --- |
| **taskId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Task identifier.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-add.html) or by using the [get task list method](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-list.html) |
| **select**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | An array of fields to be returned by the method. You can specify only the fields you need. If the array contains the value `"*"`, all available fields will be returned.  By default, it returns all fields except for custom ones. It is recommended to specify specific fields in the selection, as default fields may change.  To retrieve system fields `UF_CRM_TASK`, `UF_TASK_WEBDAV_FILES`, `UF_MAIL_MESSAGE`, and custom fields, include them in `SELECT`. You can find the names of custom fields using the [tasks.task.getFields](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-get-fields.html) method.  Include `CHAT_ID` in select to get the chat ID for the [new task card](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-new.html) |

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
-d '{"taskId":8017,"select":["ID","TITLE","DESCRIPTION","CREATED_BY","RESPONSIBLE_ID","DEADLINE","UF_CRM_TASK","UF_TASK_WEBDAV_FILES"]}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.get
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"taskId":8017,"select":["ID","TITLE","DESCRIPTION","CREATED_BY","RESPONSIBLE_ID","DEADLINE","UF_CRM_TASK","UF_TASK_WEBDAV_FILES"],"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.task.get
```

```javascript
try
{
    const response = await $b24.callMethod(
        'tasks.task.get',
        {
            taskId: 8017,
            select: [
                'ID',
                'TITLE',
                'DESCRIPTION',
                'CREATED_BY',
                'RESPONSIBLE_ID',
                'DEADLINE',
                'UF_CRM_TASK',
                'UF_TASK_WEBDAV_FILES'
            ]
        }
    );
    
    const result = response.getData().result;
    console.log('Fetched task:', result);
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
            'tasks.task.get',
            [
                'taskId' => 8017,
                'select' => [
                    'ID',
                    'TITLE',
                    'DESCRIPTION',
                    'CREATED_BY',
                    'RESPONSIBLE_ID',
                    'DEADLINE',
                    'UF_CRM_TASK',
                    'UF_TASK_WEBDAV_FILES'
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
    echo 'Error fetching task: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.task.get',
    {
        taskId: 8017,
        select: [
            'ID',
            'TITLE',
            'DESCRIPTION',
            'CREATED_BY',
            'RESPONSIBLE_ID',
            'DEADLINE',
            'UF_CRM_TASK',
            'UF_TASK_WEBDAV_FILES'
        ]
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
    'tasks.task.get',
    [
        'taskId' => 8017,
        'select' => [
            'ID',
            'TITLE',
            'DESCRIPTION',
            'CREATED_BY',
            'RESPONSIBLE_ID',
            'DEADLINE',
            'UF_CRM_TASK',
            'UF_TASK_WEBDAV_FILES'
        ]
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
        "task": {
            "id": "8017",
            "title": "Task Example",
            "description": "Task description with [B]formatting[/B]",
            "createdBy": "503",
            "responsibleId": "547",
            "deadline": "2025-10-24T19:00:00+02:00",
            "ufCrmTask": ["C_627", "CO_591", "L_1177", "T88_3", "D_1723"],
            "ufTaskWebdavFiles": [1065, 1077],
            "ufMailMessage": null,
            "descriptionInBbcode": "Y",
            "favorite": "Y",
            "group": [],
            "creator": {
                "id": "503",
                "name": "Maria Johnson",
                "link": "/company/personal/user/503/",
                "icon": "https://mysite.com/b17053/resize_cache/45749/c0120a8d7c10d63c83e32398d1ec4d9e/main/c89/c89c6b7301880958ea704b5a8470635c/4R5A1256.png",
                "workPosition": "admin"
            },
            "responsible": {
                "id": "547",
                "name": "Maria",
                "link": "/company/personal/user/547/",
                "icon": "/bitrix/images/tasks/default_avatar.png",
                "workPosition": "Tester"
            },
            "action": {
                "accept": false,
                "decline": false,
                "complete": true,
                "approve": false,
                "disapprove": false,
                "start": true,
                "pause": false,
                "delegate": true,
                "remove": true,
                "edit": true,
                "defer": true,
                "renew": false,
                "create": true,
                "changeDeadline": true,
                "checklistAddItems": true,
                "addFavorite": false,
                "deleteFavorite": true,
                "rate": true,
                "take": false,
                "edit.originator": false,
                "checklist.reorder": true,
                "elapsedtime.add": true,
                "dayplan.timer.toggle": true,
                "edit.plan": true,
                "checklist.add": true,
                "favorite.add": false,
                "favorite.delete": true
            }
        }
    },
    "time": {
        "start": 1759759363,
        "finish": 1759759363.155413,
        "duration": 0.15541291236877441,
        "processing": 0,
        "date_start": "2025-10-06T17:02:43+02:00",
        "date_finish": "2025-10-06T17:02:43+02:00",
        "operating_reset_at": 1759759963,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Object containing the response data.  Returns an empty array `"result":[],` if the task does not exist or the user does not have access to the task |
| **task**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Object with [task description](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/fields.html) after the operation is performed |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html#time) | Information about the request execution time |

HTTP Status: **400**

```json
{
    "error": "100",
    "error_description": "Invalid value {} to match with parameter {select}. Should be value of type array. (internal error)"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** |  |
| --- | --- | --- |
| `0` | wrong task id | The value of the `taskId` parameter is of an incorrect type |
| `100` | CTaskItem All parameters in the constructor must have real class type (internal error) | The required parameter `taskId` was not provided |
| `100` | Invalid value {} to match with parameter {select}. Should be value of type array. (internal error) | The `select` parameter was provided empty or contains invalid values |

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
- [Add Task tasks.task.add](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-add.html)
- [Update Task tasks.task.update](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-update.html)
- [Get the list of tasks tasks.task.list](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-list.html)
- [Delete Task tasks.task.delete](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-delete.html)
- [Get the list of fields tasks.task.getFields](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-get-fields.html)
- [How to Create a Task with an Attached File](https://apidocs.bitrix24.com/api-reference/tasks/tutorials/tasks/how-to-create-task-with-file.html)
- [How to Attach a Task to a SPA](https://apidocs.bitrix24.com/api-reference/tasks/tutorials/tasks/how-to-connect-task-to-spa.html)