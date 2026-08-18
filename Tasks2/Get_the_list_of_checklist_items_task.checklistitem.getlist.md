---
title: "Get the list of checklist items task.checklistitem.getlist | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/task-checklist-item-get-list.html"
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

The method `task.checklistitem.getlist` retrieves a list of checklist items in a task.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **TASKID** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Task identifier.  The identifier can be obtained when [creating a task](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/tasks-task-add.html) or by using the [get task list method](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/tasks-task-list.html) |
| **ORDER**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | An object for sorting the result in the form `{"field": "sort value", ... }`.  You can sort by the following fields:  - `ID` — checklist item identifier - `PARENT_ID` — parent item identifier - `CREATED_BY` — identifier of the item author - `TITLE` — text of the checklist item - `SORT_INDEX` — sort index - `IS_COMPLETE` — completion status of the item - `IS_IMPORTANT` — importance mark of the item - `TOGGLED_BY` — identifier of the user who last changed the item's status - `TOGGLED_DATE` — date and time of the item's status change  The sort direction can take the following values:  - `asc` — ascending - `desc` — descending  By default, the result is sorted by `ID` in descending order |

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
-d '{"TASKID":8017,"ORDER":{"IS_COMPLETE":"ASC"}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.checklistitem.getlist
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASKID":8017,"ORDER":{"IS_COMPLETE":"ASC"},"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.checklistitem.getlist
```

```javascript
// callListMethod: Retrieves all data at once.
// Use only for small selections (< 1000 items) due to high
// memory load.

try {
const response = await $b24.callListMethod(
    'task.checklistitem.getlist',
    {
    TASKID: 8017,
    ORDER: {
        IS_COMPLETE: 'ASC'
    }
    },
    (progress: number) => { console.log('Progress:', progress) }
);
const items = response.getData() || [];
for (const entity of items) { console.log('Entity:', entity) }
} catch (error: any) {
console.error('Request failed', error)
}

// fetchListMethod: Retrieves data in parts using an iterator.
// Use for large volumes of data for efficient memory consumption.

try {
const generator = $b24.fetchListMethod('task.checklistitem.getlist', {
    TASKID: 8017,
    ORDER: {
    IS_COMPLETE: 'ASC'
    }
}, 'ID');
for await (const page of generator) {
    for (const entity of page) { console.log('Entity:', entity) }
}
} catch (error: any) {
console.error('Request failed', error)
}

// callMethod: Manual control of pagination through the start parameter.
// Use for precise control over request batches.
// Less efficient for large data than fetchListMethod.

