---
title: "Get Comment by ID task.commentitem.get | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/comment-item/task-comment-item-get.html"
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

The method `task.commentitem.get` retrieves a comment by its ID.

Development of the method has been halted since version of the module `tasks 25.700.0`

The method `task.commentitem.get` does not work in the [new task card](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/tasks-new.html), use the method [im.dialog.messages.get](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/chats/messages/im-dialog-messages-get.html) for working with task chat.

## Method Parameters

Pass parameters in the request according to the order in the table. If the order is violated, the request will return an error.

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **TASKID** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Task ID.  The task ID can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/tasks-task-add.html) or by using the [method to get the list of tasks](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/tasks-task-list.html) |
| **ITEMID** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Comment ID.  The comment ID can be obtained when [adding a new comment](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-add.html) or by using the [method to get the list of comments](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-get-list.html) |

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
-d '{"TASKID":8017,"ITEMID":3157}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.commentitem.get
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASKID":8017,"ITEMID":3157,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.commentitem.get
```

```js
try
{
    const response = await $b24.callMethod(
        'task.commentitem.get',
        {
            "TASKID": 8017,
            "ITEMID": 3157
        }
    );
    
    const result = response.getData().result;
    console.info(result);
    console.log(result);
}
catch( error )
{
    console.error('Error:', error);
}
```

```js
BX24.callMethod(
    'task.commentitem.get',
    {
        "TASKID": 8017,
        "ITEMID": 3157
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
    'task.commentitem.get',
    [
        'TASKID' => 8017,
        'ITEMID' => 3157
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
        "POST_MESSAGE_HTML": null,
        "ID": "3157",
        "AUTHOR_ID": "503",
        "AUTHOR_NAME": "John Smith",
        "AUTHOR_EMAIL": "",
        "POST_DATE": "2025-07-15T14:30:00+02:00",
        "POST_MESSAGE": "Text of the new comment for the task",
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
    "time": {
        "start": 1753274863.280788,
        "finish": 1753274863.362892,
        "duration": 0.08210396766662598,
        "processing": 0.04009890556335449,
        "date_start": "2025-07-23T15:47:43+02:00",
        "date_finish": "2025-07-23T15:47:43+02:00",
        "operating_reset_at": 1753275463,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Object describing the comment |
| **POST\_MESSAGE\_HTML**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | HTML code of the comment |
| **ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Comment ID |
| **AUTHOR\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Author ID of the comment |
| **AUTHOR\_NAME**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Name of the comment author |
| **AUTHOR\_EMAIL**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Email of the comment author |
| **POST\_DATE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Date and time of comment creation |
| **POST\_MESSAGE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Text of the comment |
| **ATTACHED\_OBJECTS**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Object containing information about attachments. The key of the object is the attachment ID, and the value is the object with [file description](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-get.html#attached-objects) |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html#time) | Information about the request execution time |

### ATTACHED\_OBJECTS Object

| **Name**   `type` | **Description** |
| --- | --- |
| **ATTACHMENT\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Attachment ID |
| **NAME**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | File name |
| **SIZE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | File size in bytes |
| **FILE\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | File ID on Drive |
| **DOWNLOAD\_URL**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | URL for downloading the file |
| **VIEW\_URL**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | URL for viewing the file |

HTTP Status: **400**

```json
{
    "error":"ERROR_CODE",
    "error_description":"TASKS_ERROR_EXCEPTION_#512; Check listitem not found or not accessible; 512/TE/ITEM_NOT_FOUND_OR_NOT_ACCESSIBLE.<br>"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#512; Check listitem not found or not accessible; 512/TE/ITEM\_NOT\_FOUND\_OR\_NOT\_ACCESSIBLE | The error is returned in the following cases:  - Incorrect order of parameters in the method - Task or comment with the specified ID not found - No access permission to the task |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#256; Param #0 (taskId) for method ctaskcommentitem::get() expected to be of type "integer", but given something else.; 256/TE/WRONG\_ARGUMENTS | Incorrect value type for the parameter, for example, for `TASKID` |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#256; Param #1 (itemId) expected by method ctaskcommentitem::get(), but not given.; 256/TE/WRONG\_ARGUMENTS | Required parameter not specified, for example, `ITEMID` |

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
- [Get the list of comments task.commentitem.getlist](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-get-list.html)
- [Delete Comment task.commentitem.delete](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-delete.html)
- [How to Create a Comment in a Task and Attach a File](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/tutorials/tasks/how-to-create-comment-with-file.html)