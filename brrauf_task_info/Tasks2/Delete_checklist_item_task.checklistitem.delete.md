---
title: "Delete checklist item task.checklistitem.delete | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/task-checklist-item-delete.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/scopes/permissions.html)
> 
> Who can execute the method:
> 
> - any user with editing access to the task
> - Creator, Performer, and Participants of the task

The method `task.checklistitem.delete` removes a checklist item from a task.

You can check permissions for deleting an item using the method [task.checklistitem.isactionallowed](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-is-action-allowed.html).

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **TASKID** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Task identifier.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/tasks-task-add.html) or by using the [getting the list of tasks](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/tasks-task-list.html) method |
| **ITEMID** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Checklist item identifier.  The item identifier can be obtained when [adding a new item](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-add.html) or by using the [getting the list of checklist items](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-get-list.html) method |

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
-d '{"TASKID":13,"ITEMID":475}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.checklistitem.delete
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASKID":13,"ITEMID":475,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.checklistitem.delete
```

```javascript
try
{
    const response = await $b24.callMethod(
        'task.checklistitem.delete',
        {
            TASKID: 13,
            ITEMID: 475
        }
    );
    
    const result = response.getData().result;
    console.log('Deleted checklist item:', result);
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
            'task.checklistitem.delete',
            [
                'TASKID' => 13,
                'ITEMID' => 475
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error deleting checklist item: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.checklistitem.delete',
    {
        TASKID: 13,
        ITEMID: 475
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
    'task.checklistitem.delete',
    [
        'TASKID' => 13,
        'ITEMID' => 475
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
    "result": true,
    "time": {
        "start": 1764594534,
        "finish": 1764594535.201817,
        "duration": 1.2018170356750488,
        "processing": 0,
        "date_start": "2025-12-01T16:08:54+01:00",
        "date_finish": "2025-12-01T16:08:55+01:00",
        "operating_reset_at": 1764595135,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Returns `true` if the checklist item was successfully deleted |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html#time) | Information about the request execution time |

HTTP Status: **400**

```json
{
    "error": "ERROR_CORE",
    "error_description": "TASKS_ERROR_EXCEPTION_#8; Deleting item: action not allowed; 8/TE/ACTION_FAILED_TO_BE_PROCESSED<br>"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#256; Param #1 (itemId) expected by method ctaskchecklistitem::delete(), but not given.; 256/TE/WRONG\_ARGUMENTS | Required parameter `TASKID` or `ITEMID` not specified |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#256; Param #0 (taskId) for method ctaskchecklistitem::delete() expected to be of type "integer", but given something else.; 256/TE/WRONG\_ARGUMENTS | Incorrect value type for `TASKID` or `ITEMID` |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#8; Deleting item: action not allowed; 8/TE/ACTION\_FAILED\_TO\_BE\_PROCESSED | User does not have access to the task or lacks permissions to perform the action |

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

- [Checklists: Overview of Methods](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/index.html)
- [Add checklist item task.checklistitem.add](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-add.html)
- [Update checklist item task.checklistitem.update](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-update.html)
- [Get checklist item task.checklistitem.get](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-get.html)
- [Get the list of checklist items task.checklistitem.getlist](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-get-list.html)
- [Move Checklist Item task.checklistitem.moveafteritem](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-move-after-item.html)
- [Mark checklist item as completed task.checklistitem.complete](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-complete.html)
- [Mark a checklist item as incomplete task.checklistitem.renew](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-renew.html)
- [Check Action Permission for task.checklistitem.isactionallowed](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-is-action-allowed.html)