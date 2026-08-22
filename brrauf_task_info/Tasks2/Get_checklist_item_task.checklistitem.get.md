---
title: "Get checklist item task.checklistitem.get | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/task-checklist-item-get.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user with read access permission for the task or higher

The method `task.checklistitem.get` retrieves the description of a checklist item by its identifier.

## Method Parameters

Pass parameters in the request according to the order in the table. If the order is violated, the request will return an error.

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **TASKID** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Task identifier.  The identifier can be obtained when [creating a task](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/tasks-task-add.html) or by using the [method to get the list of tasks](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/tasks-task-list.html) |
| **ITEMID** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Checklist item identifier.  The item identifier can be obtained when [adding a new item](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-add.html) or by using the [method to get the list of checklist items](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-get-list.html) |

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
-d '{"TASKID":8017,"ITEMID":479}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.checklistitem.get
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASKID":8017,"ITEMID":479,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.checklistitem.get
```

```javascript
try
{
    const response = await $b24.callMethod(
        'task.checklistitem.get',
        {
            TASKID: 8017,
            ITEMID: 479
        }
    );
    
    const result = response.getData().result;
    console.log('Retrieved checklist item:', result);
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
            'task.checklistitem.get',
            [
                'TASKID' => 8017,
                'ITEMID' => 479
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error retrieving checklist item: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.checklistitem.get',
    {
        TASKID: 8017,
        ITEMID: 479
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
    'task.checklistitem.get',
    [
        'TASKID' => 8017,
        'ITEMID' => 479
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
        "ID": "495",
        "TASK_ID": "8017",
        "PARENT_ID": "457",
        "CREATED_BY": "503",
        "TITLE": "Prepare report Andrew Smith Sarah Johnson Andrew Brown",
        "SORT_INDEX": "4",
        "IS_COMPLETE": "N",
        "IS_IMPORTANT": "Y",
        "TOGGLED_BY": null,
        "TOGGLED_DATE": "",
        "MEMBERS": [
            {
                "ID": "3",
                "TYPE": "U",
                "NAME": "Andrew Brown",
                "PERSONAL_PHOTO": "249",
                "PERSONAL_GENDER": "M",
                "IMAGE": "https://mysite.com/b17053/resize_cache/249/c0120a8d7c10d63c83e32398d1ec4d9e/main/cd526b0644e7ff4d794ea41cb36bc423/odmin.png",
                "IS_COLLABER": false
            },
            {
                "ID": "11",
                "TYPE": "U",
                "NAME": "Andrew Smith",
                "PERSONAL_PHOTO": "231",
                "PERSONAL_GENDER": "M",
                "IMAGE": "https://mysite.com/b17053/resize_cache/231/c0120a8d7c10d63c83e32398d1ec4d9e/main/026bf59e161a0bd50f401d3796800651/66b.jpg",
                "IS_COLLABER": false
            },
            {
                "ID": "103",
                "TYPE": "A",
                "NAME": "Sarah Johnson",
                "PERSONAL_PHOTO": "8644",
                "PERSONAL_GENDER": "F",
                "IMAGE": "https://mysite.com/b17053/resize_cache/8644/c0120a8d7c10d63c83e32398d1ec4d9e/main/45f/45fff10d17d398a5583184c8350cd197/buh.jpg",
                "IS_COLLABER": false
            }
        ],
        "ATTACHMENTS": {
            "1111": {
                "ATTACHMENT_ID": 1111,
                "NAME": "Invoice for client.pdf",
                "SIZE": "148238",
                "FILE_ID": "989",
                "DOWNLOAD_URL": "/bitrix/tools/disk/uf.php?attachedId=1111&action=download&ncc=1",
                "VIEW_URL": "/bitrix/tools/disk/uf.php?attachedId=1111&action=show&ncc=1"
            }
        }
    },
    "time": {
        "start": 1762755387,
        "finish": 1762755387.104804,
        "duration": 0.10480403900146484,
        "processing": 0,
        "date_start": "2025-11-10T09:16:27+02:00",
        "date_finish": "2025-11-10T09:16:27+02:00",
        "operating_reset_at": 1762755987,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Object with [description of checklist item fields](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-get.html#result-fields) |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html#time) | Information about the request execution time |

#### Fields of the result object

| **Name**   `type` | **Description** |
| --- | --- |
| **ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Checklist item identifier |
| **TASK\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Identifier of the task to which the item belongs |
| **PARENT\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Identifier of the parent item.  A value of `0` indicates a root item |
| **CREATED\_BY**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Identifier of the item author |
| **TITLE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Text of the checklist item.  If `PARENT_ID = 0`, the field contains the name of the checklist |
| **SORT\_INDEX**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Sort index.  The smaller the value, the higher the item in the list or sublist |
| **IS\_COMPLETE**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Status of the item. Possible values:  - `Y` — completed, - `N` — not completed |
| **IS\_IMPORTANT**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Importance mark of the item. Possible values:  - `Y` — important, - `N` — ordinary |
| **TOGGLED\_BY**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Identifier of the user who last changed the status of the item.  Can be `null` if the status has not been changed |
| **TOGGLED\_DATE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Date and time of the status change in `ISO 8601` format |
| **MEMBERS**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | List of objects with [description of participants](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-get.html#members) |
| **ATTACHMENTS**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Object with [description of attached files](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-get.html#attachments).  Key — identifier of the file attachment `ATTACHMENT_ID` |

#### Members Object

| **Name**   `type` | **Description** |
| --- | --- |
| **ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | User identifier |
| **TYPE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | User's role in the checklist item. Possible values:  - `A` — participant, - `U` — observer |
| **NAME**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | User's name |
| **PERSONAL\_PHOTO**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Identifier of the user's avatar file on Drive |
| **PERSONAL\_GENDER**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | User's gender. Possible values:  - `M` — male, - `F` — female |
| **IMAGE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Link to the user's avatar |
| **IS\_COLLABER**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Indicates that the user is an external participant |

#### Attachments Object

| **Name**   `type` | **Description** |
| --- | --- |
| **ATTACHMENT\_ID**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Identifier of the attachment |
| **NAME**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | File name |
| **SIZE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | File size in bytes |
| **FILE\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Identifier of the file on Drive |
| **DOWNLOAD\_URL**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Link to download the file |
| **VIEW\_URL**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Link to view the file in the browser |

HTTP status: **400**

```json
{
    "error":"ERROR_CORE",
    "error_description":"TASKS_ERROR_EXCEPTION_#256; Param #1 (itemId) expected by method ctaskchecklistitem::get(), but not given.; 256\/TE\/WRONG_ARGUMENTS\u003Cbr\u003E"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#256; Param #1 (itemId) expected by method ctaskchecklistitem::get(), but not given.; 256/TE/WRONG\_ARGUMENTS\\u003Cbr\\u003E | Required parameters `TASKID` and `ITEMID` not provided |
| `ERROR_CORE` | error\_description":"TASKS\_ERROR\_EXCEPTION\_#256; Param #0 (taskId) for method ctaskchecklistitem::get() expected to be of type \\u0022integer\\u0022, but given something else.; 256/TE/WRONG\_ARGUMENTS\\u003Cbr\\u003E | Incorrect type of value for `TASKID` or `ITEMID` |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#512; Check listitem not found or not accessible; 512/TE/ITEM\_NOT\_FOUND\_OR\_NOT\_ACCESSIBLE\\u003Cbr\\u003E | Possible reasons:  - the order of parameters in the method is violated - the specified `TASKID` or `ITEMID` does not exist - the user does not have access permission to the task |

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
- [Get the list of checklist items task.checklistitem.getlist](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-get-list.html)
- [Delete checklist item task.checklistitem.delete](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-delete.html)
- [Move Checklist Item task.checklistitem.moveafteritem](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-move-after-item.html)
- [Mark checklist item as completed task.checklistitem.complete](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-complete.html)
- [Mark a checklist item as incomplete task.checklistitem.renew](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-renew.html)
- [Check Action Permission for task.checklistitem.isactionallowed](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-is-action-allowed.html)