---
title: "Get the list of comments task.commentitem.getlist | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/comment-item/task-comment-item-get-list.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user with read access permission for the task or higher

The method `task.commentitem.getlist` retrieves a list of comments for a task.

Development of the method has been halted since version `tasks 25.700.0`

The method `task.commentitem.getlist` does not work in the [new task card](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/tasks-new.html), use the method [im.dialog.messages.get](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/chats/messages/im-dialog-messages-get.html) to work with task chat.

## Method Parameters

Pass parameters in the request according to the order in the table. If the order is violated, the request will return an error.

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **TASKID** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Task identifier.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/tasks-task-add.html) or by using the [get task list method](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/tasks-task-list.html) |
| **ORDER**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | An object for sorting the result in the form `{"field": "sort value", ... }`.  You can sort by the following fields:  - `ID` — comment identifier - `AUTHOR_ID` — comment author's identifier - `AUTHOR_NAME` — author's name - `AUTHOR_EMAIL` — author's email address - `POST_DATE` — comment publication date  The sorting direction can take the following values:  - `asc` — ascending - `desc` — descending  By default, the result is sorted in descending order by comment identifier |
| **FILTER**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | An object for filtering the result in the form `{"field": "filter value", ... }`. The value of the filtered field can be a single value or an array of values.  You can filter by the following fields:  - `ID` — comment identifier - `AUTHOR_ID` — comment author's identifier - `AUTHOR_NAME` — author's name - `POST_DATE` — comment publication date  You can specify a prefix with the type of filtering before the name of the filtered field:  - `!` — not equal - `<=` — less than or equal to - `<` — less than - `>=` — greater than or equal to - `>` — greater than  By default, records are not filtered |

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
-d '{"TASKID":8017,"ORDER":{"POST_DATE":"asc"},"FILTER":{"AUTHOR_ID":503,">=POST_DATE":"2025-01-01"}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.commentitem.getlist
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASKID":8017,"ORDER":{"POST_DATE":"asc"},"FILTER":{"AUTHOR_ID":503,">=POST_DATE":"2025-01-01"},"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.commentitem.getlist
```

```js
// callListMethod is recommended when you need to retrieve the entire set of list data and the volume of records is relatively small (up to about 1000 items). The method loads all data at once, which can lead to high memory load when working with large volumes.

try {
  const response = await $b24.callListMethod(
    'task.commentitem.getlist',
    {
      "TASKID": 8017,
      "ORDER": {
        "POST_DATE": "asc",
      },
      "FILTER": {
        "AUTHOR_ID": 503,
        ">=POST_DATE": "2025-01-01",
      }
    },
    (progress) => { console.log('Progress:', progress) }
  )
  const items = response.getData() || []
  for (const entity of items) { console.log('Entity:', entity) }
} catch (error) {
  console.error('Request failed', error)
}

// fetchListMethod is preferable when working with large datasets. The method implements iterative selection using a generator, allowing data to be processed in parts and efficiently using memory.

try {
  const generator = $b24.fetchListMethod('task.commentitem.getlist', {
    "TASKID": 8017,
    "ORDER": {
      "POST_DATE": "asc",
    },
    "FILTER": {
      "AUTHOR_ID": 503,
      ">=POST_DATE": "2025-01-01",
    }
  }, 'ID')
  for await (const page of generator) {
    for (const entity of page) { console.log('Entity:', entity) }
  }
} catch (error) {
  console.error('Request failed', error)
}

// callMethod provides manual control over the pagination process through the start parameter. It is suitable for scenarios where precise control over request batches is required. However, with large volumes of data, it may be less efficient compared to fetchListMethod.

