---
title: "Add Comment task.commentitem.add | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/comment-item/task-comment-item-add.html"
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

The method `task.commentitem.add` adds a new comment to a task.

The development of the method has been halted since version `tasks 25.700.0`

The method `task.commentitem.add` continues to work, but there is a more current equivalent [tasks.task.chat.message.send](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/rest-v3/tasks/tasks-task-chat-message-send.html).

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **TASKID** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Task identifier.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/tasks-task-add.html) or by using the [getting the list of tasks](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/tasks-task-list.html) method |
| **FIELDS** \*   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Object with [comment fields](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-add.html#fields) |

### FIELDS Parameter

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **POST\_MESSAGE** \*   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Message text |
| **AUTHOR\_ID**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Identifier of the user on behalf of whom the comment should be created.  You can get the user identifier using the [user.get](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/user/user-get.html) method.  The method `task.commentitem.add` allows any user to add a comment on behalf of someone else |
| **POST\_DATE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Message date |
| **UF\_FORUM\_MESSAGE\_DOC**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Array with file identifiers from Drive. Prefix each identifier with `n`, for example, `['n123', 'n456', ... ]`.  The author of the comment must have access to the attached files; otherwise, the method will return an error |

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
-d '{"TASKID":8017,"FIELDS":{"POST_MESSAGE":"Text of the new comment for the task","AUTHOR_ID":503,"POST_DATE":"2025-07-15T14:30:00+02:00","UF_FORUM_MESSAGE_DOC":["n4755","n4753"]}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.commentitem.add
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASKID":8017,"FIELDS":{"POST_MESSAGE":"Text of the new comment for the task","AUTHOR_ID":503,"POST_DATE":"2025-07-15T14:30:00+02:00","UF_FORUM_MESSAGE_DOC":["n4755","n4753"]},"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.commentitem.add
```

```js
try
{
    const response = await $b24.callMethod(
        'task.commentitem.add',
        {
            "TASKID": 8017,
            "FIELDS": {
                "POST_MESSAGE": "Text of the new comment for the task",
                "AUTHOR_ID": 503,
                "POST_DATE": "2025-07-15T14:30:00+02:00",
                "UF_FORUM_MESSAGE_DOC": ["n4755", "n4753"]
            }
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

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'task.commentitem.add',
            [
                'TASKID' => 8017,
                'FIELDS' => [
                    'POST_MESSAGE'         => 'Text of the new comment for the task',
                    'AUTHOR_ID'            => 503,
                    'POST_DATE'            => '2025-07-15T14:30:00+02:00',
                    'UF_FORUM_MESSAGE_DOC' => ['n4755', 'n4753'],
                ],
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    // Your data processing logic
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error adding task comment: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.commentitem.add',
    {
        "TASKID": 8017,
        "FIELDS": {
            "POST_MESSAGE": "Text of the new comment for the task",
            "AUTHOR_ID": 503,
            "POST_DATE": "2025-07-15T14:30:00+02:00",
            "UF_FORUM_MESSAGE_DOC": ["n4755", "n4753"]
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
    'task.commentitem.add',
    [
        'TASKID' => 8017,
        'FIELDS' => [
            'POST_MESSAGE' => 'Text of the new comment for the task',
            'AUTHOR_ID' => 503,
            'POST_DATE' => '2025-07-15T14:30:00+02:00',
            'UF_FORUM_MESSAGE_DOC' => ['n4755', 'n4753']
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
    "result": 3141,
    "time": {
        "start": 1753262861.683775,
        "finish": 1753262862.001611,
        "duration": 0.31783604621887207,
        "processing": 0.27428317070007324,
        "date_start": "2025-07-23T12:27:41+02:00",
        "date_finish": "2025-07-23T12:27:42+02:00",
        "operating_reset_at": 1753263461,
        "operating": 0.2742629051208496
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html) | Identifier of the new comment |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/data-types.html#time) | Information about the request execution time |

HTTP status: **400**

```json
{
    "error":"ERROR_CODE",
    "error_description":"Insufficient permissions to add a comment.<br>"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `ERROR_CORE` | Comment text not specified | Required parameter `POST_MESSAGE` not provided or is empty |
| `ERROR_CORE` | Insufficient permissions to add a comment | No access permission to the task |
| `ERROR_CORE` | File not found | File from the `UF_FORUM_MESSAGE_DOC` parameter not found or the author does not have access to it |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#256; Param #1 (arFields) for method ctaskcommentitem::add() must not contain key `<FIELD_NAME>`.; 256/TE/WRONG\_ARGUMENTS | Field `<FIELD_NAME>` cannot be used in the method |
| `ERROR_CORE` | TASKS\_ERROR\_EXCEPTION\_#256; Param #0 (taskId) for method ctaskcommentitem::add() expected to be of type "integer", but given something else.; 256/TE/WRONG\_ARGUMENTS | Incorrect value type for the parameter, for example, for `TASKID` |

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
- [Update Comment task.commentitem.update](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-update.html)
- [Get Comment by ID task.commentitem.get](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-get.html)
- [Get the list of comments task.commentitem.getlist](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-get-list.html)
- [Delete Comment task.commentitem.delete](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/api-reference/tasks/comment-item/task-comment-item-delete.html)
- [How to Create a Comment in a Task and Attach a File](https://apidocs.bitrix24.com/api-reference/tasks/comment-item/tutorials/tasks/how-to-create-comment-with-file.html)