try {
const response = await $b24.callMethod('task.checklistitem.getlist', {
    TASKID: 8017,
    ORDER: {
    IS_COMPLETE: 'ASC'
    }
}, 0);
const result = response.getData().result || [];
for (const entity of result) { console.log('Entity:', entity) }
} catch (error: any) {
console.error('Request failed', error)
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'task.checklistitem.getlist',
            [
                'TASKID' => 8017,
                'ORDER' => [
                    'IS_COMPLETE' => 'ASC'
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
    echo 'Error fetching checklist items: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.checklistitem.getlist',
    {
        'TASKID': 8017,
        'ORDER': {
            'IS_COMPLETE': 'ASC'
        }
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
    'task.checklistitem.getlist',
    [
        'TASKID' => 8017,
        'ORDER' => [
            'IS_COMPLETE' => 'ASC'
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
    "result": [
        {
            "ID": "477",
            "TASK_ID": "8017",
            "PARENT_ID": "431",
            "CREATED_BY": "503",
            "TITLE": "Prepare contract Sarah Johnson",
            "SORT_INDEX": "2",
            "IS_COMPLETE": "N",
            "IS_IMPORTANT": "N",
            "TOGGLED_BY": "503",
            "TOGGLED_DATE": "2025-11-10T15:02:30+02:00",
            "MEMBERS": [
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
                "1113": {
                    "ATTACHMENT_ID": 1113,
                    "NAME": "Instructions.docx",
                    "SIZE": "115161",
                    "FILE_ID": "5065",
                    "DOWNLOAD_URL": "/bitrix/tools/disk/uf.php?attachedId=1113&action=download&ncc=1",
                    "VIEW_URL": "/bitrix/tools/disk/uf.php?attachedId=1113&action=show&ncc=1"
                },
                "1115": {
                    "ATTACHMENT_ID": 1115,
                    "NAME": "Document list.xlsx",
                    "SIZE": "14675",
                    "FILE_ID": "5067",
                    "DOWNLOAD_URL": "/bitrix/tools/disk/uf.php?attachedId=1115&action=download&ncc=1",
                    "VIEW_URL": "/bitrix/tools/disk/uf.php?attachedId=1115&action=show&ncc=1"
                }
            }
        },
        {
            "ID": "431",
            "TASK_ID": "8017",
            "PARENT_ID": 0,
            "CREATED_BY": "503",
            "TITLE": "Checklist 1",
            "SORT_INDEX": "0",
            "IS_COMPLETE": "N",
            "IS_IMPORTANT": "N",
            "TOGGLED_BY": null,
            "TOGGLED_DATE": "",
            "MEMBERS": [],
            "ATTACHMENTS": []
        },
        {
            "ID": "447",
            "TASK_ID": "8017",
            "PARENT_ID": "431",
            "CREATED_BY": "503",
            "TITLE": "Agree on details with the client",
            "SORT_INDEX": "1",
            "IS_COMPLETE": "N",
            "IS_IMPORTANT": "N",
            "TOGGLED_BY": null,
            "TOGGLED_DATE": "",
            "MEMBERS": [],
            "ATTACHMENTS": []
        },
        {
            "ID": "469",
            "TASK_ID": "8017",
            "PARENT_ID": "447",
            "CREATED_BY": "503",
            "TITLE": "Agree with the manager Andrew Smith Andrew Johnson",
            "SORT_INDEX": "2",
            "IS_COMPLETE": "N",
            "IS_IMPORTANT": "N",
            "TOGGLED_BY": null,
            "TOGGLED_DATE": "",
            "MEMBERS": [
                {
                    "ID": "3",
                    "TYPE": "A",
                    "NAME": "Andrew Smith",
                    "PERSONAL_PHOTO": "249",
                    "PERSONAL_GENDER": "M",
                    "IMAGE": "https://mysite.com/b17053/resize_cache/249/c0120a8d7c10d63c83e32398d1ec4d9e/main/cd526b0644e7ff4d794ea41cb36bc423/odmin.png",
                    "IS_COLLABER": false
                },
                {
                    "ID": "11",
                    "TYPE": "U",
                    "NAME": "Andrew Johnson",
                    "PERSONAL_PHOTO": "231",
                    "PERSONAL_GENDER": "",
                    "IMAGE": "https://mysite.com/b17053/resize_cache/231/c0120a8d7c10d63c83e32398d1ec4d9e/main/026bf59e161a0bd50f401d3796800651/66b.jpg",
                    "IS_COLLABER": false
                }
            ],
            "ATTACHMENTS": []
        },
        {
            "ID": "471",
            "TASK_ID": "8017",
            "PARENT_ID": "447",
            "CREATED_BY": "503",
            "TITLE": "Prepare solution",
            "SORT_INDEX": "1",
            "IS_COMPLETE": "N",
            "IS_IMPORTANT": "N",
            "TOGGLED_BY": null,
            "TOGGLED_DATE": "",
            "MEMBERS": [],
            "ATTACHMENTS": []
        },
        {
            "ID": "491",
            "TASK_ID": "8017",
            "PARENT_ID": "431",
            "CREATED_BY": "503",
            "TITLE": "Sign contract",
            "SORT_INDEX": "3",
            "IS_COMPLETE": "N",
            "IS_IMPORTANT": "N",
            "TOGGLED_BY": null,
            "TOGGLED_DATE": "",
            "MEMBERS": [],
            "ATTACHMENTS": []
        },
        {
            "ID": "433",
            "TASK_ID": "8017",
            "PARENT_ID": "431",
            "CREATED_BY": "503",
            "TITLE": "Find all documents for the client",
            "SORT_INDEX": "0",
            "IS_COMPLETE": "Y",
            "IS_IMPORTANT": "N",
            "TOGGLED_BY": "503",
            "TOGGLED_DATE": "2025-11-10T15:02:30+02:00",
            "MEMBERS": [],
            "ATTACHMENTS": []
        },
        {
            "ID": "485",
            "TASK_ID": "8017",
            "PARENT_ID": "447",
            "CREATED_BY": "503",
            "TITLE": "Arrange a meeting Andrew Johnson",
            "SORT_INDEX": "0",
            "IS_COMPLETE": "Y",
            "IS_IMPORTANT": "N",
            "TOGGLED_BY": "503",
            "TOGGLED_DATE": "2025-11-10T15:02:33+02:00",
            "MEMBERS": [
                {
                    "ID": "11",
                    "TYPE": "U",
                    "NAME": "Andrew Johnson",
                    "PERSONAL_PHOTO": "231",
                    "PERSONAL_GENDER": "",
                    "IMAGE": "https://mysite.com/b17053/resize_cache/231/c0120a8d7c10d63c83e32398d1ec4d9e/main/026bf59e161a0bd50f401d3796800651/66b.jpg",
                    "IS_COLLABER": false
                }
            ],
            "ATTACHMENTS": []
        }
    ],
    "time": {
        "start": 1762780903,
        "finish": 1762780903.978847,
        "duration": 0.9788470268249512,
        "processing": 0,
        "date_start": "2025-11-10T16:21:43+02:00",
        "date_finish": "2025-11-10T16:21:43+02:00",
        "operating_reset_at": 1762781503,
        "operating": 0.3446669578552246
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | A list of objects with [description of checklist item fields](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-get-list.html#result-fields) |
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
| **IS\_COMPLETE**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Completion status of the item. Possible values:  - `Y` — completed, - `N` — not completed |
| **IS\_IMPORTANT**   [`boolean`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Importance mark of the item. Possible values:  - `Y` — important, - `N` — ordinary |
| **TOGGLED\_BY**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Identifier of the user who last changed the item's status.  Can be `null` if the status has not been changed |
| **TOGGLED\_DATE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Date and time of the item's status change in `ISO 8601` format |
| **MEMBERS**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | A list of objects with [description of participants](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-get-list.html#members) |
| **ATTACHMENTS**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | An object with [description of attached files](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-get-list.html#attachments).  The key is the attachment file identifier `ATTACHMENT_ID` |

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
| **ATTACHMENT\_ID**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Attachment identifier |
| **NAME**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | File name |
| **SIZE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | File size in bytes |
| **FILE\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | File identifier on Drive |
| **DOWNLOAD\_URL**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Link to download the file |
| **VIEW\_URL**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/data-types.html) | Link to view the file in the browser |

HTTP status: **400**

```json
{
    "error":"ERROR_CORE",
    "error_description":"TASKS_ERROR_EXCEPTION_#8; Action failed; 8\/TE\/ACTION_FAILED_TO_BE_PROCESSED\u003Cbr\u003E"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#8; Action failed; 8/TE/ACTION\_FAILED\_TO\_BE\_PROCESSED\\u003Cbr\\u003E | The user does not have access to the task |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#256; Param #0 (taskId) for method ctaskchecklistitem::getlist() expected to be of type \\u0022integer\\u0022, but given something else.; 256/TE/WRONG\_ARGUMENTS\\u003Cbr\\u003E | The required parameter `TASKID` is not provided or an incorrect type is specified |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#256; Param #1 (arOrder) for method ctaskchecklistitem::getlist() must not contain key \\u0022IS\_COMPLETED\\u0022.; 256/TE/WRONG\_ARGUMENTS\\u003Cbr\\u003E | An invalid field is specified in `ORDER` |

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
- [Delete checklist item task.checklistitem.delete](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-delete.html)
- [Move Checklist Item task.checklistitem.moveafteritem](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-move-after-item.html)
- [Mark checklist item as completed task.checklistitem.complete](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-complete.html)
- [Mark a checklist item as incomplete task.checklistitem.renew](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-renew.html)
- [Check Action Permission for task.checklistitem.isactionallowed](https://apidocs.bitrix24.com/api-reference/tasks/checklist-item/api-reference/tasks/checklist-item/task-checklist-item-is-action-allowed.html)