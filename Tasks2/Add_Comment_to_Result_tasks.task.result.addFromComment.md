---
title: "Add Comment to Result tasks.task.result.addFromComment | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/result/tasks-task-result-add-from-comment.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user with access to the task

The method `tasks.task.result.addFromComment` pins a comment as the result of a task.

A user can pin only their own comment as a result. An administrator can pin any user's comment, becoming the author of the result.

When working with the [new task detail form](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/tasks-new.html) with chat from version `tasks 25.700.0`, the method does not work.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **commentId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The identifier of the comment to be pinned as the result.  The comment identifier can be obtained when [adding a new comment](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/comment-item/task-comment-item-add.html) or using the [method for retrieving the list of comments](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/comment-item/task-comment-item-get-list.html) |

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
-d '{"commentId":3199}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.result.addFromComment
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"commentId":3199,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.task.result.addFromComment
```

```javascript
try
{
    const response = await $b24.callMethod(
        'tasks.task.result.addFromComment',
        {
            commentId: 3199,
        }
    );
    
    const result = response.getData().result;
    console.log('Task result added from comment:', result);
    
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
            'tasks.task.result.addFromComment',
            [
                'commentId' => 3199
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error adding task result from comment: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.task.result.addFromComment',
    {
        "commentId": 3199
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
    'tasks.task.result.addFromComment',
    [
        'commentId' => 3199
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
        "id": 21,
        "taskId": 8017,
        "commentId": 3199,
        "createdBy": 503,
        "createdAt": "2025-07-13T14:30:00+02:00",
        "updatedAt": "2025-07-13T14:30:00+02:00",
        "status": 0,
        "text": "Sent documents to the client. The client promises to respond on [B]Monday[\/B].",
        "formattedText": "Sent documents to the client. The client promises to respond on \u003Cb\u003EMonday\u003C\/b\u003E.",
        "files": null
    },
    "time": {
        "start": 1755597246.027815,
        "finish": 1755597246.115861,
        "duration": 0.08804583549499512,
        "processing": 0.05956697463989258,
        "date_start": "2025-08-19T12:54:06+02:00",
        "date_finish": "2025-08-19T12:54:06+02:00",
        "operating_reset_at": 1755597846,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | An object describing the pinned result |
| **id**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The identifier of the result |
| **taskId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The identifier of the task |
| **commentId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The identifier of the comment pinned as the result |
| **createdBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The identifier of the user who pinned the result |
| **createdAt**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The date and time the result was pinned in ISO 8601 format |
| **updatedAt**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The date and time of the last update of the result in ISO 8601 format |
| **status**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The status of the result. Possible values:  - `0` — result is open - `1` — result is closed  The result becomes closed after the task is completed and retains this status after the task is resumed. Only new results in an unfinished task will be open.  A comment with an open result cannot be added again as a result. If the result is closed, adding is possible |
| **text**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The text of the result |
| **formattedText**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The formatted text of the result |
| **files**   `null` | Has the value `null`.  The list of files attached to the result can be obtained using the [tasks.task.result.list](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/result/tasks-task-result-list.html) method |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html#time) | Information about the time taken for the request |

HTTP status: **400**

```json
{
    "error":"0",
    "error_description":"Comment not found."
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `0` | Access denied. | The user does not have permission to access the task or the comment does not belong to the user |
| `0` | Result already exists. | The comment is already pinned as a result |
| `100` | Invalid value {value} to match with parameter {commentId}. Should be value of type int. | An invalid type value was passed in the `commentId` parameter. It should be of type `integer` |
| `0` | Comment not found. | A comment with that identifier does not exist |

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

- [Task Results: Overview of Methods](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/result/index.html)
- [Get the list of task results tasks.task.result.list](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/result/tasks-task-result-list.html)
- [Remove Comment from Result tasks.task.result.deleteFromComment](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/result/tasks-task-result-delete-from-comment.html)