try {
  const response = await $b24.callMethod('task.commentitem.getlist', {
    "TASKID": 8017,
    "ORDER": {
      "POST_DATE": "asc",
    },
    "FILTER": {
      "AUTHOR_ID": 503,
      ">=POST_DATE": "2025-01-01",
    }
  }, 0)
  const result = response.getData().result || []
  for (const entity of result) { console.log('Entity:', entity) }
} catch (error) {
  console.error('Request failed', error)
}
```

```js
BX24.callMethod(
    'task.commentitem.getlist',
    {
        "TASKID": 8017,
        "ORDER": {
            "POST_DATE": "asc",
        },
        "FILTER": {
            "AUTHOR_ID": 503,
            ">=POST_DATE": "2025-01-01",
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
    'task.commentitem.getlist',
    [
        'TASKID' => 8017,
        'ORDER' => [
            'POST_DATE' => 'asc',
        ],
        'FILTER' => [
            'AUTHOR_ID' => 503,
            '>=POST_DATE' => '2025-01-01',
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
            "POST_MESSAGE_HTML": null,
            "ID": "3157",
            "AUTHOR_ID": "503",
            "AUTHOR_NAME": "John Smith",
            "AUTHOR_EMAIL": "",
            "POST_DATE": "2025-07-15T14:31:00+02:00",
            "POST_MESSAGE": "Photos attached",
            "ATTACHED_OBJECTS": {
                "973": {
                    "ATTACHMENT_ID": "973",
                    "NAME": "photo1.png",
                    "SIZE": "1495700",
                    "FILE_ID": "4755",
                    "DOWNLOAD_URL": "/bitrix/tools/disk/uf.php?attachedId=973&auth%5Bauth%5D=3edf7ca92&action=download&ncc=1",
                    "VIEW_URL": "/bitrix/tools/disk/uf.php?attachedId=973&auth%5Bauth%5D=3edf7ca92&action=show&ncc=1"
                },
                "975": {
                    "ATTACHMENT_ID": "975",
                    "NAME": "photo2.png",
                    "SIZE": "1017053",
                    "FILE_ID": "4753",
                    "DOWNLOAD_URL": "/bitrix/tools/disk/uf.php?attachedId=975&auth%5Bauth%5D=3edf7ca92&action=download&ncc=1",
                    "VIEW_URL": "/bitrix/tools/disk/uf.php?attachedId=975&auth%5Bauth%5D=3edf7ca92&action=show&ncc=1"
                }
            }
        },
        {
            "POST_MESSAGE_HTML": null,
            "ID": "3155",
            "AUTHOR_ID": "503",
            "AUTHOR_NAME": "John Smith",
            "AUTHOR_EMAIL": "",
            "POST_DATE": "2025-07-15T14:30:00+02:00",
            "POST_MESSAGE": "Prepared new photos",
            "ATTACHED_OBJECTS": {}
        }
    ],
    "time": {
        "start": 1753270901.224447,
        "finish": 1753270901.343166,
        "duration": 0.11871910095214844,
        "processing": 0.06380701065063477,
        "date_start": "2025-07-23T14:41:41+02:00",
        "date_finish": "2025-07-23T14:41:41+02:00",
        "operating_reset_at": 1753271501,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | An array of objects. Each object contains a description of the comment |
| **POST\_MESSAGE\_HTML**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | HTML code of the comment |
| **ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Comment identifier |
| **AUTHOR\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Comment author's identifier |
| **AUTHOR\_NAME**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Comment author's name |
| **AUTHOR\_EMAIL**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Comment author's email |
| **POST\_DATE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Date and time of comment creation |
| **POST\_MESSAGE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Text of the comment |
| **ATTACHED\_OBJECTS**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | An object containing information about attachments. The key of the object is the attachment identifier, and the value is an object with [file description](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-get-list.html#attached-objects) |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html#time) | Information about the request execution time |

### ATTACHED\_OBJECTS Object

| **Name**   `type` | **Description** |
| --- | --- |
| **ATTACHMENT\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Attachment identifier |
| **NAME**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | File name |
| **SIZE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | File size in bytes |
| **FILE\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | File identifier on Drive |
| **DOWNLOAD\_URL**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | URL for downloading the file |
| **VIEW\_URL**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | URL for viewing the file |

HTTP status: **400**

```json
{
    "error":"ERROR_CORE",
    "error_description":"TASKS_ERROR_EXCEPTION_#256; Param #1 (arOrder) for method ctaskcommentitem::getlist() must not contain key ">=POST_DATE".; 256/TE/WRONG_ARGUMENTS.<br>"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#8; Action failed; 8/TE/ACTION\_FAILED\_TO\_BE\_PROCESSED | An incorrect parameter value is specified or there are no access permissions for the task |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#256; Param #0 (taskId) for method ctaskcommentitem::getlist() expected to be of type "integer", but given something else.; 256/TE/WRONG\_ARGUMENTS | An incorrect type of value is specified for the parameter, for example, for `TASKID` |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#256; Param #1 (arOrder) for method ctaskcommentitem::getlist() must not contain key ">=POST\_DATE".; 256/TE/WRONG\_ARGUMENTS | Parameters are specified in the wrong order |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#256; Param #2 (arFilter) for method ctaskcommentitem::getlist() must not contain key "%POST\_DATE".; 256/TE/WRONG\_ARGUMENTS | The parameter name or prefix for filtering is incorrectly specified |

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

- [Comments in Tasks: Overview of Methods](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/index.html)
- [Add Comment task.commentitem.add](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-add.html)
- [Update Comment task.commentitem.update](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-update.html)
- [Get Comment by ID task.commentitem.get](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-get.html)
- [Delete Comment task.commentitem.delete](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-delete.html)